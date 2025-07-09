# Testing, CI/CD & Deployment Setup — Week #4

---

## **Testing and QA**

We conducted basic testing to verify the functionality of API endpoints (i.e., checking whether they respond and work as expected).

 But now we have less coverage by tests. In the future we will improve it by creating more complex tests and improoving of the code quality.

### Evidence of Test Execution

![testing res](https://github.com/setterwars/Capstone-project-2025/blob/main/resukt%20of%20testing.png?raw=true)

---

## **CI/CD Setup**

### Link to CI/CD Configuration Files
[CI/CD configs](https://github.com/IU-Capstone-Project-2025/Ego_AI/blob/main/.github/workflows/ci-cd.yml)

![CiCD1](https://github.com/setterwars/Capstone-project-2025/blob/main/CiCdWeek41.png?raw=true)

![CiCD2](https://github.com/setterwars/Capstone-project-2025/blob/main/CIcdweek42.png?raw=true)

![CiCD3](https://github.com/setterwars/Capstone-project-2025/blob/main/CiCdWeek43.png?raw=true)

![CiCd4](https://github.com/setterwars/Capstone-project-2025/blob/main/CiCdWeek45.png?raw=true)


As you can see from spript to keep private data like API keys or databases passwords we use github secrets.

---

## **Deployment**

### Staging
For staging server deployment, we use an auto-deployment script integrated into our CI/CD pipeline.  
All `.env` files are manually configured on the server by the DevOps engineer or team lead.

For running our web site we use docker files and docker compose what run all this docker files.


### Production
We deploy a new version of the product weekly to the production server.  
The current deployment is available at:

- 🌐 [http://egoai.duckdns.org:3000](http://egoai.duckdns.org:3000)

Also you can acsess to the API documentation using this link:

- 🌐 [http://egoai.duckdns.org:8000/docs](http://egoai.duckdns.org:8000/docs)

We use a server located in Germany due to regional limitations of the AI API key.  
The domain is configured using [DuckDNS](https://www.duckdns.org/).

---

## **Vibe Check**

The team is staying motivated and productive. Everyone is focused on their tasks, and communication has been smooth throughout the week. We faced some minor technical challenges with the MongoDB setup and CI/CD pipeline, but they were resolved quickly thanks to good collaboration. Progress feels steady, and we're gaining momentum as more features come together. There’s a clear sense of direction, and the team is aligned on our short-term goals. Overall, the vibe is positive and focused.

---

## **Weekly Commitments**

### What Was Done This Week?

- **MongoDB Integration**:  
  - Set up a MongoDB database to store AI chat history.
  - Created API endpoints to:
    - Retrieve chat history
    - Add new messages
    - Delete chat history

- **Geo Recommendations Page**:  
  - Initial version of the Geo Recommendations frontend page created.
  - Currently a static template; backend API integration is planned for next week.

![Geo Recommendations](https://github.com/setterwars/Capstone-project-2025/blob/main/geo-recomendations.png?raw=true)

- **CI/CD Improvements**:
  - Backend endpoint tests added.
  - Autodeployment script updated and fixed.

- **backend endpoints**

  - Created  endpoints for gettinf JSON-array of current user interation history, and will be created endpoints for weather and geolocation recomendations

- **AI rescheduling recomendation page**

  - In this week will be created AI rescheduling page but now it does not integrated to frontend pages.

  ![Recomendations page](https://github.com/setterwars/Capstone-project-2025/blob/main/Recomendations%20page.jpg?raw=true)
---

## **Individual Contributions**

| Team Member          | Contribution                                       | Links        |
|----------------------|----------------------------------------------------|--------------|
| **Dmitriy Ryazanov** | Endpoints for weather and geolocations recomendations                               | [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/pull/82) |
| **Diana Tsoi**       | Create Recomendations frontend page(now not integrated to main pages structure)                      | [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/b575f1525fb67ae2abb37fa3a04893802231b88b) |
| **Stepan Sarantsev** | endpoint getting JSON-array of current user interaction history                                | [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/pull/83/commits/4c118b8fc17fcf09992eba52e4c89f567fa44f7d) |
| **Andrey Zhdanov**   | Created API endpoints for AI rescheduling          | [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/10b6d7d04cdf286adfa063b715ab5ed4cc452bdb)|
| **Artyom Lapin**     | Wrote CI/CD tests, edited autodeployment script    | [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/eb46a893ce883803d2a13cc1ac7bf961f3aaf749) [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/96a469dad0f6868ec7ddb41ae712241600d02bb9) |
| **Mikhail Sofin**    | Developed Geo Recommendations frontend page        | [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/a758c329edf686dc71d8746d0d041674ad2d593e)|
| **Salavat Zaynulin** | Set up MongoDB, developed API for chat history ops, write report week 4 | [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/bcd42eb98e5bfba67114684a8923a543d8f1e70e), [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/b2f48dd65687c7e7d5fe87158548a49e70ed7a02), [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/a1b4a962fa2d32ee28cc452a659cd9ba8af88fe8)|

---

## **Plan for Next Week**

- Complete backend integration for Geo Recommendations  
- Complete backend integration for AI rescheduling recomendations 
- Improve AI chat model setup
- Connect voice to task function in AI chat menu

---

## Confirmation of Code Operability

We confirm that the code in the `main` branch:

- Is fully operational  
- Runs successfully via `docker-compose`

---
