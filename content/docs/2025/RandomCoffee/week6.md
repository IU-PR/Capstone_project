---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**: <u>[@random_coffee_iu_bot](https://t.me/random_coffee_iu_bot)</u>
- **API Docs**: <u>[Backend](https://github.com/IU-Capstone-Project-2025/RandomCoffee/blob/main/backend/profile-service/src/main/resources/api.yaml)</u>, <u>[ML](https://github.com/IU-Capstone-Project-2025/RandomCoffee/blob/main/ml/endpoint/ml.yaml)</u>
- **Demo**: <u>[Video](https://drive.google.com/file/d/1JB784yfOVi1Ejvne2rhK1UuD_wnVnfaz/view?usp=sharing)</u>

## Final deliverables

### Project overview
**Project Description**  
RandomCoffee is a matchmaking mini-app designed to connect IT professionals for meaningful conversations and networking. The app automates the process of pairing users based on their interests, professional backgrounds, and meeting goals, making it easier for people to expand their professional network and share knowledge.  

**Problem Solved**  
*Networking Barriers*: Many professionals struggle to find relevant contacts for knowledge sharing, mentorship, or collaboration, especially in remote or distributed environments.  
*Manual Pairing Inefficiency*: Traditional networking relies on manual introductions or random chance, which can be inefficient and intimidating.  
*Lack of Context in Matches*: Existing solutions often fail to provide enough context about matches, leading to less meaningful interactions.  

### Key Implemented Features  
**User Registration & Editing**
- Users can register in the app with pre-filled name and surname.
- Users are filling the bio and sutable tags from our tags database

**User Registration for Matchmaking & Preferences**  
- Each week users can register for matchmaking cycles and choose their preferred goal for the meeting.
- Participation is flexible — users are not required to join every week.

**Automated Matchmaking**  
- Users are automatically paired based on shared interests (bio), professional tags, and chosen meeting goals (Tech, Non-tech, or Random communication).  
- The matchmaking algorithm is refined to maximize relevance and user satisfaction.  

**Profile Enrichment**  
- Each user profile includes a bio and tags describing their interests and expertise.
- Users see their match’s bio and tags for better context before connecting.

**Notifications**  
- Users receive notifications when a match is found and reminders to register for upcoming matchmaking cycles in the bot.

### Tech stack
- **Frontend:** Next.js, TypeScript, React, Tailwind CSS, Telegram Mini Apps SDK, Telegram UI, Zustand
- **Backend:** Java 21, Spring Boot, Spring Cloud Gateway, PostgreSQL, OpenAPI
- **Bot:** Java, Spring Boot, Telegram Bots API
- **ML Service:** Python, FastAPI, scikit-learn, sentence-transformers, PyTorch, NLTK, transformers
- **Containerization/Orchestration:** Docker, Docker Compose

### Setup instructions

**Local Deploy**

1. Clone the repository
2. Enter the project root folder
3. Add a `.env` file to the root folder (see `.env.example`)
4. Run:
   ```bash
   docker compose -f compose-dev.yaml up -d --build
   ```

**Remote Deploy**

1. Download `compose.yaml`
2. Add `.env` to the same folder (see `.env.example`)
3. Run:
   ```bash
   docker compose up -d
   ```


**Opening the Mini App**

To open the mini app locally from your Telegram app, you need to log in to the Telegram Test Environment, because production clients require an SSL certificate for mini apps.

**Guide:**
- Log in to the Telegram Test Environment. For example:
    - **iOS/macOS:** Tap Settings 10 times → Tap on "Accounts" → "Login to another account" → "Test"
    - **Windows:** Go to Settings → Right click with Shift+Alt on Add Account → Select Test Server
- If you want to open the mini app from your computer (with the Docker container running):
    - Open @random_coffee_test_bot
    - Tap on "Open App" button in the bot's profile
- If you want to open the mini app from mobile (with the Docker container running):
    - Open @BotFather and create a new bot
    - Get your computer's IP address in the local network
    - Enter bot edit mode, tap on "Bot Settings" → "Configure Mini App" → "Enable Mini App" and paste your computer's IP address in the format `http://<IP_ADDRESS>:3000`
    - Open your bot and tap on "Open App" button in the bot's profile

## Presentation draft
<u>[Link](https://www.canva.com/design/DAGtUkbYYOs/C7WOicmPWUrYRJ5P7qCMpQ/edit?utm_content=DAGtUkbYYOs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)</u>  
VPN is required to open the link, in case of troubles contact team lead @Mituttta

# Weekly commitments

## Individual contribution of each participant

1. **Anastasia Mitiutneva**:  
- Conducted final testing considering all corner cases of the app  
- Upadated `README.md`  
[Commit](https://github.com/IU-Capstone-Project-2025/RandomCoffee/commit/e82a5ed849f117fea969d84d1e14fe842bb5bde9)  
- Added cosmetics to bot messages  
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/62)
- Started preparing presentation slides (see section presentation draft)
2. **Maksim Al Dandan**:  
- Conducted final testing considering all corner cases of the app
- Fixed bugs connected to "update" and "create" requests after final testing  
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/56)
- Added the ability to change matchmaking state using endpoint  
[Commit](https://github.com/IU-Capstone-Project-2025/RandomCoffee/commit/c3062c9f0cb010e3901285f4dcd1df9336d9efcb)
3. **Aleksandr Andreev**:  
- Conducted final testing considering all corner cases of the app
- Fixed bugs connected to time configuration  
[Pull Request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/57)
- Frontend matchmaking state relies on the variable obtained from backend  
[Commit](https://github.com/IU-Capstone-Project-2025/RandomCoffee/commit/59c0ac2809f6ddf8c935f32dbc92a7a4ee47ad19)
- Real-time page reload  
[Commit 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/commit/94eacb264e97f33fc1e7a9498e31df4474609f6b)  
[Commit 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/commit/288028275c3f1731591145a88d0f3824fd09a47d)
- Added partner goal info to the match page  
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/64)
4. **Ivan Ilyichev**:  
- Conducted final testing considering all corner cases of the app
- Updated ML API documentation and added comments to the code
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/63)
5. **Rail Sabirov**:  
- Conducted final testing considering all corner cases of the app
- Added `README.md` to the ML project  
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/61)  
## Plan for Next Week

- Final Rehearsal: One last run-through of the presentation and demo.
- Technical Check: Ensure the demo environment and any required software are working perfectly.
- Deliver Final Presentation:
    - Present your project clearly and confidently.
    - Conduct a smooth live demo of the key functionalities.
    - Be prepared for a Q&A session.


## Confirmation of the code's operability

We confirm that the code in the main branch:  
✅ In working condition.  
✅ Run via docker-compose (see `README.md`).
