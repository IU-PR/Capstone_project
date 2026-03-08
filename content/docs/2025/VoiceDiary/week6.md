# Week 6

**Project name:** VoiceDiary

**Code repository:** [link](https://github.com/IU-Capstone-Project-2025/VoiceDiary)

**VoiceDiary** is an AI-powered voice journaling tool that analyzes tone, emotion, and key themes in spoken entries. It generates personalized emotional insights and well-being suggestions based on recorded reflections.

# Team

| Team member          | Telegram alias  | Innopolis Email                    | Responcibilities |
| -------------------- | --------------- | ---------------------------------- | ---------------- |
| Dziyana Melnikava    | @meldilen24     | dz.melnikava@innopolis.university  | PM, Frontend     |
| Anastasia Kuchumova  | @n_rngk         | a.kuchumova@innopolis.university   | Frontend, UX/UI  |
| Dzhamilia Fatkullina | @jam11a         | d.fatkullina@innopolis.university  | ML               |
| Elina Kuzmichyova    | @lin_anile      | e.kuzmichyova@innopolis.university | ML               |
| Olesia Novoselova    | @doiwannaknoww8 | o.novoselova@innopolis.university  | Backend          |
| Danil Davydyan       | @chocop         | d.davydyan@innopolis.university    | Backend          |

## Links  

**Deployment**: [Link](https://178.205.96.163:443)  
**API Docs**: [Swagger](https://drive.google.com/drive/folders/1c47heTBhiNhkhRdKbm1zMVKSpNiOMXks?usp=sharing), [README.md](https://github.com/IU-Capstone-Project-2025/VoiceDiary/blob/main/backend/README.md)  
**Design&Demo**: [Link](https://drive.google.com/drive/folders/1TnhcD9yxOiT_D2OI4j3NvfDhLdaFmVHs?usp=sharing)  

##  Project Overview

**Voice Diary** is a voice-based journaling application designed to make emotional self-tracking more natural, engaging, and insightful. Unlike traditional text-based mood trackers, this app lets users record short voice messages and uses AI to analyze vocal tone and content to determine the **"Emotion of the Day"**, provide **personalized recommendations**, and identify **emotional patterns over time**.

This app is intended for users who are interested in monitoring their emotional wellbeing but want a more interactive and personalized experience. It leverages voice as a natural medium for expression and uses machine learning models to extract emotional insights.

### ✅ Solves the Problem of:
- Low engagement in mood tracking apps
- Lack of personalization in emotional wellness tools
- Time-consuming journaling habits


## Features

The following features are fully implemented in this version of the app:

- 🎙️ **Voice-based Emotion Detection**  
  Record a voice note and get real-time emotion classification.

- 📊 **Emotional Pattern Tracking**  
  View your recent emotional history and observe trends over time.

- 🧠 **Personalized Recommendations**  
  Receive daily suggestions based on your emotional state and patterns.

- ✍️ **Manual Emotion Input**  
  Override or set your emotion manually if desired.

- 📁 **Secure Diary Storage**  
  Each entry is saved securely in your personal log for future reflection.


## Tech Stack

### Backend:
- **Go** with **Gin** framework — RESTful API services
- **Python** with **FastAPI** — AI model serving for emotion classification
- **PostgreSQL** — Voice entry and metadata database

### Frontend:
- **React.js** — Interactive and responsive user interface
- **Redux** — State management for UI and API interactions

### AI/ML:
Audio Pipeline
- **Whisper Large V3 fine-tuned** + **j-hartmann** → Emotion classification
- **Whisper Large V3** → Low-latency transcription
Analysis Layer
- **Samsum** → Concise daily summaries
- **OpenHermes-2.5** → Psychological insights

## 🚀 Setup Instructions

```
git clone https://github.com/IU-Capstone-Project-2025/VoiceDiary.git
mv .env.example .env
docker-compose up --build # in root directory of the repository
```

## Presentation Draft

[Link](https://www.canva.com/design/DAGtPo9TD4M/-AFZsf0dNmS92UcIOA8wdw/edit?utm_content=DAGtPo9TD4M&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Individual commitments

---

| Team member              | Telegram alias  | Contribution                                                                                                                                                                                                | Link                                                                                                                               |
| ------------------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Dziyana Melnikava (Lead) | @meldilen24     | Fixed bugs: secure connection (usage of 443 port, wrote SSL certificates, wrote nginx service for Docker), api for user info update reconnected, New features: added record list displaying, updated design, connected insights and updated form for them                                                                                   | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=meldilen)                                            |
| Anastasia Kuchumova      | @n_rngk         | Finished CI, updated the calendar, added entries list feature, added documentedation of components                                                                                                                  | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=Ann24-02)                                            |
| Dzhamilia Fatkullina     | @jam11a         | Tested input texts, Improved insight generation LLM prompt, Fixed output cleaning & JSON extraction bug, Prepared draft presentation & Week 6 report                                                                                                                                 | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=DzhamiliaFatkullina)  |
| Elina Kuzmichyova        | @lin_anile      | finalized testing of emotion by test model, built two versions of emotion orchestration—basic and one with a custom covariance matrix, tested by tweaking transitions (limiting neutral jumps)     | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits?author=ellilin) |
| Olesia Novoselova        | @doiwannaknoww8 | REST endpoints in Go service for: Record deletion, Profile update, User existence check during registration, Refactored database schemas | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=olesia8novoselova)                                                      |
| Danil Davydyan           | @chocop         | Fixed insights generation in Go backend, Disabled DB save for onboarding page entries, Fixed Docker Compose (production setup with Nginx), Updated Go tests                                                                                                                    | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits?author=Dan1lD)                                                      |

---

### **Plan for Next Week**

#### ML
- Further improve psychological insights prompt
- Add emotion aggregation logic to handle days with excessive entries
- Finalize README.md

#### Frontend
- Improve connection safety
- Improve UX/UI design
- Test and fix bugs
- Finalize README.md

#### Backend
- Model inference optimization
- API endpoint refactoring (new contract compliance)
- Finalize handler logic (full consistency check)
- Verify test coverage & passing status
- Finalize README.md


### **Confirmation of the code's operability**

We confirm that the code in the main branch:

- [✓] In working condition.
