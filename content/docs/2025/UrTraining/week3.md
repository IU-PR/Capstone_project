# Report 3. MVP Development

# UrTraining

**Authors:** Ildar Rakiev, Makar Dyachenko, Salavat Faizullin, Egor Chernobrovkin, Alexandra Starikova, Ilona Dziurava, Anisya Kochetkova

**Date:** June 2025

# Team Members

| **Team Member**     | **Telegram**   | **Email Address**                    | **Role**          |
| ------------------- | -------------- | ------------------------------------ | ----------------- |
| Ildar Rakiev (Lead) | @mescudiway    | i.rakiev@innopolis.university        | Backend / Frontend|
| Makar Dyachenko     | @index099      | m.dyachenko@innopolis.university     | Frontend / Design |
| Salavat Faizullin   | @FSA_2005      | s.faizullin@innopolis.university     | Backend           |
| Egor Chernobrovkin  | @lolyhop       | e.chernobrovkin@innopolis.university | ML                |
| Alexandra Starikova | @lexandrinnn_t | a.nasibullina@innopolis.university   | ML                |
| Ilona Dziurava      | @a_b_r_i_c_o_s | il.dziurava@innopolis.university     | PM                |
| Anisya Kochetkova   | @anis1305      | a.kochetkova@innopolis.university    | Backend           |

---

# Implemented MVP features

## Fully Implemented User Flow
### **1. Registration → Questionnaire → Personalized Recommendations**  
- The user signs up, completes a brief survey, and receives a tailored list of ranked training programs.  

### **2. General Catalog Access**  
- The user can explore the full catalog of available training programs at any time.

**Visualization:**  
The user flow diagram can be seen below:
![Flow1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Flow1.png)
![Flow2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Flow2.png)

## Initial MVP scope:
- User registration for both trainers and clients
- User profile questionnaire
- Basic workout recommendations based on input
- Workout upload system for trainers (support for text, images, and PDFs)
- Content processing algorithm to structure uploaded workouts into standardized cards (with descriptions, structure, and tags)
- Basic recommendation system suggesting workouts based on user profiles
- Training catalog as a scrollable feed of exercise cards
- Purchase/save functionality for training programs

## Implemented Features:

### 1. User Registration for Both Trainers and Clients
Main page for not-logged users:
![Main not logged](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/GIFs/Main-page-navigation-_not-logged_.gif)
Main page for logged users:
![Main logged](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/GIFs/Main-page-navigation-_logged__1.gif)
Registration procedure:
![Client Registration](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/GIFs/Registration-procedure.gif)  
Login procedure:
![Login](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/GIFs/Login-procedure.gif)  

**Frontend Commits:**  
- [Signup page](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/a564ea85a27cbdb4a7f65e903c46c91623c6f5a7)  
- [Login page](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/766c215457054c0f67b19731ce8d51b845d6a753)  
- [Login and Signup merged into one component](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/b55aa20683c8c2ffb892f5e89e557a38ad769625)  
- [Login and Register system](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/4979170c830b287a5a387f5a01d32f0e9981e2d5)  

**Backend Commits:**  
- [Login and Signup endpoints](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/37)
- [Authorization tests](https://1drv.ms/w/c/64ea16d230ddc2a8/EUGtruTL7OBDkzu6iy-GvWMBxIpTIODg99z2NHmCfAO_5Q?e=3bzxYf)

**Integration Commits:**  
- [Backend and Frontend integration](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/fdfa3598e21fc859dc4ce62ec79970baf09ce212)  

### 2. User Profile Questionnaire
Survey procedure:
![Questionnaire](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/GIFs/Survey-procedure.gif)
Survey step 1:
![Step1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/Screenshots/Survey_step_1.png)
Survey step 2:
![Step2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/Screenshots/Survey_step_2.png)
Survey step 3:
![Step3](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/Screenshots/Survey_step_3.png)
Survey step 4:
![Step3](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/Screenshots/Survey_step_4.png)

**Frontend Commits:**  
- [Multi-step form implementation](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/2dba37b9608774734c4b61f34956e245c40a64c7)  
- [Improvements](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/1f76c69568a0587ab1694945277e9304888c4ce9)  
- [Submit form](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/c4ba8184d95efd34dfbf4ee0d1cf4e0ecbf518e0)  
- [Survey Routing](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/2f83d2132daa326e0af6cf1cf2045a316810fb6b)  
- [Questionnaire filling and sending](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d1770830868b8c8ac600a8e1bf140b3b5d02551b)  

**Backend Commits:**  
- [Endpoints for questionnaire](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d3732ad6efbfbbc338835963db8d9155d120bad3)  
- [Processing the user's form](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/32)  
- [User possible values](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/0a49c71cce5fed213ae3f8ca0f5ac438ee989980)

**Integration Commits:**  
- [Backend and Frontend integration](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d1770830868b8c8ac600a8e1bf140b3b5d02551b)  

### 3. Workout Recommendations

**Frontend Commits:**  
- [Course page](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/348f416c8f30109952e9792ad4ee75ae3a39b9ec)
- [Training card component](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/9096504cbaf2ea0570ad168220ef6bafeb21b16f)  

**Backend Commits:**  
- [Training models and endpoints](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/41/commits/f87f7ae2d307ff55f10203d915edf8394bf94156)  
- [Training metadata](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/41/commits/6d8f3db2a4d876809ab89d25d117f7a7b2258c89)  

**ML Commits:**  
- [Raw version of the dataset](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/ml/scripts/data/dataset.csv)
- [Raw dataset collection code](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/ml/scripts/prepare_dataset.ipynb)
- [Version of the dataset for training on TripletLoss](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/ml/scripts/data/training_data.csv)
- [Code for training](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/4bc2c85b2135004cd1bce474016e25cf232e33af)
- [Generated sport programs](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/54)
- Generated courses example
```
[
    {
        "Activity Type": "Yoga",
        "Program Goal": ["Competition Preparation"],
        "Training Environment": ["Pool"],
        "Difficulty Level": "Advanced",
        "Course Duration (weeks)": 2,
        "Weekly Training Frequency": "1-2 times",
        "Average Workout Duration": "45-60 minutes",
        "Age Group": ["Young Adults (18-30)"],
        "Gender Orientation": "For Men",
        "Physical Limitations": [],
        "Required Equipment": ["No Equipment", "Pull-up/Dip Bars"],
        "Course Language": "Other",
        "Visual Content": ["Progress Graphs"],
        "Trainer Feedback Options": ["Personal Consultations"],
        "Tags": [
            "Weight Loss", "Recovery", "Minimal Equipment", "Fat Burning",
            "Anti-Stress", "Explosive Strength", "Energy", "Arms", "Better Sleep"
        ],
        "Average Course Rating": 4.99,
        "Active Participants": 967,
        "Number of Reviews": 456,
        "Certification": {
            "Type": "ISSA",
            "Level": "Master",
            "Specialization": "Yoga"
        },
        "Experience": {
            "Years": 8,
            "Specialization": "Yoga",
            "Courses": 20,
            "Rating": 4.9
        },
        "Trainer Name": "Anna Smirnova",
        "Course Title": "Competition Preparation with Anna Smirnova",
        "training_plan": [
            {
                "title": "Week 1 - Day 1 (Monday, 60 min)",
                "exercises": [
                { "exercise": "Leg swings (front and back)", "repeats": "-", "sets": "1", "duration": "5 min", "rest": "-", "description": "Dynamic warm-up" },
                { "exercise": "Arm circles (forward and backward)", "repeats": "-", "sets": "1", "duration": "-", "rest": "-", "description": "Shoulder warm-up" },
                { "exercise": "Hip openers (lateral and forward)", "repeats": "-", "sets": "1", "duration": "-", "rest": "-", "description": "Hip mobility" },
                { "exercise": "Downward-Facing Dog (Adho Mukha Svanasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Foundational strength" },
                { "exercise": "Plank (Phalakasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Core activation" },
                { "exercise": "Tree Pose (Vrksasana)", "repeats": "-", "sets": "3", "duration": "30 sec (each leg)", "rest": "30 sec", "description": "Balance training" },
                { "exercise": "Triangle Pose (Trikonasana)", "repeats": "-", "sets": "3", "duration": "30 sec (each side)", "rest": "30 sec", "description": "Flexibility and balance" },
                { "exercise": "Seated Forward Fold (Paschimottanasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Hamstring stretch" },
                { "exercise": "Eagle Pose (Garudasana)", "repeats": "-", "sets": "3", "duration": "30 sec (each leg)", "rest": "30 sec", "description": "Balance and joint focus" },
                { "exercise": "Seated forward fold", "repeats": "-", "sets": "1", "duration": "-", "rest": "-", "description": "Cool-down stretch" },
                { "exercise": "Leg stretches (hamstrings and quadriceps)", "repeats": "-", "sets": "1", "duration": "-", "rest": "-", "description": "Post-workout recovery" },
                { "exercise": "Final relaxation", "repeats": "-", "sets": "1", "duration": "5 min", "rest": "-", "description": "Relaxation and breath" }
                ]
            },
            {
                "title": "Week 1 - Day 5 (Friday, 60 min)",
                "exercises": [
                { "exercise": "Downward-Facing Dog (Adho Mukha Svanasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Full-body strength" },
                { "exercise": "Plank (Phalakasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Core stability" },
                { "exercise": "Warrior Pose (Virabhadrasana)", "repeats": "-", "sets": "3", "duration": "30 sec (each leg)", "rest": "30 sec", "description": "Lower body power" },
                { "exercise": "Seated Spinal Twist (Bharadvajasana)", "repeats": "-", "sets": "3", "duration": "30 sec (each side)", "rest": "30 sec", "description": "Spinal flexibility" },
                { "exercise": "Pigeon Pose (Eka Pada Rajakapotasana)", "repeats": "-", "sets": "3", "duration": "30 sec (each leg)", "rest": "30 sec", "description": "Hip opener" },
                { "exercise": "Crow Pose (Bakasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Balance and strength" }
                ]
            },
            {
                "title": "Week 2 - Day 7 (Monday, 60 min)",
                "exercises": [
                { "exercise": "Boat Pose (Paripurna Navasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Core focus" },
                { "exercise": "Side Plank (Vasisthasana)", "repeats": "-", "sets": "3", "duration": "30 sec (each side)", "rest": "30 sec", "description": "Obliques and core" },
                { "exercise": "Bridge Pose (Setu Bandha Sarvangasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Back and glutes" },
                { "exercise": "Headstand (Sirsasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Inversion challenge" },
                { "exercise": "Crow Pose (Bakasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Balance and arm strength" },
                { "exercise": "Tree Pose (Vrksasana)", "repeats": "-", "sets": "3", "duration": "30 sec", "rest": "30 sec", "description": "Balance posture" }
                ]
            }
        ],
        "id": "c217bc40-7553-42f9-90cd-339013cfe3b5"
    }
```  

**Integration:**  
- [Backend and Frontend integration](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d1770830868b8c8ac600a8e1bf140b3b5d02551b)

### 4. Training Catalog
Catalogue of courses and course card:
![Catalog](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/media/GIFs/Catalogue-of-courses-and-course-card.gif)  

**Frontend Commits:**  
- [Catalogue of trainings](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/9096504cbaf2ea0570ad168220ef6bafeb21b16f)
- [Course Catalogue improvements](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/a490c917671d7826650d153dacad6f812dcd9f1c)

**Backend Commits:**  
- [Structure of the training model](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/51)
- [Refine training model and endpoints](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/53)

---

# Deploy
Fronted part is deployed [here](http://31.129.96.182/).

Backend part is deployed [here](http://31.129.96.182:8000/).

ML part is deployed [here](http://31.129.96.182:1337/)


# Updated API documentation

The updated API documentation can be found by the link: [API documentation](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/backend/ENDPOINTS.md)

This file contains comprehensive API documentation for an application backend. It outlines available RESTful endpoints grouped by functionality, including user registration and authentication, profile and training data management, and trainer-related features. Each endpoint is described with its purpose, method, URL, authentication requirements, request/response formats, and possible error responses. This documentation supports both frontend integration and backend maintenance.

---

# Internal demo notes
During the demo, we showed the full flow of user registration and login. The basic authentication system is already in place and working smoothly. After signing up, users can fill out a questionnaire, which is an essential part of collecting input for future recommendations. The form is functional, and the collected data is being processed on the backend.

We also walked through the catalog: users can browse available training programs and navigate into specific workout lists. While the connection to the ML model isn’t finished yet, we mentioned that API integration for model-based recommendations is planned and will be added soon.

The feedback was mostly focused on improving the UI, because some parts still look rough and need polishing. It was suggested to refine the layout, make forms more responsive, make text with program description bigger, remove non-functional buttons and ensure the overall design feels more cohesive and user-friendly.

---

# Weekly Progress Report

During the second week, our team transitioned from planning to early implementation. The primary focus was on expanding the initial requirements, creating design prototypes, and setting up foundational structures for both the frontend and backend.

| Team Member (Role)         | Contribution Description                                                                                                                                             | Contribution Link                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Ildar Rakiev (Backend/Frontend Lead) | Implemented the trainer registration and trainee questionnaire features, including frontend forms and backend integration to handle data submission and processing            | [New data for trainer registration form and trainee questionnaire](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/3d1ddfca2fd1740408c2b69c66f7147958f4de1f), [Questionnaire filling and sending process](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d1770830868b8c8ac600a8e1bf140b3b5d02551b)         |
| Makar Dyachenko (Frontend/Design) | Built core frontend pages including welcome, signup, login, and questionnaire pages; implemented form submission logic, token expiration handling, API integration, and improved course UI                                             | [Data processing via JSON](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/b55aa20683c8c2ffb892f5e89e557a38ad769625), [API connection](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/fdfa3598e21fc859dc4ce62ec79970baf09ce212), [Login and Register system](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/4979170c830b287a5a387f5a01d32f0e9981e2d5), [User token expire algorithm](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/2f83d2132daa326e0af6cf1cf2045a316810fb6b), [Survey imporvements](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/1f76c69568a0587ab1694945277e9304888c4ce9), [Form submit](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/c4ba8184d95efd34dfbf4ee0d1cf4e0ecbf518e0), [Improved Course Page](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/348f416c8f30109952e9792ad4ee75ae3a39b9ec)         |
| Salavat Faizullin (Backend)   | Developed backend APIs and business logic for user survey processing and training module management; added database models and ensured backend integration with frontend                                                                                   | [Backend and frontend integration](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/2118344ee2c6b8306897cd2fb82e342382a7f9c0), [Survey endpoints](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d3732ad6efbfbbc338835963db8d9155d120bad3), [Processing the user's form](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d1770830868b8c8ac600a8e1bf140b3b5d02551b), [Add training models](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/f87f7ae2d307ff55f10203d915edf8394bf94156), [Add training metadata](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/6d8f3db2a4d876809ab89d25d117f7a7b2258c89), [Fix database container](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/c7e2ab0097cdd6530fd4e64c5e4c0dd4c9a33a42)         |
| Egor Chernobrovkin (ML)  | Deployed and configured a vector database as part of the ML pipeline to enable similarity-based search functionality. Collected raw datasets and prepared training data. Completed the first phase of training | [Vector-db deploy](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/44), [Raw version of the dataset](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/ml/scripts/data/dataset.csv), [Raw dataset collection code](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/ml/scripts/prepare_dataset.ipynb), [Version of the dataset for training on TripletLoss](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/ml/scripts/data/training_data.csv), [Code for training](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/ml/scripts/train_model.ipynb)   |
| Alexandra Starikova (ML) | Developed and integrated the generation pipeline for personalized sport programs using LLM, and contributed initial dataset for training purposes | [Add generated sport programs](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/54)        |
| Ilona Dziurava (PM)      | Prepared the project report, facilitated two team meetings, coordinated task distribution, maintained the product backlog, organized and led a project demo, and structured the team’s workflow for efficient collaboration | This report :)   |
| Anisya Kochetkova (Backend)   | Authored backend documentation for defined API endpoints, and define authorization testing   | [API documentation](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/60a670e9c1f59ce7deb5fcd1a99f17909fc18cfe), [Create user_possible_values.md](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/0a49c71cce5fed213ae3f8ca0f5ac438ee989980), [Authorization tests](https://1drv.ms/w/c/64ea16d230ddc2a8/EUGtruTL7OBDkzu6iy-GvWMBxIpTIODg99z2NHmCfAO_5Q?e=3bzxYf) |

## Challenges & Solutions

One of the biggest challenges this week was making sure the frontend and backend teams worked smoothly together so that data could flow correctly through the app. Since we had to move fast, it was important to stay well-coordinated. To handle this, we made sure each team member knew exactly which part of the work they were responsible for, used mock APIs to start frontend work before the backend was fully ready, and held daily check-ins to quickly catch and fix any problems.

## Conclusions & Next Steps

By the end of Week 3, we successfully delivered the first working version of the Minimum Viable Product (MVP). This includes a fully functional end-to-end user journey, with integrated frontend and backend components, persistent data storage, and a basic authentication flow. Additionally, the ML team delivered the first model iteration, integrated via a backend API for early testing and validation.

An internal demo was conducted to showcase the current state. Feedback helped identify minor usability issues and edge cases in error handling, which are now being tracked for resolution.

### Next Steps for Week 4

- **Testing:** Add unit tests for key frontend components and backend functions. Write integration tests for API routes and aim to cover one full user flow with basic end-to-end tests. The ML team will also start validating their model with test data.

- **CI/CD Setup:** Configure a Continuous Integration (CI) pipeline to automatically run tests whenever code is pushed. If time allows, we'll also set up Continuous Deployment (CD) to automatically deploy new changes to a staging environment after merging to the main branch.

- **Deployment:** Set up a staging environment and deploy the current version of the app. If possible, we’ll also connect a custom domain name.

This week will focus on improving the reliability of the project, catching bugs early through testing, and making the deployment process smooth and automated.

**We confirm that the code in the main branch:**

In working condition.
Run via docker-compose.
