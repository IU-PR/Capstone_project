# Week 2 Initial Design & Elaboration

**Project name:** VoiceDiary

**Code repository:** [link](https://github.com/IU-Capstone-Project-2025/VoiceDiary)

**VoiceDiary** is an AI-powered voice journaling tool that analyzes tone, emotion, and key themes in spoken entries. It generates personalized emotional insights and well-being suggestions based on recorded reflections.

# Team

---

| Team member          | Telegram alias  | Innopolis Email                    | Responcibilities |
| -------------------- | --------------- | ---------------------------------- | ---------------- |
| Dziyana Melnikava    | @meldilen24     | dz.melnikava@innopolis.university  | PM, Frontend     |
| Anastasia Kuchumova  | @n_rngk         | a.kuchumova@innopolis.university   | Frontend, UX/UI  |
| Dzhamilia Fatkullina | @jam11a         | d.fatkullina@innopolis.university  | ML               |
| Elina Kuzmichyova    | @lin_anile      | e.kuzmichyova@innopolis.university | ML               |
| Olesia Novoselova    | @doiwannaknoww8 | o.novoselova@innopolis.university  | Backend          |
| Danil Davydyan       | @chocop         | d.davydyan@innopolis.university    | Backend          |

---

# Detailed Requirements Elaboration

**Responsible:** Dzhamilia Fatkullina, Dziyana Melnikava

## Expanded User Stories for MVP

As a user, I want to speak freely into the app without typing or structuring my thoughts, so that I can reflect naturally, even when tired or overwhelmed.

**Acceptance Criteria:**

- One-tap recording:  
  ✅ Single press of a microphone button starts/stops recording.  
  ✅ Visual feedback (waveform/timer) confirms active recording.
- Uninterrupted flow:  
  ✅ Pause/resume functionality without data loss.
- Accessibility:  
  ✅ No forced sign-up to record.

---

As a user, I want the app to require almost no setup or cognitive effort, so that I can use it daily, even on busy days.

### Acceptance Criteria:

- Instant insights:  
  ✅ Auto-generated emotion summary (e.g., "You sound reflective today").  
  ✅ 2-3 key themes extracted without user input.
- Zero friction:  
  ✅ Provide user with hints of what he/she can talk about

---

### Backlog in Kaiten: [CLICK TO SEE](https://drive.google.com/drive/folders/1-avR197XspvZUU75_QLxDHV2Ur86uBhX?usp=sharing)

# Design

**Responsible:** Dziyana Melnikava, Anastasia Kuchumova

User Flow Diagrams: [CLICK TO SEE](https://drive.google.com/drive/folders/15oNUbqcYoJvEAS5x4L_bfGQFflLAKU4Z?usp=sharing)

Low-fidelity wireframes in Figma: [CLICK TO SEE](https://drive.google.com/drive/folders/1ppPrjLcYnsuovhGqUTHJI_zxiXkCB9lh?usp=sharing)

---

# Frontend

**Responsible:** Dziyana Melnikava, Anastasia Kuchumova

Link to frontend branch: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/front/feature/onboardingPage)

- The frontend structure was re-formed and made more detailed as MVP vision was changed.
- Skeleton components were created.
- Onboarding page was implemented according to the wireframe design in Figma.

---

# Backend

**Responsible:** Olesia Novoselova, Danil Davydyan

Project Architecture: [Schema](https://drive.google.com/file/d/1nR4DT_XFKpmfW56uH2R8LRGTJr7YABLE/view?usp=sharing)

Database schema: [Schema](https://drive.google.com/file/d/1HbNmjTRkw8eRUrWpAKfJM6FcRqkzfMmR/view?usp=sharing)

Link to API contract for ML: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/pull/1)

Link to Golang HTTP service connected to PostgreSQL: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/feature/go-endpoint/backend/go_api)

---

# ML

**Responsible:** Dzhamilia Fatkullina, Elina Kuzmichyova

Link to ML contribution: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/front/feature/onboardingPage/ml)

## Research Summary

#### Models

#### 1. Emotion Recognition From Speech (V1.0) - don't have access to that model yet

- Predicts six emotions (sad, neutral, happy, fear, angry, disgust) from speech without linguistic information.
- Method: Extracts audio features and passes them to an emotion recognition model.
- Datasets: Uses four publicly available datasets (Ravdess, CREMA-D, TESS, SAVEE) with labeled emotional speech.
- Relevance to VoiceDiary:
  - Can enhance emotion analysis in voice entries by identifying emotional tones.
  - Provides a framework for integrating emotion recognition into VoiceDiary's AI analysis.

#### 2. Robust Speech Recognition via Large-Scale Weak Supervision - Whisper article

- Improves speech recognition robustness using large-scale, weakly supervised pre-training.
- Method: Trains models on 680,000 hours of multilingual audio to generalize across domains without fine-tuning.
- Key Features:
  - Zero-shot transfer learning for diverse speech tasks.
  - Competitive performance with human accuracy in real-world conditions.
- Relevance to VoiceDiary:
  - Enhances transcription accuracy for diverse user voices and emotional tones.
  - Supports multilingual entries, broadening VoiceDiary's usability
  - Transcription can be used for more effective and accurate recomendation and assist in emotion recognition

#### Datasets used in MVP

#### 3. Large Raw Emotional Dataset with Aggregation Mechanism - Dusha, large dataset for emotion recognition in Russian

- Introduces "Dusha," a large Russian speech emotion dataset with acted and real-life recordings.
- Method: Combines crowd-sourced acted speech and podcast segments, annotated via crowd-sourcing.
- Key Features:
  - 350 hours of audio with transcripts, labeled for anger, happiness, sadness, and neutral.
  - Includes raw and aggregated labels for flexible use.
- Relevance to VoiceDiary:
  - Will be used for additional training of Emotion recognition models from speech

### Datasets that we plan to use for future training beyond MVP (Data collection plan)

- [RAVDESS Emotional speech audio](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

- [Crowd Sourced Emotional Multimodal Actors Dataset (CREMA-D)](https://www.kaggle.com/ejlok1/cremad)

- [Toronto emotional speech set](https://www.kaggle.com/ejlok1/toronto-emotional-speech-set-tess)

- [Surrey Audio-Visual Expressed Emotion](https://www.kaggle.com/datasets/ejlok1/surrey-audiovisual-expressed-emotion-savee)

- [MELD: Multimodal EmotionLines Dataset](https://affective-meld.github.io/)

- [Emotion Dataset for Emotion Recognition Tasks](https://www.kaggle.com/datasets/parulpandey/emotion-dataset)

---

## Individual commitments

---

| Team member              | Telegram alias  | Contribution                                                                                                                                                                                                              | Link                                                                                                                                                                                                                                                                                                                                      |
| ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dziyana Melnikava (Lead) | @meldilen24     | Developed User Flow Diagrams and low-fidelity wireframes in Figma (Onboarding, User Profile, enhanced Main pages), updated GitHub with detailed frontend project structure, set up PM tool for tracking, write the report | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/front/feature/onboardingPage/), [User Flow Diagrams](https://www.figma.com/design/LsI0QXuWRl11MRhvdFAC9a/VoiceDiary?node-id=96-1380&m=dev), [Figma Design](https://www.figma.com/design/LsI0QXuWRl11MRhvdFAC9a/VoiceDiary?node-id=120-2046&t=sRCH5CRDDUWRDx2v-0) |
| Anastasia Kuchumova      | @n_rngk         | Developed low-fidelity wireframes in Figma (Main pages, components, Results page), implemented Onboarding Page                                                                                                            | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/front/feature/onboardingPage/), [Figma Design](https://www.figma.com/design/LsI0QXuWRl11MRhvdFAC9a/VoiceDiary?node-id=120-2046&t=sRCH5CRDDUWRDx2v-0)                                                                                                             |
| Dzhamilia Fatkullina     | @jam11a         | Tested Wisper model and wrote research summary                                                                                                                                                                            | [Python code](https://github.com/IU-Capstone-Project-2025/VoiceDiary/blob/front/feature/onboardingPage/ml/models/test_whisper.py)                                                                                                                                                                                                         |
| Elina Kuzmichyova        | @lin_anile      | Tested Wav2Vec model, prepared datasets and data plan, started additional traning                                                                                                                                         | [Python code](https://github.com/IU-Capstone-Project-2025/VoiceDiary/blob/front/feature/onboardingPage/ml/models/test_Wav2Vec2.py)                                                                                                                                                                                                        |
| Olesia Novoselova        | @doiwannaknoww8 | Prepared database shema, created Golang HTTP service connecting to PostgreSQL, fetching user records as JSON via a GET endpoint, offering a POST endpoint to forward a record’s data URL to a Python ML API                                                                                                                                                                                   |     [Pull Request](https://github.com/IU-Capstone-Project-2025/VoiceDiary/pull/2)                                                                                                                                                                                                                                                                                                                                      |
| Danil Davydyan           | @chocop         | Defined the initial API contract on Python for ML, drew project architecture schema                                                                                                                                                                       | [Pull Request](https://github.com/IU-Capstone-Project-2025/VoiceDiary/pull/1)                                                                                                                                                                                                                                                                                                                                          |
---

### **Plan for Next Week**

#### ML
- Finish training Wav2Vec model
- Make summary from voice input transcription
- Make an orchestration of two models to predict a final emotion based on voice and text

#### Frontend
- Create components for showing results of emotion prediction
- Connect frontend components to backend APIs

#### Backend
- Integrate the model’s predictions into the backend
- Implement voice transmission
- Research MinIO

### **Confirmation of the code's operability**

We confirm that the code in the main branch:

- [✓] In working condition.

