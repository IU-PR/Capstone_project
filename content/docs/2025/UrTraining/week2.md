# Report 2. Initial Design & Elaboration

# UrTraining

**Authors:** Ildar Rakiev, Makar Dyachenko, Salavat Faizullin, Egor Chernobrovkin, Alexandra Starikova, Ilona Dziurava, Anisya Kochetkova

**Date:** June 2025

# Team Members

| **Team Member**     | **Telegram**   | **Email Address**                    | **Role**          |
| ------------------- | -------------- | ------------------------------------ | ----------------- |
| Ildar Rakiev (Lead) | @mescudiway    | i.rakiev@innopolis.university        | Backend / Design  |
| Makar Dyachenko     | @index099      | m.dyachenko@innopolis.university     | Frontend / Design |
| Salavat Faizullin   | @FSA_2005      | s.faizullin@innopolis.university     | Backend           |
| Egor Chernobrovkin  | @lolyhop       | e.chernobrovkin@innopolis.university | ML                |
| Alexandra Starikova | @lexandrinnn_t | a.nasibullina@innopolis.university   | ML                |
| Ilona Dziurava      | @a_b_r_i_c_o_s | il.dziurava@innopolis.university     | PM / Frontend     |
| Anisya Kochetkova   | @anis1305      | a.kochetkova@innopolis.university    | Backend           |

---

# Requirements

## User Story and Acceptance Criteria

| **User Story**                                                                                                                                 | **Acceptance Criteria**                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **As a new user,** I want to select a coach or trainee role, so that I can access features relevant to my role.                                | - Role selection is required during registration. <br> - Role-specific features are only available after selecting a role.                                                                                  |
| **As a new user,** I want to register as a trainee, so that I can start training.                                                              | - Registration form tailored to trainees. <br> - Successful registration logs in the user as a trainee.                                                                                                     |
| **As a new trainee,** I want to see an explanation page before the questionnaire, so that I understand its purpose.                            | - Page includes short info about data collection, estimated time, and a progress indicator.                                                                                                                 |
| **As a new trainee,** I want the questionnaire to take no more than 5 minutes, so that I don’t waste time.                                     | - Optimized for completion within 5 minutes.                                                                                                                                                                |
| **As a new trainee,** I want to provide my name, so that the system knows how to address me.                                                   | - Field “What should we call you?” with a brief explanation.                                                                                                                                                |
| **As a new trainee,** I want to provide basic personal info, so that I receive more relevant plans.                                            | - Fields: gender, age, height, weight.                                                                                                                                                                      |
| **As a new trainee,** I want to choose training goals, so that I receive relevant programs.                                                    | - Goals: Weight loss, Muscle gain, Endurance, Flexibility, Fitness maintenance, Competition prep, Stress relief. <br> - Can choose up to 2.                                                                 |
| **As a new trainee,** I want to describe my experience level, so that plan difficulty matches me.                                              | - Options: Beginner, Intermediate, Advanced. <br> - Also ask: “How often have you trained in the last 3 months?” with set choices.                                                                          |
| **As a new trainee,** I want to specify my training location, so I get suitable suggestions.                                                   | - Options: Gym, Home, Pool, Outdoors.                                                                                                                                                                       |
| **As a new trainee,** I want to describe my training environment, so the system aligns equipment accordingly.                                  | - **Gym:** Full center or basic equipment. <br> - **Home:** Some equipment or bodyweight only. <br> - **Pool:** No extra questions. <br> - **Outdoors:** With or without workout stations.                  |
| **As a new trainee,** I want to specify workout length, so they fit my schedule.                                                               | - Options: Up to 30 min, 30–45 min, 45–60 min, > 60 min.                                                                                                                                                    |
| **As a new trainee,** I want to rate interest in training types, so I get personalized workouts.                                               | - Types: Strength, Cardio, HIIT, Yoga/Pilates, Functional, Stretching. <br> - Rating: 1–5 stars.                                                                                                            |
| **As a new trainee,** I want to indicate health limitations, so I don’t risk injury.                                                           | - Ask: “Do you have joint/back problems?” and “Any chronic diseases affecting exercise?” <br> - If yes: show a “Tell us more” field and display disclaimer: “Consult your doctor before starting training.” |
| **As a new trainee,** I want to navigate questionnaire steps, so I can review/correct answers.                                                 | - “Back” and “Next” buttons available on all steps.                                                                                                                                                         |
| **As a new trainee,** I want a final confirmation page after the questionnaire, so I know my answers were saved.                               | - Show confirmation message with summary or success notification.                                                                                                                                           |
| **As a new trainee,** I want my training plan generated under 15 seconds, so I can begin quickly.                                              | - Plan generation completes in under 15 seconds.                                                                                                                                                            |
| **As a new trainee,** I want my questionnaire progress saved if I leave early, so I can continue later.                                        | - Auto-save and restore questionnaire state.                                                                                                                                                                |
| **As a new user,** I want to register as a trainer, so that I can share my training plans.                                                     | - Registration form tailored to trainers. <br> - Successful registration logs in the user as a trainer.                                                                                                     |
| **As a new trainer,** I want to see an explanation page before the questionnaire, so that I understand what is collected.                      | - Page has a brief explanation, progress indicator, and an estimated time.                                                                                                                                  |
| **As a new trainer,** I don’t want the questionnaire to take more than 5 minutes, so it’s quick.                                               | - Average completion time ≤ 5 minutes.                                                                                                                                                                      |
| **As a new trainer,** I want to provide my name, so the system knows how to refer to me.                                                       | - Field “How would you like us to call you?” with explanation.                                                                                                                                              |
| **As a new trainer,** I want to share my work experience, so clients see my professionalism.                                                   | - Input for total years of experience and a background description.                                                                                                                                         |
| **As a new trainer,** I want to enter my age, so users get context.                                                                            | - Number field with validation (18+).                                                                                                                                                                       |
| **As a new trainer,** I want to specify training types I offer, so users know my expertise.                                                    | - Multi-choice: Strength, Cardio, HIIT, Yoga/Pilates, Functional, Stretching.                                                                                                                               |
| **As a new trainer,** I want to upload certifications, so clients know I'm qualified.                                                          | - Optional file upload: PDF, JPG, PNG.                                                                                                                                                                      |
| **As a trainer,** I want to create courses, so I can share my knowledge.                                                                       | - “Create Course” button opens the course creation form.                                                                                                                                                    |
| **As a trainer,** I want to enter course basic info, so users understand it.                                                                   | - Form: course name, auto-filled trainer, description.                                                                                                                                                      |
| **As a trainer,** I want to select training types for my course, so users can filter accordingly.                                              | - Multi-select training types; option to add custom types.                                                                                                                                                  |
| **As a trainer,** I want to specify course goal, so users find relevant programs.                                                              | - Multi-select up to 2: goals like Weight Loss, Muscle Gain, etc.                                                                                                                                           |
| **As a trainer,** I want to indicate course location, so users filter by environment.                                                          | - Multi-select: Home (with/without equipment), Gym, Outdoors, Pool, Universal.                                                                                                                              |
| **As a trainer,** I want to define difficulty level, so users find the right challenge.                                                        | - Single-select: Beginner, Intermediate, Advanced, All Levels.                                                                                                                                              |
| **As a trainer,** I want to indicate course duration (weeks), so users know commitment.                                                        | - Dropdown: 1 / 2 / 5 weeks.                                                                                                                                                                                |
| **As a trainer,** I want to set weekly training frequency, so users understand schedule.                                                       | - Single choice: 1–2, 3–4, or 5–6 times/week.                                                                                                                                                               |
| **As a trainer,** I want to specify session duration, so users know how much time is needed.                                                   | - Single choice: up to 30 min, 30–45 min, 45–60 min, > 60 min.                                                                                                                                              |
| **As a trainer,** I want to define target age group, so I reach the right audience.                                                            | - Multi-select: Teens, Young Adults, Adults, Seniors, All ages.                                                                                                                                             |
| **As a trainer,** I want to set gender orientation of the course, so users know if it suits them.                                              |                                                                                                                                                                              |
| **As a trainer,** I want to specify suitability for physical limitations, so those users feel safe joining.                                    | - Multi-select from listed conditions; include “No adaptation” for healthy.                                                                                                                                 |
| **As a trainer,** I want to list required equipment, so users prepare in advance.                                                              | - Multi-select from a comprehensive equipment list; “Other – specify.”                                                                                                                                      |
| **As a trainer,** I want automatic detection of course language, so localization is seamless.                                                  | - System auto-detects language (English or others).                                                                                                                                                         |
| **As a trainer,** I want automatic identification of visual content type, so users know what to expect.                                        | - System auto-categorizes visuals (photos, videos, animations, charts, minimal visuals).                                                                                                                    |
| **As a trainer,** I want to select feedback options for my course, so users know how to contact me.                                            | - Multi-select feedback options: comments, personal consults, group sessions, chat, or none.                                                                                                                |
| **As a trainer,** I want to pick up to 10 tags, so users can search effectively.                                                               | - Multi-select from validated tag list (weight loss, strength, flexibility, etc.), up to 10.                                                                                                                |
| **As a trainer,** I want to see my course performance metrics, so I can track engagement.                                                      | - Display average rating, active participants count, number of reviews.                                                                                                                                     |
| **As a trainer,** I want my certification data to auto-fill in my course, so users see my credibility.                                         | - Auto-fill from profile: certification type, level, specialization.                                                                                                                                        |
| **As a trainer,** I want my experience data to auto-fill, so clients quickly see my background.                                                | - Auto-fill: years of experience, specializations, number of created courses, average rating.                                                                                                               |
| **As a trainer,** I want to upload training plans, so I can help people train.                                                                 | - File upload interface for training plan materials (PDF, video, structured data, etc.).                                                                                                                    |
| **As a user on the platform,** I want to receive a recommended training plan based on my preferences, so that I don’t have to browse manually. | - Onboarding form captures goals, equipment, frequency, duration, restrictions. <br> - Recommendation model suggests top 3–5 relevant plans. <br> - User can view details or skip to catalog.               |
| **As a user on the platform,** I want to view a list of available training plans, so I can choose the best fit.                                | - Catalog shows plan cover, title, coach name, duration, tags. <br> - Filters: goal, equipment, duration, frequency, difficulty, coach. <br> - Sorting: relevance, newest, most popular, rating.            |
| **As a user on the platform,** I want to open a detailed training plan page, so that I can understand its structure.                           | - Plan detail includes full description, week-by-week breakdown, expected results, visuals (if available), trainer info, required equipment. <br> - “Start plan” button begins user progress tracking.      |
| **As a user following a training plan,** I want to mark workouts as complete, so that I can track my progress.                                 | - Each session has a “Mark as done” button or checkbox. <br> - Progress per user and per plan is saved. <br> - Completed session count is displayed (e.g., “3/10 sessions completed”).                      |

## Backlog

![Backend1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/backend1.png)
![Backend2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/backend2.png)
![Frontend1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/frontend1.png)
![Frontend2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/frontend2.png)
![ML](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/ml.png)
![Design1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/design1.png)
![Design2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/design2.png)
![Report](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/report.png)
![Github](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/git.png)

---

# Design

## Core Application Design

The core application design can be viewed [here](https://www.figma.com/design/UzErz9hYhXC1HQSKE0cEQO/UrTraining-design-draft?node-id=0-1&t=lTjrWgRml9VbQjDp-1). These initial designs form the foundation of the core user experience. Below are the key screens that have been designed so far:

- **User Questionnaire**: A multi-step form where the user answers questions to receive a personalized training program.  
  ![Form Prototype](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/FormPrototype.png)

- **Prototype Review Window**: Allows users to preview and modify their recommended training programs.  
  ![Training Aditor Prototype part 1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/TrainingEditorPrototype.png)

  ![Training Aditor Prototype part 2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/TrainingEditorPrototype2.png)

- **Training Plan Catalog**: Displays a list of available training programs when the user clicks on the **"Catalog"** tab in the top navigation bar.  
  ![Catalogue of training](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Catalogueoftrainings.png)

- **Training Card Overview**: A detailed view of an individual training plan, including its description, difficulty level, and schedule.  
  ![Card of training plan](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Cardoftrainingplan.png)

## User Flow Diagram

User flow diagrams for key interactions can be found here:
[User flow diagram](https://www.figma.com/design/hi2bbbi7k00Ri0jgOfRlqE/Untitled?node-id=0-1&p=f&t=JFwQyUtexNgPHoQM-0)

---

# Frontend

During Week 2, we implemented several key pages and set up basic routing for the application:

- **Welcome Page with Role Selection (User / Trainer)**  
  Implemented an entry screen that directs users based on their role.  
  [Welcome Page Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/82749b20b133652e39a3babdabc69a850ab9ad89)

- **Authentication Pages (Signup / Login)**  
  Added user authentication forms for registration and login, with working layout and form validation.  
  [Signup Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/a564ea85a27cbdb4a7f65e903c46c91623c6f5a7)  
  [Login Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/766c215457054c0f67b19731ce8d51b845d6a753)

- **Basic Routing Setup**  
  Established initial routing logic to navigate between the main pages.  
  [Routing Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d3b51df4fb867abb5b438d2fee1b18794c09ef94)

- **User Questionnaire Page**  
  Created a multi-step form displayed after registration, allowing users to specify preferences for personalized training programs.  
  [Questionnaire Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/2dba37b9608774734c4b61f34956e245c40a64c7)

Fronted part is deployed [here](http://31.59.121.167).

---

# Backend

Progress during Week 2 was focused on defining the API contract and preparing the backend for upcoming integration with the frontend.

- **Basic Endpoints with Dummy Data**  
  One to two base endpoints with dummy responses were already implemented last week.  
  [Dummy Data Endpoints Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/dd42e75c9b8516b0741d2118fcf94203b93588d8)

- **Core Business Logic and API Implementation**  
  Added initial backend logic and API endpoints to support MVP features.  
  [Core Logic Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/bc7f5aa09aa3452171db3a5c819480c8a0e87221)

- **Database Integration**  
  Connected the project to the database and added a guide for working with it.  
  [Database Setup Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/3bba0ec5cc0aa7f85d3de85020d2eb2e0d54533f)

The following diagram illustrates the current architecture of our application: ![Architecture](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/ArchitectureDraft.png)

Backend part is deployed [here](http://31.59.121.167:8000/).

---

# ML System Design

## Overview

The ML system consists of two core components:

- **Recommendation System**: Delivers personalized course recommendations to users
- **Image-to-Tracker**: Converts exercise images into structured tracking programs

## Recommendation System

### Current Approach

Due to limited initial data, the system employs synthetic data generation for the first iteration model training.

### Data Generation Pipeline

#### User Data Structure

- **Profile Data**: Registration form responses (weight, fitness goals, experience level, etc.)
- **Interaction Metadata**: User engagement metrics (completed courses, retention rates, activity patterns)

#### Synthetic Data Generation Process

1. **User Profile Generation**

   - Multiple LLMs (DeepSeek, Gemma, LLaMA) generate diverse user profiles
   - Prompt engineering with seed phrases ensures profile diversity
   - Metadata generation aligned with corresponding user profiles
   - Target: 1,000 training examples for baseline model

2. **Course Data Generation**

   - Multiple LLMs generate the main content of exercises (for gym, swimming or other)
   - For each course type (gym, swimming, others) we generate separate training program
   - Finally, we align generated courses with coach-provided metadata forms (also generated by LLMs)

3. **Dataset Assembly**

   - For each user profile + metadata, DeepSeek R1 rearranges the courses (generates optimal course-user pairings for training data)

4. **Model Training**  
   The training process utilizes a bi-encoder architecture to learn meaningful representations of users and courses. It aims to maximize similarity between compatible user-course pairs while minimizing similarity for incompatible ones, enabling effective personalized recommendations through vector similarity search.

   **Architecture**:

   - Bi-encoder models (e5, bge-m3, or similar embeddings models)
   - Separate encoding for user profiles and course descriptions
   - Vector generation for both user queries and course documents

   **Training Objective**:

   - Contrastive learning approach using triplet, margin, or contrastive loss functions
   - Optimize embeddings to place similar user-course pairs closer in vector space

![BERT-like model](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/BERT-like.jpeg)

## Image-to-Tracker System

### Current Implementation

The system utilizes open-source visual language models (VLM) to extract structured data from exercise images.

**Process Flow**:

1. **Image Processing**: Vision-language model analyzes input images
2. **Text Extraction**: Converts visual content to structured JSON format:
   ```json
   [
     {
       "content": "exercise_description"
     }
   ]
   ```
3. **Tracker Mapping**: Each JSON object maps to a dedicated tracker page

### Future Development (won't be included in MVP)

**Data Collection Strategy**: - Use images from real coaches to build the dataset - Annotate those images by DeepSeek or assessors - Training pair generation: (image) → (structured_tracker_json)

# Users

To better understand how trainers create and structure their training programs, we asked several of them to share real examples. This research helps us design a more intuitive and relevant upload feature that aligns with their actual workflows.

Below are four examples of training programs provided by different trainers:

![Example 1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Tabl_box3.jpg)
![Example 2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/training.jpeg)
![Example 3](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/trainingplan.jpg)
![Example 4](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/example4.jpeg)

It turned out that most trainers write their programs using tables, while one of them prefers to save and structure their programs in Telegram saved messages.

---

# Weekly Progress Report

During the second week, our team transitioned from planning to early implementation. The primary focus was on expanding the initial requirements, creating design prototypes, and setting up foundational structures for both the frontend and backend.

| Team Member         | Contribution Description                                                                                                                                             | Contribution Link                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Ildar Rakiev        | Sign page implementation,  frontend and backend deploy, architecture of the application            | [Signin Page Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/766c215457054c0f67b19731ce8d51b845d6a753), [Architecture](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/ArchitectureDraft.png), [Frontend](http://31.59.121.167), [Backend](http://31.59.121.167:8000/)         |
| Makar Dyachenko     | Project structure in the frontend repository, welcome page implementation, signup page implementation, basic routing, user questionary page                                             | [Welcome Page Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/82749b20b133652e39a3babdabc69a850ab9ad89), [Signup Page Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/a564ea85a27cbdb4a7f65e903c46c91623c6f5a7), [Routing Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d3b51df4fb867abb5b438d2fee1b18794c09ef94), [Questionnaire Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/2dba37b9608774734c4b61f34956e245c40a64c7)         |
| Salavat Faizullin   | Core business logic and API implementation, database integration                                                                                                 | [API implementation](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/bc7f5aa09aa3452171db3a5c819480c8a0e87221), [Database Setup Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/3bba0ec5cc0aa7f85d3de85020d2eb2e0d54533f)         |
| Egor Chernobrovkin  | Research potential models/algorithms, EmbedderAPI & Docs with ML system design | [EmbedderAPI and Docs Pull Request](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/25)   |
| Alexandra Starikova | Start collecting/preparing a dataset, pipeline for generating sport programs via LLM | [Pipeline for generating programs Pull Request](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/26)        |
| Ilona Dziurava      | Report writing, user stories specification, backlog creation, contacting trainers for training form information | [Backlog](https://urtraining.yougile.com)   |
| Anisya Kochetkova   | User flow diagram for key interactions, basic endpoints   | [User flow diagram](https://www.figma.com/design/hi2bbbi7k00Ri0jgOfRlqE/Untitled?node-id=0-1&p=f&t=JFwQyUtexNgPHoQM-0), [Endpoints Commit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/dd42e75c9b8516b0741d2118fcf94203b93588d8) |

## Challenges & Solutions

One challenge we encountered was ensuring consistency between the frontend and backend specifications. We addressed this by closely aligning on the API contract early and scheduling regular sync meetings between the respective subteams.

## Conclusions & Next Steps

By the end of **Week 2**, we successfully transformed initial ideas into concrete requirements, established foundational designs, and set up project structures across the frontend and backend. The team now has a shared understanding of both the technical and functional aspects of the project, with wireframes, a prioritized backlog, and initial codebase scaffolding in place.

Looking ahead to **Week 3**, our focus will shift to **MVP development**, where we aim to implement core functionality and deliver at least one complete end-to-end user flow. This will involve connecting frontend components to backend endpoints, integrating with the database, and enabling meaningful interactions within the application.

### Next Steps for Week 3

- **Frontend**: Connect UI components to real backend data and handle basic user interactions.
- **Backend**: Implement core business logic and enable database operations for MVP features.
- **Database**: Finalize schema and ensure it supports the initial set of use cases.
- **Authentication**: Begin integrating simple user auth flows.
- **ML**: Train a basic model version and expose an API endpoint.
- **Testing & Demo Prep**: Ensure the MVP flow is stable enough for an internal demo.

This upcoming sprint will be critical in turning the project from a prototype into a working product.

**We confirm that the code in the main branch:**

In working condition.
Run via docker-compose.
