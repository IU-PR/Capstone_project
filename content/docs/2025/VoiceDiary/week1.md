# Week 1

# Project description

---

**Project name:** VoiceDiary

**Code repository:** [link](https://github.com/IU-Capstone-Project-2025/VoiceDiary)

**VoiceDiary** is an AI-powered voice journaling tool that analyzes tone, emotion, and key themes in spoken entries. It generates personalized emotional insights and well-being suggestions based on recorded reflections.

# Team

---

| Team member | Telegram alias | Innopolis Email | Responcibilities |
| --- | --- | --- | --- |
| Dziyana Melnikava | @meldilen24 | dz.melnikava@innopolis.university | PM, Frontend |
| Anastasia Kuchumova | @n_rngk | a.kuchumova@innopolis.university | Frontend, UX/UI |
| Dzhamilia Fatkullina | @jam11a | d.fatkullina@innopolis.university | ML |
| Elina Kuzmichyova | @lin_anile | e.kuzmichyova@innopolis.university | ML |
| Olesia Novoselova | @doiwannaknoww8 | o.novoselova@innopolis.university | Backend |
| Danil Davydyan | @chocop | d.davydyan@innopolis.university | Backend |




# Brainstorming

---

### **Ideas during brainstorming**

| Rank | Idea |
| **1** | An AI-based voice journaling platform that processes spoken reflections to detect emotional tone, mood trends, and core topics, offering personalized mental well-being feedback. |
| **2** | A self-growth tracker where users build and evolve virtual “selves” representing different aspects of personality. |
| **3** | A sleep-integrated dream and emotion journal that analyzes voice-recorded dreams and detects subconscious emotional trends. |

### Problem validation

**1. VoiceDiary**

**Problem**: People often struggle to identify and understand their emotional patterns, lack time or motivation for traditional journaling, and find it hard to reflect consistently.

**Validation**:

- Voice is perceived as a more natural and less effort-intensive method of self-expression in self-reflection contexts.


**2. PersonaPulse**

**Problem**: Many people feel disconnected from different parts of their personality (e.g., professional vs emotional self) and lack structured tools to develop personal traits in a holistic and engaging way.

**Validation**: 

- Behavioral patterns suggest that people engage more when self-development is approached playfully or symbolically rather than abstractly.


**3. Sleep-Sleep**

**Problem**: Dreams are a rich source of emotional insight, but most people forget them quickly or lack a structured way to reflect on their subconscious thoughts.

**Validation**:

- Cognitive psychology suggests that reflecting on dream content can increase awareness of unresolved emotional issues.


# Basic Requirements

---

## Target Users and Their Primary Needs
**Reflective Individuals:** People interested in understanding themselves better, journaling, or mental wellness

- Need: A natural, non-intrusive way to reflect emotionally


**Busy Individuals:** People with limited time for self-reflection or therapy 

- Need: A low-effort tool to track emotions and stress without interrupting routine



## User Stories
- As a user, I want to speak freely into the app so I can reflect without needing to write or plan.
- As a user, I want the experience to require minimal effort so I can use it even on busy or stressful days.
- As a user, I want the app to identify patterns in my mood and emotions over time so I can understand my mental state (statistics).
- As a user, I want the system to recognize tone and key themes in what I say so I can gain deeper self-insights.
- As a user, I want to receive recommendations so I can take small steps toward emotional well-being.
- As a user, I want the app to feel like a personal, private space so I can be honest and unfiltered in my entries.


## Initial Scope (MVP)

---

| **IN Scope (W1–W3)** | **OUT (Post-MVP)** |
| --- | --- |
| Basic homepage with embedded calendar | Authentication + Enhanced homepage with achievements |
| Integration with 1 emotion recognition model | Voice record analysis + recommendations |
| No statistics | Emotion statistics (weekly/monthly/yearly) |



## Tech Stack

---

|  | **Choice** | **Justification** |
| --- | --- | --- |
| **Frontend** | React | For building a responsive, modern web interface with reusable components and efficient state management. |
| **Backend** | Golang | High performance, concurrency support, and fast API response times; suitable for real-time web services. |
| **ML API** | Python | Extensive machine learning libraries and seamless integration with pretrained models. |
| **ML Models** | Whisper (by OpenAI), Emotion_Recognition_From_Speech, xlsr-wav2vec-speech-emotion-recognition | Open-source, speech-focused models with high accuracy; suitable for emotion detection from voice; will be tested and selected based on performance. |
|  | LLaMA | To generate contextual emotional feedback and personalized recommendations based on analysis. |
| **Database** | PostgreSQL | Reliable relational database with strong consistency guarantees and support for structured data (e.g. logs, users, entries). |
| **Auth** | OAuth | Standard and secure method for third-party authentication, reduces password handling and improves UX. |
| **Infra** | Docker + Docker Compose | Ensures consistent development and production environments, simplifies deployment. |
|  | GitHub Actions (CI/CD) | Enables continuous integration, testing, and deployment with minimal manual effort. |


## Collective commitments

---

Met with the team, Discussed our project visions, Finalized the system architecture and technology stack after thorough discussion of all ideas.




## Individual commitments

---

| Team member | Telegram alias | Contribution | Link |
| --- | --- | --- | --- |
| Dziyana Melnikava (Lead) | @meldilen24 | Developed the frontend project structure and finalized the UX/UI design—agreeing on the layout and visuals, with references sourced from Pinterest | https://github.com/IU-Capstone-Project-2025/VoiceDiary/commit/77cfcc49a1ce1f5ee2a28c466bec73250009cc60, https://pin.it/35So4qndM |
| Anastasia Kuchumova | @n_rngk | Developed the frontend project structure and finalized the UX/UI design—agreeing on the layout and visuals, with references sourced from Pinterest | https://github.com/IU-Capstone-Project-2025/VoiceDiary/commit/d81e7231d7c82c923c435448f21307478cb15807, https://github.com/IU-Capstone-Project-2025/VoiceDiary/commit/2684b933021ed546455311b5e23e13603908d098, https://pin.it/35So4qndM |
| Dzhamilia Fatkullina | @jam11a | Researched emotion recognition models and datasets, selecting the most suitable ones for the project | https://huggingface.co/harshit345/xlsr-wav2vec-speech-emotion-recognition, https://huggingface.co/dmdoy/Emotion_Recognition_From_Speech, https://github.com/openai/whisper/blob/main/model-card.md, https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio, https://www.kaggle.com/ejlok1/cremad, https://www.kaggle.com/ejlok1/toronto-emotional-speech-set-tess, https://www.kaggle.com/datasets/ejlok1/surrey-audiovisual-expressed-emotion-savee, https://github.com/salute-developers/golos/tree/master/dusha#dusha-dataset and a few others |
| Elina Kuzmichyova | @lin_anile | Read research papers on the selected models, conducted a comparative analysis, and outlined the machine learning implementation plan | https://arxiv.org/abs/2212.04356, https://arxiv.org/abs/2212.12266, https://huggingface.co/dmdoy/Emotion_Recognition_From_Speech |
| Olesia Novoselova | @doiwannaknoww8 | Wrote project report and user stories | this commit ; ) |
| Danil Davydyan | @chocop | Set up the backend infrastructure, started developing backend of the project | https://github.com/IU-Capstone-Project-2025/VoiceDiary/commit/ab02bd635be5262cbbfa3920b1994cfb2e57dda4 |



### **Confirmation of the code's operability**

We confirm that the code in the main branch:

- [✓]  In working condition.
- [✓]  Run via docker-compose (or another alternative described in the `README.md`).

