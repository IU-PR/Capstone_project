# Practicum Project  
PALTUS team. Report 5

## Feedback

1. Course Creation & Editing  
   - Allow expansion of subtopics to include presentations, homework, or additional materials.  

2. UX Features
   - Clarify validation rules (e.g., "A proper topic is required") to guide users.  
   - Improve annotations/instructions for users unfamiliar with the system.  
   - Optimize the platform for mobile devices (currently not supported).  

3. Knowledge Base & AI Enhancements  
   - Integrate a knowledge base for the AI model to generate more complete courses.  
   - Allow manual editing/expansion of AI-generated courses.  
   - Implement a service to improve user prompts (beyond basic validation).  

4. Interactive Learning Features  
   - Add quizzes to assess user knowledge retention.  

5. User Account & Security  
   - Implement user registration (done this week).

### Google Drive folder with screenshots of exact feedbacks

[Screenshot folder in Google Drive](https://drive.google.com/drive/folders/1nARhMYD_WLm-qb310XpuCgS5_8i0zZuA?usp=sharing)
  

## Iteration & Refinement

### Implemented features based on feedback
1. Quizzez are currently in progress.
2. Authorization and regstration are done on this week.
3. Editing course right after its creation feature is donne on this week.
4. An ability to edit subtopic using LLM model.
5. An ability to add notes as user is added.

### Performance & Stability
- Course creation time - 9,98 sec.
- Course removal time - immediate.
- User feedback (overall level of satisfaction) - 2 people out of 6 were not satisfied.
- Course editing time metric - to be measured.
- GPT answer time - to be measured.

### Documentation
README file is the only documentation.

### ML Model Refinement
The prompt we use is changing in a good way to satisfy the conditions and expectations we need.

## Weekly commitments

### Individual contribution of each participant

- Sergey Knyazkin
  - [Rewrite requests for authorization](https://github.com/IU-Capstone-Project-2025/PALTUS/pull/40).
  - [Authorization and registration requests](https://github.com/IU-Capstone-Project-2025/PALTUS/pull/40).
  - [Add notes to subtopics](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/e490be3977f1bcfeeb0522c637d6c43a920f96a5)
  - [Add modal to fix course](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/824d0bb71071e3a4abc031dd5933aa1c8ff1d2d7)
  - [Add text-area component](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/92a3dd56276753c0c5563650bff2a543fb981c85)
- Ramazan Gizamov
  - [Awards page layout and styling](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/ef5086d95b640fffa40d14d1be58c48aa862ba71).
  - [Quiz page layout and styling](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/a33cb1efedb0fc8a8e3d4b90f06a3bee11fa7c6c).
  - [Report for week 5](https://github.com/poeticlama/PALTUS/new/master/content/docs/2025/PALTUS/week5.md).
  - [Collected feedback](https://drive.google.com/drive/folders/1nARhMYD_WLm-qb310XpuCgS5_8i0zZuA?usp=sharing).
- Aidar Sarvartdinov
  - [Fixed the same user is not duplicated when registering again](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/d045100ee10a020d279ce204b6d7862d95844784).
  - [Fixed   exclude JwtFilter from ExceptionLoggingAspect to avoid proxying](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/6edea8645efa833f9434d2eb2d903781b93fa199).
- Igor Dubrovsky
  - [Base content generation](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/321896aca1e0c7430e017f080188447c94b24df2).
- Amir Fayzullin
  - [Fixed tests](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/1492366198120431bc02dd71f990179c05f6580b).

## Plan for Next Week

### *Frontend*
- Error Displaying.
- Validation.
- Quizzes.
- Gamification.

### *Backend*
- Quizzes.
- Gamification.
- GPT interaction.
- Daily streak.


## Confirmation of the code’s operability

We confirm that the code in the main branch:
Run via docker-compose.
