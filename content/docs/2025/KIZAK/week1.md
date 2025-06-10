---
title: "Week #1"
---

# Week #1

## 👥 **Team Members**

| Team Member            | Telegram ID          | Email Address                       | Track    | Responsibilities              |
|------------------------|----------------------|-------------------------------------|----------|-------------------------------|
| Marsel Berheev (Lead)  | @mrbrtg              | m.berheev@innopolis.university      | DevOps   | Documentation, DevOps         |
| Makar Egorov           | @sashosr             | m.egorov@innopolis.university       | Backend  | Backend Development           |
| Maksim Malov           | @newspec             | m.malov@innopolis.university        | Backend  | Backend Development           |
| Timur Farisunov        | @netimaaa            | t.farizunov@innopolis.university    | Frontend | Frontend Development, Design  |
| Sarmat Lutfullin       | @lutfullin_sarmat    | s.lutfullin@innopolis.university    | Frontend | Frontend Development, Design  |
| Ulyana Chaikovskaya    | @uchaikouskaya       | u.chaikouskaya@innopolis.university | ML       | ML Engineer, NLP              |
| Kseniia Khudiakova     | @ksksksksksksksushka | k.khudiakova@innopolis.university   | ML       | ML Engineer, NLP              |

## 💡 Project Idea

### 🚨 Problem Statement

In today’s fast-evolving IT field, newcomers face an huge number of frameworks, libraries, tools, and learning platforms. Choosing the right career path, identifying the most relevant technologies, and creating a structured learning plan often feels hard and frustrating without expert guidance.


### 🔍 Market Research

Although several projects aim to solve similar problem, each comes with unique advantages and limitations. To create a more refined and comprehensive solution, our team analyzed **6 comparable projects**, identifying key features and limitations in the current market.

| **Project Name**                                       | **Link**                                                                  | **Pros**                                                                                                                      | **Cons**                                                                                            |
| ------------------------------------------------------ | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **AI Career Coach by redjules**                        | [GitHub](https://github.com/redjules/ai-career-coach)                     | - Open-source with customizable features<br>- Interview preparation via quizzes         | - Requires technical knowledge to set up<br>- Not scalable for large audiences                      |
| **AI Career Coach by calvin1011**                      | [GitHub](https://github.com/calvin1011/ai-career-coach)                   | - Focus on interviews with real-time feedback<br>- Good for practicing technical Q\&A                                    | - Narrow scope and poor planning features                           |
| **FutureFit AI**                                       | [Website](https://www.futurefit.ai/)                                      | - Career navigation based on real market data<br>- Scalable and enterprise-ready<br>- Personal career coaching at scale | - May lack long-term user engagement<br>- Enterprise focus may reduce accessibility for individuals |
| **Coach by CareerVillage**                             | [Website](https://www.aicareercoach.org/)                                 | - Research-based and community-backed<br>- Aims to close real skill gaps across populations                                   | - Limited documentation of detailed features and technical capabilities                             |
| **LearningPath.ai**                                    | [Website](https://learningpath.ai/)                                       | - Curated paths focused on Data & AI careers<br>- Hands-on, project-driven methodology                                        | - Narrow in scope; not ideal for users outside of data/AI domains                                   |
| **AI Personalized Learning Platform by HemantKumar01** | [GitHub](https://github.com/HemantKumar01/AIPersonalizedLearningPlatform) | - Offers personalized roadmaps with resource recommendations<br>- Simple and practical                                        | - Lacks advanced AI features like interactive coaching or resume creation                           |


### 🌟 Our Solution: **KIZAK**

We introduce **KIZAK** — an AI-powered learning and career guidance platform built to make IT education accessible, intelligent, and personalized. **KIZAK** supports users in setting clear goals, assessing their current knowledge, and developing structured learning paths to advance confidently in their careers.

Unlike existing tools, **KIZAK** integrates **career planning**, **AI coaching**, **daily recommendations**, and **skill tracking** into a unified experience — personalized for every user.

## 👥 **User Profiling**  
To build a successful product, we must deeply understand our customers—their needs, goals, and challenges.  

### 🎯 **Target Users**  
Our primary users are professionals and learners in the **IT field**, including:  
- **Students** seeking structured, high-quality education to kickstart their careers.  
- **Junior Developers** looking to upskill and gain a competitive edge in the job market.  
- **Career Switchers** transitioning into tech who need guided roadmaps for efficient learning.

### 💬 **User Stories**  
User stories help prioritize features based on real needs. Here’s what our users say:  

1. As a **student**, I want to find **good mentor** so that I will get good learning plan
2. As an **intern**, I want to create a **good resume** to increase my chances of getting an offer from a good company.
3. As a **career switcher**, I want to **have a roadmap** so that I can efficiently learn new skills
4. As a **junior developer**, I want to **improve my skills** so that I get better position in company
5. As a **user**, I want **simple auntefication** so I wont forget my password

## 🚀 Project Features

### 🔑 **Key Features**
The MVP v0 will focus onthe following essential feature

* **🔍 Onboarding & Goal Setting**
  Personalized user profiles with skill self-assessment, career goals, and technology preferences.

* **🧠 ML-Powered Learning Paths**
  AI-generated roadmaps based on individual goals, learning pace, and current skill set.

* **📄 Resume Generator**
  Dynamically creates a professional resume highlighting skills, courses, and projects as users progress.

### 🔮 **Future Features**
Also our team have additional functionality planned for future updates

* **🎯 Smart Recommendations**
  Automatically delivers daily/weekly content from trusted sources (e.g., Coursera, YouTube, Stepik).

* **💬 AI Career Coach**
  Virtual assistant to:

  * Answer learning-related questions
  * Simulate technical interviews
  * Review your learning path and resume
  * Provide motivational and feedback loops

* **🔗 Platform Integrations**
  Link GitHub, LinkedIn, and email accounts to sync portfolios, display achievements, and streamline sign-in.

* **📊 Skill Progress Tracker**
  Visual dashboards showing completed tasks, acquired skills, and roadmap milestones.

* **🔐 Secure OAuth Authentication**
  Industry-standard login and data security protocols for smooth and safe user access.
Here’s an enhanced version with badges (using emojis and formatting for visual appeal) and minor corrections:  

## 🛠️ **Tech Stack**  

### **Backend**  
- **Flask**  🐍  - A **lightweight** Python web framework for building scalable APIs and backend services.
- **PostgreSQL** 🐘 - A **powerful**, open-source relational database with strong extensibility and SQL compliance.

### **Frontend**  
- **React** ⚛️ - **Fast and popular** JavaScript library for building dynamic, component-based user interfaces.
- **Next.js** ▲ - React framework for **server-side renderin**g, static sites, and **scalable web apps**.
- **Tailwind CSS** 🎨 - Utility-first CSS framework for **rapid UI development** with minimal custom CSS.
- **Redux** 🔄 - **State management** library for predictable global state in JavaScript apps.

### **ML / AI**  
- **LLaMA** 🦙 - Meta’s open-source large language model for **advanced NLP** tasks.
- **Transformers** 🤗 - Hugging Face’s library for state-of-the-art NLP models

## ⚙️ Repo Setup
You can find the boilerplate and source code for our project in the official repository:

👉 [KIZAK_Capstone](https://github.com/LowIQCoder/KIZAK_Capstone)

All instructions for setting up and running the project locally are available in the repository’s [README.md](https://github.com/LowIQCoder/KIZAK_Capstone/blob/main/README.md) file.
