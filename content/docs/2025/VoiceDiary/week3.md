# Week 3 MVP Development 

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

# Implemented MVP features 
- Emotion recognition based on voice
- Summary for user voices
- User frendly design: minmum effort functionality
- Pause and resume recording without data loss
- Visual feedback while recording: timer and waveform



# Demonstration of the working MVP 
[CLICK TO SEE](https://drive.google.com/file/d/12MUHKCTWQI3D3ffB8yz_1a0jFMhyZCEH/view?usp=sharing)

# Frontend

**Responsible:** Dziyana Melnikava, Anastasia Kuchumova

Link to Frontend contribution: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/frontend)

---

# Backend

**Responsible:** Olesia Novoselova, Danil Davydyan

Link to Backend contribution: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/backend)

Swagger demonstartion: [CLICK TO SEE](https://drive.google.com/drive/folders/1trXUJF8lo0l9oZiHlHI-ezu67flPScue)

---

# ML

**Responsible:** Dzhamilia Fatkullina, Elina Kuzmichyova

Link to ML contribution: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/ml)

Link to the training code: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/blob/main/ml/models/finetuning/Wav2Vec2_dusha_study.py)

Link to model artifacts: [CLICK TO SEE](https://disk.yandex.ru/d/LWot5j8zuPGqAw)





## Individual commitments

---

| Team member              | Telegram alias  | Contribution                                                                                                                                                                                                              | Link                                                                                                                                                                                                                                                                                                                                      |
| ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dziyana Melnikava (Lead) | @meldilen24     | Connected frontend with backend, Finished adaptive design of Sign-Up and Loging page, Made custom Error handling, updated README| [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=meldilen), [README](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/frontend#readme) |
| Anastasia Kuchumova      | @n_rngk         | Made results page, Improved UX-UI by adding above microphone clues and a loader, Updated Dockerfile  | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/frontend/feature/analysisOutput)                                                                                                         |
| Dzhamilia Fatkullina     | @jam11a         | Add new emotion recognition model, added multilingual support and translation, write report  | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main?author=DzhamiliaFatkullina), [README](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/ml#readme)                                                                                                                                                                                                         |
| Elina Kuzmichyova        | @lin_anile      | Train Wav2Vec model, add model for text summary, write report       | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main?author=ellilin), [Models](https://disk.yandex.ru/d/LWot5j8zuPGqAw), [README](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/ml#readme)                                                                                                                                                                                                        |
| Olesia Novoselova        | @doiwannaknoww8 | Implemented the logic for voice data transfer, improved integration between the Go API and the Python ML service, set up Docker Compose                                                                                                                                                                                   |     [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main?author=olesia8novoselova), [Swagger Demo](https://drive.google.com/drive/folders/1trXUJF8lo0l9oZiHlHI-ezu67flPScue)                                                                                                                                                                                                                                                                                                                                      |
| Danil Davydyan           | @chocop         | Improved communication between the backend and ML, established communication between the Go API and Python API                                                                                                                                                                     | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main?author=Dan1lD)                                                                                                                                                                                                                                                                                                                                          |
---

### **Plan for Next Week**

#### ML
- Research emotion recognition model based on text
- Research LLM model to add support comments based on user voices

#### Frontend
- Finish Authorization page and connect it with backend
- Create Hompage
- Limit record length for unauthorized users

#### Backend
- Service logs
- Secure storage of user data
- Performance measurements under load
- Authorization


### **Confirmation of the code's operability**

We confirm that the code in the main branch:

- [✓] In working condition.
- [✓] Run via docker-compose (or another alternative described in the README.md).

