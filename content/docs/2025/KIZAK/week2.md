---
title: "Week #2"
---

# **Week #2**

## ⚙️ **Detailed Requirements Elaboration**

### 👤 **Detailed User Stories**
* **Student Seeking Mentorship**  
  **As a computer science student**, I want to **find an experienced mentor** in my field so that **I can get a personalized learning plan** to study efficiently without feeling overwhelmed.  
  
  **Acceptance Criteria**:  
  ✅ Mentor profiles with:  
     - Areas of expertise (e.g., Python, Web Dev, Data Science)  
     - Availability (timezone-friendly schedule)  
     - Ratings/reviews from past mentees
       
  ✅ Matching system based on:  
     - My current skill level (beginner/intermediate)  
     - My learning goals (e.g., "get a good offer")   
  
  **Edge Cases**:  
  ⚠️ No mentors available in my area (e.g., Rust programming)  
  ⚠️ Mentor has poor communication 

* **Intern Resume Builder**  
  **As a tech intern**, I want to **create an resume** with industry-specific templates so that **I can pass automated screenings and impress hiring managers**.  
  
  **Acceptance Criteria**:  
  ✅ Pre-filled templates for tech roles (Backend Developer, Data Analyst, etc.)
  
  ✅ Real-time feedback
  
  ✅ One-click export to PDF/LinkedIn  
  
  **Edge Cases**:  
  ⚠️ I have no prior work experience  
  ⚠️ My projects are school assignments (how to present them)  
  ⚠️ Non-traditional background (e.g., self-taught)  

* **Career Switcher Roadmap**  
  **As a marketing professional switching to data science**, I want a **customized 6-month roadmap** so that **I can focus only on relevant skills (SQL, Python, stats) without wasting time**.  
  
  **Acceptance Criteria**:  
  ✅ Roadmap adjusts based on:  
     - My 20-hour/week availability
         
  ✅ Includes:  
     - Free/low-cost resource links (Coursera, Stepik)   
     - Personal tasks  
  
  **Edge Cases**:  
  ⚠️ I get stuck on a topic (e.g., linear algebra)  
  ⚠️ Job market shifts (e.g., sudden demand for PySpark)  

* **Junior Developer Upskilling**  
  **As a junior React dev**, I want to **identify and fill skill gaps** through curated challenges so that **I can qualify for mid-level roles within 12 months**.  
  
  **Acceptance Criteria**:  
  ✅ Skill assessment quiz outputting:  
     - Priority areas (e.g., "Learn Redux for state management")  
     - Weak spots (e.g., "API design best practices")
       
  ✅ Progress tracker showing:  
     - Competency growth (e.g., "Frontend: 60% → 85%")  
     - Peer benchmarks  
  
  **Edge Cases**:  
  ⚠️ Conflicting advice from different seniors  

* **User Authentication**  
  **As a forgetful user**, I want to **sign up/login with Google/GitHub** so that **I don’t get locked out due to password issues**.  
  
  **Acceptance Criteria**:  
  ✅ Social login options:  
     - Google  
     - GitHub
       
  ✅ Clear error messages for:  
     - "Email already in use"  
     - "Account locked (too many attempts)"  
  
  **Edge Cases**:  
  ⚠️ My social account gets hacked  

### 🐗 **Prioritized backlog**

Our current backlog could be found [here](https://github.com/orgs/IU-Capstone-Project-2025/projects/11) 

## 📈 **Project specific progress**

### 🖼️ **Design**

* Created initial [design](https://www.figma.com/design/Ew8Vmgzn739HYN2aAaVb1s/Untitled?node-id=0-1&t=eC6UcHbY32eWsSUx-1) for:
  * Initial page (by Sarmat)
  * Onboarding pages (by Timur)
  * Main page with roadmap (by Timur)
  * Options (by Timur)

### ♿ **Frontend**

* Created Initial page (by Sarmat)
* Created Login and Singup pages (by Sarmat)
* Created Onboarding page (by Timur)
* Created Main page (by Timur)

### ⚙️ **Backend**

* Created initial CI/CD pipeline (by Maksim)
* Created database [prototype](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/db/init.sql) (by Marsel)
* Created base endpoints for
  * User CRUD operations (by Maksim)
  * Roadmap CRUD operations (with nodes and links) (by Marsel)
  * Resource CRUD operations (by Marsel)
* Created simple [docs](https://github.com/IU-Capstone-Project-2025/KIZAK/tree/main/docs) for API

### 🤖 **ML**

* Training dataset selected (by Ksenia & Ulyana)

# 📝 **Weekly commitments**

## 📊 **Individual contribution of each participant**

* **Marsel Berheev:** m.berheev@innopolis.university
  * Weekly report
  * Roadmap and Resource API design (see [issue](https://github.com/IU-Capstone-Project-2025/KIZAK/issues/27) or [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/30))

* **Maksim Malov:** m.malov@innopolis.university
  * CI/CD pipeline initial design (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/6))
  * User API design (see [issue](https://github.com/IU-Capstone-Project-2025/KIZAK/issues/18) or [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/28))

* **Makar Egorov:** m.egorov@innopolis.university
  * Course scraping (see [issue](https://github.com/IU-Capstone-Project-2025/KIZAK/issues/15))

* **Timur Farizunov:** t.farizunov@innopolis.university
  * Onboarding and main page design (see corresponding frames in [figma](https://www.figma.com/design/Ew8Vmgzn739HYN2aAaVb1s/Untitled?node-id=0-1&t=eC6UcHbY32eWsSUx-1))
  * Main page design and frontend structure setup (see [commit](https://github.com/IU-Capstone-Project-2025/KIZAK/commit/1cf59a878d99964351fa6d0eefe34f39f559f5c7))

* **Sarmat Lutfullin:** s.lutfullin@innopolis.university
  * Initial page design (see corresponding frames in [figma](https://www.figma.com/design/Ew8Vmgzn739HYN2aAaVb1s/Untitled?node-id=0-1&t=eC6UcHbY32eWsSUx-1))
  * Login and Singup frontend (see [commit](https://github.com/IU-Capstone-Project-2025/KIZAK/commit/5fedd0bdef21244b3a52e645818afd19f076e1e0))
 
* **Ulyana Chaikovskaya:** u.chaikouskaya@innopolis.university
  * Dataset analisys (see corresponding frame in [miro](https://miro.com/app/board/uXjVIrMw-Nw=/?share_link_id=30918973188) or [issue](https://github.com/IU-Capstone-Project-2025/KIZAK/issues/13))

* **Kseniia Khudiakova:** k.khudiakova@innopolis.university
  * New dataset design (see [ipynb file](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/feature-job_skill_mapping/ml/jv_mapping.ipynb))

## 🎯 **Plan for Next Week**

* Finish frontend MVP
  * Polish existing pages
  * Complete end to end userflow
  * Design refinement
* Integrate API to MVP
  * Integration with existing endpoints
  * Adding new endpoints if needed
* Update documentation
  * Complete documentation for API
* First iteration of AI model
* Finish dataset design

## **Confirmation of the code's operability**

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
