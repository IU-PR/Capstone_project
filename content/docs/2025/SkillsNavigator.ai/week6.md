---
title: "Week #6"
---

# **Week #6**

## Links

*Specify here all the necessary links to your website, application installer, final demo, etc.*

- **Deployment**: [skillsnavigator.ru](https://skillsnavigator.ru)
- **API Docs**: [GitHub](https://skillsnavigator.ru/api/swagger)
- **Design**: [Figma](https://www.figma.com/design/JjmqRt1Tr5xyc9X3vRJN5L/SkillsNavigator?node-id=0-1&t=uApr9A2j8Ij0JpfT-1)


## Final deliverables

### Project Overview 

**SkillsNavigator.ai** is a platform designed to help users build a personalized learning journey, tailored to their current skills, career goals, and budget. Whether you're aiming to become a developer or pursuing a different path, SkillsNavigator.ai recommends the most effective and affordable online courses to achieve your objectives. The platform provides step-by-step guidance, cost-aware resources, and a clear view of your progress at every stage.


## Problems Solved

**1. Too Many Courses, Not Enough Guidance**

**Problem:**
Users often struggle to choose the best courses from a vast sea of online options.

**Solution:**
SkillsNavigator.ai uses advanced vector search and AI-powered recommendations to match you with the most relevant and effective courses, eliminating the guesswork.

**2. Lack of Personalized Learning Paths**

**Problem:**
Most existing platforms rarely tailor recommendations to your unique skill level, goals, available time, or budget.

**Solution:**
SkillsNavigator.ai creates a fully personalized learning journey based on your current skills, career aspirations, time constraints, and budget—so every step is relevant and achievable.

**3. Difficulty Tracking Progress and Next Steps**

**Problem:**
It’s hard to keep track of your learning progress and plan what to do next.

**Solution:**
SkillsNavigator.ai provides a clear, interactive roadmap and real-time progress tracking, making it easy to monitor your achievements and see exactly what to learn next.


## Key Features 

### Advanced Vector Search
* **Free-form chat input**—just describe your goals or skills, and get instant recommendations.
* **Quick processing:** Recommendations are provided in real-time.
* **Course details at a glance:** View each course’s image, rating, difficulty, duration (hours), number of enrolled students, name, author, and price.
* **Direct course access:** One click to open the course in Stepik.
* **Chat history:** Keeps a record of all your chats for easy reference.
* **Multiple chat sessions:** Support for managing several learning chats at once.
* **One-click roadmap:** Instantly generate a learning roadmap from your chat.

### Сonvenient Roadmap

* **Automatic roadmap generation:** Forms a clear learning path using courses found via advanced vector search, prioritized logically by AI (LLM) based on your skill level and needs.
* **Sequential display:** All recommended courses are shown in the suggested learning order.
* **Minimalistic, clear roadmap:** Easy to follow and visually clean.
* **Rich course info on hover:** See detailed course info (image, rating, difficulty, hours, students enrolled, name, author, price) by pointing at any node.
* **Progress tracking:** Monitor your advancement directly through Stepik.
* **Easy access:** Go straight to any course from the roadmap.
* **Roadmap history:** Track and revisit previous roadmaps.
* **Multiple roadmaps:** Manage several learning journeys at the same time.

###  Stepik Integration

* **Login with Stepik:** Sign in using your Stepik account for a seamless experience.
* **Persistent history:** View your chat and roadmap history at any time.
* **Progress synchronization:** See your progress on each roadmap and course, updated in real time.



## Tech stack

- React - Frontend;
- FastAPI - Backend;
- qdrant (vector DB) - Vector Embeddings and Search;
- Deepseek - course selection;
- Docker - Deploy.
- PostgreSQL - DataBase for users, chats, roadmaps. 



## Setup instructions

#### 1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd <your-repo-directory>
```


#### 2. **Set Up Environment Variables**

Copy the example `.env` file to create your actual `.env` file, then edit as needed:

```bash
cp .env.example .env
# Open .env in your preferred editor to adjust values:
# nano .env
```



#### 3. **Build and Launch with Docker Compose**

Use the provided Docker Compose file for your local environment:

```bash
docker compose -f docker-compose.local.yml up --build
```



#### 4. **Access the Application**

* Check the terminal output for which ports the services are running on.
* Open the application in your web browser.



## Presentation draft

[Link to GitHub](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/blob/master/assets/Presentation_draft.pdf)



# Weekly commitments

## Individual contribution of each participant

| Name (Role)             | GitHub         | Email                                    | Role(s)                       | Main contributions / Notable PRs/Commits |
|-------------------------|----------------|------------------------------------------|-------------------------------|------------------------------------------|
| Lana Ermolaeva (lead)   | @oELYAo        | l.ermolaeva@innopolis.university         | Project/Product Management, ML| Report writing, Presentation draft [Link](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/blob/master/assets/Presentation_draft.pdf), Backlog [ClickUp](https://app.clickup.com/9015876757/v/o/s/90155186012)|
| Adilya Saifetdiarova    | @sayfetik      | a.saifetdiarova@innopolis.university     | Frontend, UX/UI design       | Fix bugs: make the node background white, prevent unauthorized users from navigating anywhere from the roadmap, check that chat continuation does not start from the beginning, fix loading indicator display, prohibit sending messages after the roadmap is finished, set scroll position to 0 when the page is refreshed, fix lines for disabled nodes in the roadmap, remove the "Go to Roadmap" button for unauthorized users, handle the case when no courses are found. [Commit1](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/35957b758f72b8df8be2a4c8ab7d8da774e082f7), [Commit2](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/0518bc4653fcdc8b3e562a7e92fc11d36971d7a4), [Commit3](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/54a9a3f31fadd13aea74f9f2de04f104e7a6a83c), [Commit4](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/237dadd88faed5d5f4f18ba3ec71b08a01c8d6b0); Add animations [Commit5](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/e26f518fb8960d122fc897fa35370ce8e5bfbcb3); Add cost & Price related questions [Commit6](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/f632e540b548479d990a618e9332bf425ada6d13)|
| Ivan Ershov             | @spiritonchiс  | i.ershov@innopolis.university            | ML                            | Request speed optimisation & bug fixes [Commit1](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/a9be2c5e08aaf2998336da8f96cfc13069735028); Change course selection logic to roadmap selection logic [Commit2](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/038bf8501534b0bfadeaafbc563c08b5f0bedd28); Add time & cost constrains to the search [Commit3](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/da2d24be4dd59214ccb966de51c779402fc85c66); Delete redundant code [Commit4](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/7cdb21f3b7e187029eca0165286aabcd8232ed36) |
| Bulat Gazizov           | @BulatGazizov0 | b.gazizov@innopolis.university           | Backend, DevOps               | Fix chat naming bug [Commit1](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/9bf6ba68f20fbd24972877cd446e92c7527f3203); Add backend for cost and time filterng, display pregress on the roadmap [Commit2](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/02e3252a4575610a342221c3529cee225ab36b7e)| 
| Arthur Popov            | @ee_boooy      | ar.popov@innopolis.university            | Backend, MLOps       | As part of optimizing the CI/CD process, a self-hosted GitHub Runner was added to a dedicated host. This significantly improved pipeline execution speed compared to cloud-hosted runners. However, considerable time was spent resolving port and container conflicts, since the Runner and the staging environment are located on the same server. [Commit1](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/e76d7f3b101d4e0a0c9a0e53cbedf5dc5dc38447) The pipeline logic was also updated [Commit2](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/9e46c7674a0a05789cfd3615d79f6020fd1a8c9a). Testing: CI is triggered on pushes and pull requests to the master, develop, and devops branches; at this stage, the application is built and tested, but Docker images are not pushed to the registry. Deployment: On tag push, CI builds the Docker images and pushes them to the Docker Registry. This triggers CD to the staging environment; for production releases, the tagged image is pushed and deployed to the production server. Pipeline was multiple time tested on different cases|

## Plan for Next Week

Check if the service handles the load, prepare the presentation design, successfully defend the project.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose (or another alternative described in the `README.md`).
