---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

We conducted five live user testing sessions with 2nd-year students experienced with Stepik and roadmap creation. All students are not our team members.  Daria and Stepan had previously built study roadmaps using ChatGPT, while Kirill and Leonid had done it manually. During the sessions, we observed as they used the site from the starting page, noting their real-time feedback. We gave time time to discover functionality by themselves as well as asked complete tasks to cover all available userflows. All users quickly understood the platform’s purpose and features, but shared suggestions and highlighted usability issues. All users mentioned the convenience and time efficiency of using the service comparing with their previous habbits.

| User                         |  Feedback                                                                                                                                                                                                                                        | Requirements                                                                                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Daria**        | - Chat restarts from beginning after reload<br>- Button to jump from the chat to roadmap would be intuitive     | - Chat and questions persist after reload<br> - Resume chat from last point<br>- "Go to roadmap" button in chat<br>                         |
| **Azalia**   | - Popular courses take long to load, graphics load in chunks<br> | - Fast loading of courses/graphics<br>       |
| **Stepan**  | - Roadmap line in graph mixed up coloring <br>- I want to see information about any course in the roadmap  <br>- I want to clearly see whats available and what is not and what to do to gain access| - Clear, correct roadmap graph lines<br>- Display history-related features as blocked and offer Stepik sign-in |
| **Kirill**  | - It mixes up courses teaching different languages  | - Enhance search accuracy           |
| **Leonid**   | - Roadmap shouldn’t double block, just unavailable elements <br>- I want to see list of all dialogues to keep several learning paths <br>              | - No double blocking on roadmap<br>- Save all chats and roadmaps <br>                                                      |

---

### Analyze

| Priority | Requirement                                             | Realisation / Solution                                                            |
| -------- | ------------------------------------------------------- | --------------------------------------------------------------------------------- |
| High     | Chat and questions persist after reload                 | Implement storage to save chat state and reload from last point     |
| High     | Clear, correct roadmap graph lines                      | Redesign graph visualization; fix color and logic issues                          |
| High     | Display unavailable/blocked features clearly in roadmap | Mark locked features visually and explain required actions for access             |
| High   | Save all chats and roadmaps                             | Store user chat and roadmap data for retrieval across sessions                    |
| Medium   | No double blocking on roadmap elements                  | Update roadmap logic to block elements only once and show others as unavailable   |
| Medium   | Display list of all dialogues/learning paths            | Add a section to view/manage all ongoing chats and learning paths                 |
| Medium  | Enhance search accuracy (different languages)           | LMM selection of the courses instead of treashhold                    |
| Low   | "Go to roadmap" button in chat                          | Add a prominent button in chat UI linking to roadmap                              |
| Low     | Fast loading of courses/graphics                        | Optimize background images, popular courses downloading|



## Iteration & Refinement

### Implemented features based on feedback

- Chat and answers persist after reload      
- Display roadmap graph lines properly
- Make roadmap accessibe without login in            
- Save all chats and roadmaps
- Display list of all dialogues/learning paths
- Display unavailable/blocked features clearly in roadmap
- Compress background image


### Performance & Stability

Metrics developed for further service performance evaluation.

#### 1. **API Response Time (95th Percentile)**

* Measures how fast backend endpoints respond for 95% of requests.
* **Formula:**
  Response time value below which 95% of requests complete.
* **Target:** `<500ms`



#### 2. **Course Search Latency**

* Time from user search input to course results display (end-to-end).
* **Formula:**
  `Total search response time`
* **Target:** `<1s`



#### 3. **Database Query Time**

* Average execution time for key SQL queries.
* **Formula:**
  `Σ(query_times) / total_queries`
* **Target:** `<100ms`



#### 4. **Frontend Largest Contentful Paint (LCP)**

* Time for main content to become visible to the user.
* **Formula:**
  LCP measurement as reported by browser
* **Target:** `<2.5s`



#### 5. **Overall System Availability**

* Percentage of time the application is fully operational.
* **Formula:**
  `(total_requests - failed_requests) / total_requests × 100%`
* **Target:** `>99.5%`



### Documentation


#### **What exists and why:**

- **User Documentation:**
  *README.md* (main, frontend, backend) for setup, onboarding, and API usage.
- **API Documentation:**
  Manual API docs in *backend/README.md*, FastAPI auto-generated docs, and backend docstrings to define API contracts and usage.
- **Configuration Docs:**
  Inline comments in config files (Docker, envs, package.json), and setup details to aid in environment configuration.
- **Design Documentation:**
  Visual assets (Figma, PDFs) and design flow documentation to track and communicate UI/UX changes.
- **Operational Logs:**
  Log files and logging setup for debugging, monitoring, and understanding system behavior.

#### **What can be added:**

- **Architecture Documentation:**
  System diagrams, data flow, and tech stack rationale are essential for onboarding and system understanding.
- **Developer & Contributing Docs:**
  Workflow guides, contributing standards, database schema, and ML model explanations to support collaboration and consistency.
- **Deployment Documentation:**
  Production deployment guides, environment configs, monitoring setup for backup/recovery.
- **Testing Documentation:**
  No formal docs on testing strategy, test data, performance testing, or CI setup— critical for quality assurance.
- **User Guides:**
  No user manual, FAQ, or feature documentation for end users.
- **Operational Docs:**
  Troubleshooting, monitoring, and incident response procedures.
- **Maintenance Documentation:**
  Lacking guides for dependency updates, data migration, and scaling.


### ML Model Refinement

To improve our ML model, Ivan Ershov tried different models, ways to compare results, and various thresholds. However, using thresholds did not give good enough results. We also saw that courses need to be ordered in a specific, meaningful way, which is hard to do with just semantic search. So, we decided to use an LLM to help with course selection and ordering. In the future, we may replace semantic search with BM25 or another method that can rank and filter courses better.

# Weekly commitments

## Individual contribution of each participant

| Name (Role)             | GitHub         | Email                                    | Role(s)                       | Main contributions / Notable PRs/Commits |
|-------------------------|----------------|------------------------------------------|-------------------------------|------------------------------------------|
| Lana Ermolaeva (lead)   | @oELYAo        | l.ermolaeva@innopolis.university         | Project/Product Management, ML| Report writing, test sessions conduction, feature prioritization [ClickUp](https://app.clickup.com/9015876757/v/o/s/90155186012), performance metrics |
| Adilya Saifetdiarova    | @sayfetik      | a.saifetdiarova@innopolis.university     | Frontend, UX/UI design       | Conducted user tests. Integrated roadmaps and chats with the backend [Commit1](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/d983fbee65d16342c33532272ea7a35fcc848d24), visual updates, and enhanced navigation. [Commit2](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/86ddd7c22a35bb6ec4cba57c0faeb10e76455b49); Implemented various UI improvements and minor features, including chat and sidebar fixes [Commit1](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/ee50644f58f5562d96630e05bcfb0d7661c2d720) [Commit2](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/8d1a85742b7d6f325963ca49a03d5ff590cb3c9a), [Commit3](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/051da877cfe730e7efea2adf03bb0520b9b6a665); Improved authentication/authorization and optimized performance by compressing images [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/68ab9f58e2877da15352ea02a27292bdebd35449).|
| Ivan Ershov             | @spiritonchiс  | i.ershov@innopolis.university            | ML                            | Code fixes (adding required libraries, removing unnecessary or unsafe code, etc.) [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/984b9e5c39a1d6b80c189bc082f80f12802517be); Updates to the DeepSeek service: it now filters the courses retrieved by search [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/a9d5627465255d6b04c806c30719089afcce6ffb).|
| Bulat Gazizov           | @BulatGazizov0 | b.gazizov@innopolis.university           | Backend, DevOps               | Revised the authorization process. Now, after a user logs in via Stepik, a JWT token is generated and stored in the user's cookies. This token is then used to identify the user within the system, connect postgresql [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/004aa52aba7ee014c7ee7b7947b4c9baf1021701); Added models (tables) for User, Course, Dialog, Message, and Roadmap to the database/backend. Implemented the following endpoints: сreating a dialog, saving messages to a dialog, retrieving the list of all dialogs, retrieving the list of all roadmaps [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/c5cd86efec574a17ac3d0ed91a01282c4fe8c140). 
| Arthur Popov            | @ee_boooy      | ar.popov@innopolis.university            | Backend, MLOps       | A Docker Registry (v2) was deployed on a remote server with HTTPS via nginx and user/password authentication; certificates were issued by Let’s Encrypt. CI workflows build backend and frontend images, tag them with the GitHub SHA, and push to the Registry. Staging and production servers use docker-compose files referencing these images, pulling the correct tag after authenticating to the Registry. [CI/CD Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/c036d244a4bdde25638c4ee842570e5210c7446e), [Tests Update Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/f8e5491fc60ff63d97e98a4b444dcb8650fd1e1c)|



## Plan for Next Week

- Synchronize course progress from Stepik
- Set roadmap constraints (time/budget)
- Organize courses meaningfully in the roadmap
- Test and fix bugs
- Refactor the code
- Update the documentation

### Service available at [https://skillsnavigator.ru](https://skillsnavigator.ru)
### Backlog available at [ClickUp](https://app.clickup.com/9015876757/v/o/s/90155186012)

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose (or another alternative described in the `README.md`).
