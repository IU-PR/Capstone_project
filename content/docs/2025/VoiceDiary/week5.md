# Week 5

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

# Feedback

## Sessions 

    1. "Convenient and beautiful interface, intuitively clear where to click. The site is gorgeous. The output wasn’t very clear to me, but I used it just for fun—it was interesting to see something come out. It’s fascinating to observe how the neural network reacts to my input. I haven’t tried the voice AI yet, but it seems intriguing."

    2. "I visited the site—it’s beautiful, and at first glance, it seemed like something serious. I tried speaking into it, and while the topics were somewhat relevant, the psychological insights didn’t quite fit me. The results were in English even though I spoke in Russian. I’d use it more if the app were higher quality."

    3. "The concept is cool, and the design is modern, but the responses sometimes don't match. I would like if it could all be edited, because I would like to use it daily, sometimes the emotion is not accurate. Also, adding multilingual support would make it more accessible."

## Analize

### Strengths  
✅ **UI/UX praised** – Users highlight the intuitive, visually appealing interface.  
✅ **Engagement potential** – Some interact "for fun," showing interest in observing AI behavior.  
✅ **Voice input curiosity** – Ineresting feature.  

### Pain Points  
⚠ **Output clarity issues** – Confusion over results (e.g., psychological insights feeling mismatched).  
⚠ **Language mismatch** – Russian input yielding English outputs reduces usability.  
⚠ **Perceived lack of depth** – Feedback suggests responses can feel low-quality.  

## Actionable Improvements  

### High Priority  
🔧 **Customizable output fields** – Add emotion editing possibility (to correct when the model is wrong)

🔧 **Input-language consistency** – Warn users that product functionality is in English.  

### Mid/Long-Term  
🌍 **Multilingual support** – Currently high effort; requires deeper pipeline changes.  
🤖 **Emotion recognition improvement** – Refinine context retention, improve emotion recognition.  

### Additional Notes  
- Some users treat the tool as entertainment—could lean into this with a "playful mode" variant. 

## Iteration & Refinement

The product is fully functional and stable in production. While we’re actively addressing minor issues, the core system performs reliably. Next week, we’ll implement several researched features to enhance functionality.
### 📌 Key Progress Highlights:

    Performance & Stability: Rigorous testing has ensured a robust foundation. Remaining issues are edge cases (e.g., rare latency spikes) being prioritized for fixes.

    ML Model Refinement:

        Emotional Insights: Discovered a more accurate approach for emotion analysis (higher precision/recall).

        Orchestration: Finalizing multi-model pipelines for end-to-end emotional recognition.

    Documentation:

        Structured Guides: READMEs in /frontend and /ml detail setup, architecture, and workflows.

        Experimental Work: /experimental includes R&D notes for upcoming features.

#### Next Steps:

    Deploy refined emotional recognition models.

    Optimize API handoffs between backend/ML services.

---

## Individual commitments

---

| Team member              | Telegram alias  | Contribution                                                                                                                                                                                                | Link                                                                                                                               |
| ------------------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Dziyana Melnikava (Lead) | @meldilen24     | Finished debugging authentication, connected profile with storage, added logout handling, worked on handling session errors, collaborated with backend team on connecting new endpoint for record insights and refactoring the database                                                                                           | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=meldilen)                                            |
| Anastasia Kuchumova      | @n_rngk         | Updated design, Created Main and User Profile page,calendar page, autentification page, implemented custom calendar, wrote unit tests, fixed unit tests, create adaptive version of all pages                                                                                                                        | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=Ann24-02)                                            |
| Dzhamilia Fatkullina     | @jam11a         | Researched psychological feedback models, tested 3 approaches of insight extraction, started orchestration implementation                                                                                                                                                           | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=DzhamiliaFatkullina)  |
| Elina Kuzmichyova        | @lin_anile      | Implemented researched models emotion-to-text models, started orchestration implementation            | [Link](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/ml/models/experimental) |
| Olesia Novoselova        | @doiwannaknoww8 | Implemented a logout feature, invalidating session tokens, Refactored the endpoints for fetching record analysis to improve performance and organization and use a more efficient SQL queries, updated the database schemas to efficiently store records and retrieve them by date and limit, enabling more flexible and scalable data retrieval and improving the API's performance, scalability, and usability | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=olesia8novoselova)                                                      |
| Danil Davydyan           | @chocop         | Did CI/CD, made model inference, made additional features in model API's                                                                                                                     | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits?author=Dan1lD)                                                      |

---

### **Plan for Next Week**

#### ML
- Finish emotion recognition model orchestration

#### Frontend
- Do a manual emotion change function
- Collaborate with backend

#### Backend
- Enhance frontend integration
- New user-facing features to edit generated fields
- Expand test coverage for the Go service
- Optimize CI/CD pipeline 

### **Confirmation of the code's operability**

We confirm that the code in the main branch:

- [✓] In working condition.
