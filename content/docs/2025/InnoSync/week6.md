---
title: "Week #6"
---

# **Week #6**

### Project name: **InnoSync**

**Code repository**: https://github.com/IU-Capstone-Project-2025/InnoSync

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| (Lead) Ahmed Baha Eddine Alimi     | @Allimi3 | a.alimi@innopolis.university | [Management/ProductDesign] | Team Management, Frontend & Design Supervision|
| Yusuf Abudghafforzoda| @abdugafforzoda | y.abudghafforzoda@innopolis.university | [Backend] | Backend Integration, Database Design and Conception |
| Egor Lazutkin            | @Johnn_u | e.lazutkin@innopolis.university | [CustDev] | Customer Development & Customer Relation |
| Anvar Gilmiev            | @glmvai | a.gilmiev@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Asgat Keruly            | @east511 | a.keruly@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Aibek Bakirov | @bakirov817 | a.bakirov@innopolis.university | [DevOps] | Infrastructure Automation, CI/CD Setup, Deployment |
| Gurbanberdi Gulladyyev | @gurbangg | g.gulladyyev@innopolis.university | [ML] | ML Model Research & Development for QuickSyncing |


---

## 🔗 Useful Links

- **🌐 Deployment**: [innosync.duckdns.org](https://innosync.duckdns.org/)
- **📄 API Documentation**: [API Docs](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/assets/API_documentation.md)
- **🎨 Design (Desktop/Mobile)**: [High-Fi Figma](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&p=f&t=rTl11YLSam4kCmHW-0)
- **📹 Demo Videos**: [Google Drive](https://drive.google.com/drive/folders/1VZAhBosnuWQwqZfdrPHZ1adBGzNMDaEO?usp=sharing)
- **📱 Mobile App UX Research**: [Low-Fidelity Mobile Design](https://www.figma.com/design/islrijonPzZEUrBi9NgV94/UX-UI-Mid?node-id=47-31994&t=bATNSWtlbjcDZmov-1)
- **📊 Presentation Draft**: [Google Slides](https://docs.google.com/presentation/d/1BywG0vKwBAYrr6pOMzMjQu8Lwm-46xev3xxxsQ51wG4/edit?usp=sharing)

---

# ✅ Final Deliverables

## 🧩 Project Overview

**InnoSync** is a smart collaboration and talent-matching platform built for the Innopolis community. It simplifies the process of finding projects and talents, team formation, and collaboration by solving the following problems:

- Fragmented job/talent search across multiple platforms.
- Inefficient communication through various tools.
- Time-consuming process of assembling effective teams in academic or innovative environments.

---

## 🚀 Key Features

- 📝 **User Authentication**: Sign-up, Login, and Logout.
- 💼 **Project Creation**: Launch projects with details (type, size, description, etc.).
- 📥 **Apply to Projects**: Users can apply to join projects.
- 📩 **Invite Talents**: Project leads can send invitations to talents.
- 👤 **Profile Management**: Update positions and technologies.
- 📃 **Project & Talent Directory**: View all projects/talents with filtering capabilities.
- 🤖 **QuickSync Matching (AI-powered)**: A machine learning module that recommends the most suitable talents for a project based on skill similarity, project needs, and user preferences. This speeds up team formation by offering intelligent candidate suggestions to project leads.

---

## 🛠 Tech Stack

### **Frontend**
- React
- Next.js
- TypeScript
- Figma (for design)

### **Backend**
- Java (Spring Boot)
- PostgreSQL

### **DevOps**
- Docker
- Nginx
- GitHub Actions
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Prometheus + Grafana
- Node Exporter + Alertmanager

### **Machine Learning**
- Python
- scikit-learn
- PyTorch
- HuggingFace

---


# 🧪 Setup Instructions

To run the project locally, follow the steps below:

### 1️⃣ Clone the Repository
#### Option A: HTTPS
```bash
git clone https://github.com/IU-Capstone-Project-2025/InnoSync.git
```
#### Option B: SSH
```bash
git clone git@github.com:IU-Capstone-Project-2025/InnoSync.git
```

### 2️⃣ Navigate to the Project Directory
```bash
cd InnoSync
```

### 3️⃣ Configure Environment
Create `.env` files in:
- `backend`
- `frontend/innosync`

*For credentials, contact us via Telegram: `@abdugafforzoda`*

### 4️⃣ Start the Project with Docker
Return to the root directory and run:
```bash
docker-compose up --build
```

### 5️⃣ Access the Application
Visit: [http://localhost:3000/](http://localhost:3000/)

---

# 🤖 Machine Learning Improvements

- Resolved integration issues between the ML model and backend by aligning data formats and communication protocols.
- Implemented JWT authentication in the ML service to secure API requests between backend and ML components.
- Started developing an enhanced ML model aimed at improving the accuracy and efficiency of the QuickSync team matching feature.
- ML research and testing continue with real user data to validate and optimize model performance.

---

# 🛡 DevOps Improvements

## 📊 Monitoring & Logging

To ensure robust observability and maintainability of the deployed services, we have integrated the following tools:

- **ELK Stack (Elasticsearch, Logstash, Kibana)**  
  Used for centralized logging. Logs from containers and services are collected and shipped to Logstash, indexed in Elasticsearch, and visualized via Kibana dashboards. This helps us trace application behavior and debug issues effectively.

- **Prometheus + Grafana**  
  Prometheus is used to scrape and store time-series metrics from various components. Grafana is connected to Prometheus to provide real-time dashboards, giving insights into service and system performance.

- **Node Exporter**  
  Installed alongside Prometheus to expose hardware and OS-level metrics such as CPU usage, memory consumption, and disk I/O from the host machine.

- **Alertmanager**  
  Integrated with Prometheus to handle alerting rules. It sends alerts via Telegram based on specific metric thresholds, enabling faster incident response and minimizing downtime.

## ⚙️ Server Configuration

We optimized the deployment environment with the following configurations:

- **Nginx Reverse Proxy**  
  Nginx is configured to serve as a reverse proxy, forwarding HTTPS traffic from users to the backend services. This centralizes traffic routing and simplifies exposure of internal services.

- **SSL via Let's Encrypt**  
  Secure HTTPS communication is enabled using certificates issued by Let’s Encrypt. This ensures that all data transferred between the client and server is encrypted and secure.

- **Dockerized Deployment**  
  The entire application, including backend, frontend, and monitoring tools, is containerized using Docker. Services are orchestrated using `docker-compose` to simplify development, testing, and production deployment.

---
# 🎨 Product Design Enhancements

Our product design process focused on creating a smooth, intuitive, and accessible user experience for both desktop and mobile platforms. The design work was led by the frontend and product design team members in collaboration with feedback from customer development sessions.

## 🖥 Desktop Application Design

- We developed a complete **high-fidelity desktop UI** in Figma, reflecting the final visual look and layout of the application.  
- The design includes all major user flows: registration/login, project creation, profile management, project browsing, invitation handling, and filtering.
- This Figma file was used as the **single source of truth** for frontend implementation, ensuring visual consistency across components.
- Link: [High-Fidelity Desktop Design](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=ipSTIA94kiUU0fP1-1)

## 📱 Mobile Application Concept

- A mobile version of the platform was conceptualized to explore future extensibility and enhance user accessibility.
- The design is presented in **low-fidelity wireframes**, focusing on layout structure, user interaction patterns, and adapting features to smaller screens.
- This concept ensures our design system is responsive and considers on-the-go use cases for project browsing, receiving invites, or quick applications.
- Link: [Mobile UX Concept – UX Research](https://www.figma.com/design/islrijonPzZEUrBi9NgV94/UX-UI-Mid?node-id=47-31994&t=bATNSWtlbjcDZmov-1)

## 🔄 Iterative Design Process

- Designs were updated incrementally based on user feedback collected through customer interviews and usability testing.
- We prioritized simplicity, clear visual hierarchy, and ease of navigation—especially in pages involving filtering and forms (like project creation and profile editing).
- The team ensured that color contrast, button placements, and content readability met accessibility guidelines where possible.

---

# 🧾 Presentation Draft

📽 [Google Slides Draft Presentation](https://docs.google.com/presentation/d/1BywG0vKwBAYrr6pOMzMjQu8Lwm-46xev3xxxsQ51wG4/edit?usp=sharing)

---

# Weekly commitments

- **Ahmed Baha Eddine Alimi:**
    - Updated GitHub Issues to reflect current progress. [View Issues](https://github.com/IU-Capstone-Project-2025/InnoSync/issues)
    - Coordinated cross-functional work across frontend, backend, and design teams.
    - Implemented frontend bug fixes. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/090e77c73f0a8739069d34f4c21f3b8e7a9baea2)
    - Conducted UX research and analysis for the **Mobile Application**. [View Research](hhttps://www.figma.com/design/islrijonPzZEUrBi9NgV94/UX-UI-Mid?node-id=47-31994&t=bATNSWtlbjcDZmov-1)
    - Wrote the report.


- **Yusuf Abudghafforzoda:**
    - Assisted in integrating the **ML model** with backend endpoints. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/5c9795102a4573622c340ea9f4f31265c7c03281)
    - Updated and refined the **API documentation** for clarity and consistency. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/4c02ccae6d383577af4075ceaf9b5f113a90b815)

- **Egor Lazutkin:**
    - Prepared and structured the content for the **final presentation** slides. [Draft Presentation](https://docs.google.com/presentation/d/1BywG0vKwBAYrr6pOMzMjQu8Lwm-46xev3xxxsQ51wG4/edit?usp=sharing)


- **Asgat Keruly:**
    - Investigated and resolved frontend bugs affecting the user experience. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/615aebc72f2909d7bf43d34ea8c6ecc472188291)
    - Participated in the development of the **QuickSync integration** in the design.[View Design](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=ipSTIA94kiUU0fP1-1)
    - Contributed to the structure and writing of the report.

- **Anvar Gilmiev:**
    - Fixed multiple frontend bugs and worked on component polishing. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/524af3fc9e77dd14d8ff028927935e8a37ffca39)

- **Aibek Bakirov:**
    - Finalized monitoring and logging setup using **ELK Stack**, **Prometheus + Grafana**, and **Alertmanager** for alerting via Telegram.
    - Verified and maintained **Nginx reverse proxy** and **SSL configuration** with Let’s Encrypt.
    - Ensured production deployment remains stable and secure.

- **Gurbanberdi Gulladyyev:**
    - Fixed the ML integration to work seamlessly with the backend data model. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/5c9795102a4573622c340ea9f4f31265c7c03281)
    - Integrated ML service with backend APIs, including adding JWT authentication support. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/5c9795102a4573622c340ea9f4f31265c7c03281)
    - Began implementing an enhanced ML model for improved performance and accuracy.

## Plan for Next Week


---

### Frontend
- Finalize and polish the current UI to ensure a smooth, bug-free user experience for the final delivery.
- Perform thorough UI/UX refinements based on feedback and usability testing results.

---

### Backend
- Conduct comprehensive bug hunting and fix any critical or minor issues.
- Optimize backend performance and ensure stable API behavior.

---

### Machine Learning
- Complete the final development and tuning of the ML model.
- Perform real-user testing to validate model accuracy and usability.
- Integrate feedback to improve the model before production deployment.

---

### DevOps
- Optimize frontend image assets by reducing sizes and applying efficient compression techniques.
- Improve overall frontend loading speed and performance metrics.

---

### Customer Development (CustDev)
- Finalize the demo presentation.
- Incorporate feedback from trial presentations to enhance clarity and impact.

---

### Product & Design
- Finalize onboarding and verification UI designs to enhance user acquisition flow.
- Ensure consistent alignment and styling of interface elements across all pages for a unified look.
- Complete the mobile app design, preparing it for handoff to development.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [**✔**] In working condition.
- [**✔**] Run via docker-compose (or another alternative described in the `README.md`).