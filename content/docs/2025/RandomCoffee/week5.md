---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

Our team has conducted 7 usability testing sessions with potential users. All participants are IT-related specialists of different age. Respondents reviews can be found <u>[here](https://docs.google.com/spreadsheets/d/16tiuKEnM-wr9mrbDnG0Km2l8QtRDZ-N1kkdeXii9d9I/edit?usp=sharing)</u>

### Analyze

**Visual Design & Usability**
- The UI is clean, modern, and visually guided with friendly illustrations.
- Large buttons and generous use of white space are appreciated.
- Users suggest animating transitions to make the process feel smoother.
- Home page is visually friendly, but users would like to see more information (e.g., a short bio snippet or tags) when viewing profiles.

**Navigation & Flow**
- The app is intuitive and easy to follow.
- The format feels casual and non-intimidating, with strong CTAs (e.g., “Open chat”).
- **Critical bug:** The “disabled” button still allows users to proceed to the next step.
- Real-time validation and feedback are missing when fields are incomplete.
- Users would like a “Request another match” button if their match is unavailable.

**Tags & Suggestions**
- Tag suggestions are helpful, but users want clearer guidance on their purpose (only for profile or for matching too).
- Synonyms or AI-based tag suggestions would improve usability.
- Allowing users to import tags from LinkedIn or job roles could reduce friction.

**Matching page**
- Users want more context about matches (e.g., common interests, matching tags).
- An indicator for match status (e.g., whether both users have opened the chat) would be helpful.
- Users would like to rate matches or have more options after being matched.

**Matchmaking algorithm**

Overall Satisfaction:
- The majority of users rated their matches highly, with several perfect scores (10/10) and most ratings above 7/10.
- Users frequently commented on shared interests, complementary skills, and the potential for meaningful conversations, indicating that the algorithm is generally successful in pairing users with relevant partners.

Strengths:
- **High Relevance:** Matches often shared professional interests or technical backgrounds (e.g., both working with data, Java, PostgreSQL).
- **Positive Surprises:** Some users found their matches inspiring or saw opportunities to learn from each other, such as exploring new domains.
- **Reflection and Diversity:** Users appreciated being matched with someone on a similar journey or with a different but complementary focus (e.g., frontend vs. backend).

Areas for Improvement:
- **Domain Alignment:** A few matches, while positive, noted only partial overlap in research or technical domains (e.g., data analytics vs. research domain), resulting in slightly lower ratings (6–8/10).

Average Match Rating: 8.3  


**Performance & Feedback**
- The app is fast and avoids unnecessary questions.
- Loading spinners or indicators are missing, making it unclear if actions are processing.
- Users want notifications when a match is found.

**Other Suggestions**
- The survey question about contacting a match feels too binary; more nuanced options are suggested.

---

**Overall:**  
The app is well-received for its design and simplicity.  
**Key areas for improvement:** bug fixes, better feedback/validation, richer match context, and enhanced tag handling.

We have divided the suggestions into several categories:

| Category                            | Suggestions                          |
|-------------------------------------|--------------------------------------|
| **Bugs**                            | - "Disabled" button still allows users to proceed to the next step **(Urgent)**<br>|
| **Already in Development**          | - Bio and tags of matched partner **(High)**<br> -Synonyms and AI-based tag suggestions **(Medium)**<br>- Notifications when a match is found **(Medium)**|
| **New Features**                    | - Clearer guidance on tag purpose **(Low)** |
| **Not Applicable**                  |- Import tags from LinkedIn (we position the product as only russian app)<br>- More nuanced options in "Have you contacted ...?" not just yes/no (we do not want to overcomplicate our app) |
| **Possible features in the future** | - Animate transitions between steps **(Low)** <br>  - “Request another match” button if match is unavailable **(Medium)** <br>- Indicator for match status (e.g., both users opened chat)<br>- Option to rate matches **(Very low)**

## Iteration & Refinement

### Implemented features based on feedback

- Fixed the found bug.
- Added bio and tags of the matched partner
- Added notifications when match is found
- Added more eaplanatory text about tags

### Performance & Stability

### 1. Technical Performance Metrics

a) Backend/API Performance

- **Response Time**
  - **Current Status:** 200–500ms.
  - **No need to improve**  

- **Matchmaking Algorithm Execution Time**
  - **Current Status:** 50 users processed in 500ms.
  - **No need to improve as matchmaking algorithm performs once a week and does not have to be fast**

- **System Uptime/Availability**
  - **How to Improve:**  
    - Set up health checks and alerts.
    - Use redundancy and failover strategies.

b) Frontend Performance

- **Page Load Time**
    - **Current Status:** slow GIF images loading
  - **How to Improve:**  
    - Optimize asset sizes.
    - Lazy-load non-critical resources.

---

### 2. Product/User-Centric Metrics

a) User Engagement & Satisfaction

- **Match Acceptance Rate**
  - **Definition:** Percentage of users who contact their match after being paired.
  - **How to Measure:** Track responses to the “Have you contacted your match?” questionnaire.
  - **How to Improve:**  
    - Provide more context about matches.
    - Add features like “Request another match”.

- **Average Match Rating**
  - **Definition:** Average user rating of their match (e.g., 8.3/10 as reported).
  - **How to Measure:** Collect ratings after each match via survey.
  - **How to Improve:**  
    - Refine matchmaking algorithm (e.g., better tag handling, consider user goals).
    - Allow users to specify preferences more granularly.

- **User Retention Rate**
  - **Definition:** Percentage of users who participate in multiple matchmaking cycles.
  - **How to Measure:** Track user participation over time.
  - **How to Improve:**  
    - Personalize reminders.
    - Add gamification.

b) Matchmaking Quality

- **Unmatched User Rate**
  - **Definition:** Percentage of users who do not get matched in a cycle.
  - **How to Measure:** Count users left unmatched after each run.
  - **How to Improve:**  
    - Adjust algorithm to handle odd numbers (e.g., allow groups of 3).
    - Encourage more users to participate.

---


### Documentation

**1. Project-Level Documentation**  
`README.md`  
- **Purpose:**  
  - Provides a high-level overview of the project, its goals, and main features.
  - Offers step-by-step instructions for remote and local deployment.
  - Guides users on how to open and test the Telegram Mini App, including platform-specific instructions.
- **Why:**  
  - To help new users and contributors quickly get started with the project.
  - To document essential setup and deployment procedures.

---

**2. Service-Specific Configuration and Documentation**
- **Location:**  
  - Each backend service (`API-gateway`, `bot-service`, `profile-service`, `ml/endpoint`) contains configuration files such as:  
    `application.yaml`, `application-local.yaml`, `ml.yaml`
- **Purpose:**  
  - Document environment-specific settings and service behavior.
  - Provide service identification and logging information.
- **Why:**  
  - To ensure each microservice can be configured, deployed, and debugged independently.

---

**3. API Specifications**
- **Files:**  
  - `backend/API-gateway/src/main/resources/gateway-api-spec.yaml`
  - `backend/profile-service/src/main/resources/api.yaml`
  - `mini-app/gateway-openapi.yaml`
- **Purpose:**  
  - Define the structure, endpoints, and expected behavior of APIs.
  - Serve as a contract between frontend and backend, and between microservices.
- **Why:**  
  - To enable automated code generation, validation, and integration.
  - To provide clear, machine-readable documentation for developers.

---

**4. Machine Learning Documentation**

- **Location:**  
  - `ml/` directory, including:
    - Jupyter notebooks (`.ipynb`)
    - Python scripts
    - Data files and configuration YAMLs
- **Purpose:**  
  - Document data preparation, model training, and experimentation.
  - Provide configuration for ML services and endpoints.
- **Why:**  
  - To ensure reproducibility of ML experiments.
  - To clarify the ML pipeline for future development and maintenance.

---

**5. Code Comments, Javadocs and Structure**

- **Location:**  
  - Throughout the codebase (Java, Python, etc.)
- **Purpose:**  
  - Provide inline documentation for functions, classes, and complex logic.
- **Why:**  
  - To aid maintainability and knowledge transfer among developers.

---

**Summary**

Each type of documentation in this project is designed to make the system easier to use, develop, and extend by different audiences:
- **Users:** Quick start and usage instructions.
- **Developers:** Deployment, configuration, and code-level guidance.
- **Integrators:** API contracts and specifications.
- **Data Scientists:** ML pipeline and experiment reproducibility.

---

### Matchmaking refinement

- This week we have implemented the functionality for user to register for the matchmaking. User does not have to get a partner every week.
- Also we have added the ability to choose goal for the meeting: "Tech communication", "Non-tech communication" or "Random". This allows us to match users with similar aims.

# Weekly commitments

## Individual contribution of each participant

1. **Anastasia Mitiutneva**:  
Reviewed each pull request  
Identifed future plans for each team.  
2. **Maksim Al Dandan**: implemented time configuration (date and time of matchmaking and ) (notiications in the bot when match was found and with reminder to register in the next matchmaking).  
[Pull Request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/45)  
Implemented Scheduler that automatically starts matchmaking and sends messages based on time configuration. Added info about user registration in the following matchmaking and user goal for the matchmaking.    
[Pull Request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/47)  
[Pull Request 3](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/48)  
3. **Aleksandr Andreev**:  
Improved CI/CD to build images only if they are changed and added environment variables for API endpoints.  
[Pull Request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/43)  
Implemented functioning registration for the matchmaking with ability to choose a goal for matchmaking (Tech, Non-tech, Random communication). Implemented "View more" page about the partner. Impremented "Edit page". Fixed non-disabled button bug.  
[Pull Request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/53)  
<u>[App screenshots](https://www.tldraw.com/f/37VWdlc4Mts0bzYcR4qxh?d=v-17472.9970.14449.9031.kNT5Vq7od4SeH8C180OHN)</u>
4. **Ivan Ilyichev**:  
Synchronized the backend API, configuration, and algorithm implementation after machine learning model improvements.  
[Pull Request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/49)  
Added tags validation logic and endpoint for it  
[Pull Request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/51)  
5. **Rail Sabirov**:
Implemented matchmaking based on user's goal (Tech, Non-tech, Random communication), change matchmaking model based on users amount  
[Pull Request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/46)  
[Pull Request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/50)


## Plan for Next Week

### Each team:  
 - Testing and critical bug fixes  


### Product manager
- Conduct final testing  
- Update `README.md`
- Start preparing the presentation slides

## Confirmation of the code's operability

We confirm that the code in the main branch:  
✅ In working condition.  
✅ Run via docker-compose (see `README.md`).  