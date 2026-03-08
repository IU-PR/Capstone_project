# Week 4 Testing, CI/CD & Deployment Setup

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

# Frontend

**Responsible:** Dziyana Melnikava, Anastasia Kuchumova

Link to frontend contribution: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/frontend)

- Unit tests for critical frontend components are wtitten.
- Component for Analysis Output enhanced according to new ML model.
- Authentication is established.
- Feedback component was created.
- Main and User Profile pages are created.
- Custom calendar is implemented.

### Unit Testing Areas

#### 🎤 _AudioRecorder Component Tests_

- **Initial UI Rendering:**  
  Ensures microphone icon (MicIcon) is visible on initial load, verifies that recording controls like "Pause" or "Stop" are not displayed unless recording starts.
- **Permission Denied Banner:**  
  When microphone permission is 'denied', the component shows a warning icon and an alert message: "Microphone access is blocked".
- **Active Recording State:**  
  Shows recording controls (Pause, Stop icons) and the recording timer when recording starts.
- **Post-recording Loading State:**  
  Displays a loading message indicating voice recording is being analyzed.
- **Save/Delete UI After Recording:**  
  When `audioBlob` exists (indicating recording finished), the component shows Save and Delete buttons with corresponding labels.
- **Delete Confirmation Trigger:**  
  Clicking the delete icon triggers the `handleDeleteClick` function, initiating delete confirmation.
- **Stop Recording Action:**  
  Clicking the stop icon calls the `stopRecording` function, verifying the stop recording interaction.

#### ⭐ _FeedbackWidget Component Tests_

- **Initial Render:**  
  Renders the feedback question and instruction text.
- **Display of Rating Options:**  
  Verifies all rating buttons with emojis and labels are displayed.
- **Submitting a Rating:**  
  Checks that clicking a rating calls the `onSubmit` handler with the correct value.
- **Thank You Message After Submission:**  
  Confirms the thank-you message appears and the question disappears after rating submission.
- **Hover Effect on Ratings:**  
  Applies active CSS class when hovering over a rating button.
- **Hover Leave Effect:**  
  Removes active CSS class when mouse leaves a rating button.

#### 📊 _RecordingCard Component Tests_

- **Rendering Behavior with Null Result:**  
  Verifies that the component renders nothing when the `result` prop is null.
- **Full Rendering with Valid Result:**  
  Checks that all main sections (emotion, summary, insights, coping strategies, recommendations, footer) render correctly for a valid `result` object.
- **Emotion Pill Styling:**  
  Tests that the emotion label displays with the correct CSS class depending on the emotion type (positive, negative, aggressive, neutral).
- **Rendering Multiple Key Triggers:**  
  Confirms that multiple key triggers are rendered correctly when present in the data.

#### 🌊 _WaveAnimation Component Tests_

- **Audio Initialization on Recording Start:**  
  Verifies that when the component mounts with `isRecording=true`, it requests microphone access (`navigator.mediaDevices.getUserMedia`) and creates an `AudioContext`.
- **Graceful Handling of getUserMedia Errors:**  
  Simulates permission denial or error during microphone access request and confirms that the error is caught and logged via `console.error` without crashing.
- **Animation Frame Cleanup on Unmount:**  
  Confirms that ongoing animation frames requested via `requestAnimationFrame` are properly cancelled on component unmount to prevent memory leaks or unnecessary processing.

### ✅ Test Cases

<table>
  <tr>
    <td><img src="https://downloader.disk.yandex.ru/preview/0fb96366ef0e256d64862c3d15e561d7fdc829f9068c428457046e809982edbc/6865b6c8/wcF0dk2E3bvzMgUR04qo6jAuwZ533WXZLe4wXS7ARiGEoOUFIPYDosM3kfZDdO-tTKBOoY-PziGX1bbSqL1ulw%3D%3D?uid=0&filename=%D1%822.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v3&size=2048x2048" alt="Example of test" width="400"/></td>
    <td><img src="https://downloader.disk.yandex.ru/preview/b1d90d966b49691d1d5283530ea3a9984fa6859c1806959770ffdde3d0781d06/6865b6dc/zn1AfdIgDKreRC3dVfDT6DAuwZ533WXZLe4wXS7ARiELENlTBUq6vXwMJArX5AnWCL4coH2bizoVE4PpECnZfA%3D%3D?uid=0&filename=%D1%821.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v3&size=2048x2048" alt="Example of Test" width="400"/></td>
    <td><img src="https://downloader.disk.yandex.ru/preview/8ea6840333491888baa52953b9ad6dcd59dec86cc85b94c7e22997a12cbe47af/6865b705/Z_LeqfhBtFv_l9hugNpgjzAuwZ533WXZLe4wXS7ARiGTGghyrv4N08fC-E572v_PhrViKDdy_I3pXMqYnfaszQ%3D%3D?uid=0&filename=%D1%823.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v3&size=2048x2048" alt="Example of Test" width="400"/></td>
  </tr>
  <tr>
  <td><img src="https://downloader.disk.yandex.ru/preview/e22e376ebcf5d8521ddb943d1477d71e52969746e5f814ce6efd3880631a2a31/6865b71e/piiY6rcRVDBnoNRF8sviiTAuwZ533WXZLe4wXS7ARiH1WYr7BlGbr77zn4USDZfEqeDJJkwYVXt-tl9ACGjieg%3D%3D?uid=0&filename=%D1%824.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v3&size=2048x2048" alt="Example of Test" width="400"/></td>
    <td><img src="https://downloader.disk.yandex.ru/preview/e46b7156c341fc45cdb70a1ca756224f1f89eef894ae8be613b4899b7512e0b4/6865b72b/CG9M-lhs8Mfzvxv460u7nzAuwZ533WXZLe4wXS7ARiFScSUbm2TUDClz3V0OhzPxadI1Ccad_SzUQreSDE5tZw%3D%3D?uid=0&filename=%D1%825.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v3&size=2048x2048" alt="Example of Test" width="400"/></td>
  </tr>
</table>

---

# Backend

**Responsible:** Olesia Novoselova, Danil Davydyan

Link to backend contribution: [CLICK TO SEE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/backend)

- User authentication implemented using HTTP-only cookies with a 30-day expiration period.
- Secure password handling added: user passwords are hashed at the service layer before storage.
- Unit tests written for critical service and repository logic.
- Integration tests developed for key API endpoints to verify end-to-end functionality.
- CI/CD pipeline and Docker Compose setup completed for streamlined development and deployment.

### Unit & Integration Testing Areas

#### 🔑 _Authentication & Session Management Tests_

- **User Registration:**  
  Verifies that new users are registered with hashed passwords and stored securely in the database.
- **User Login:**  
  Ensures users can log in with valid credentials, and receive a secure HTTP-only session cookie.
- **Session Validation:**  
  Checks that endpoints requiring authentication reject requests with missing or invalid session tokens.

#### 🗄️ _Service & Repository Layer Tests_

- **User Service:**  
  Tests user creation, password hashing, session creation, and user retrieval by login or session token.
- **Record Service:**  
  Verifies saving, fetching, and retrieving records by user and record ID.
- **Repository Functions:**  
  Ensures correct SQL operations for users, sessions, and records, including error handling for not found and constraint violations.

#### 🌐 _API Integration Tests_

- **/users/register:**  
  Confirms successful registration and error handling for duplicate users.
- **/users/login:**  
  Validates login flow, session cookie issuance, and error responses for invalid credentials.
- **/me:**  
  Checks that authenticated users can retrieve their profile info, and unauthenticated requests are rejected.
- **/records/upload:**  
  Tests file upload endpoint for authentication and correct error handling.
- **/users/:userID/records & /records/:recordID:**  
  Verifies correct responses for valid, invalid, and non-existent users/records.

#### ⚙️ _CI/CD & Deployment_

- **CI/CD Pipeline:**  
  Automated testing and deployment pipeline configured for backend service.
- **Docker Compose:**  
  Multi-service orchestration for backend, database, and ML service for local development and

### ✅ Test Cases

Test Cases output is available here: [CLICK HERE](https://drive.google.com/drive/folders/1XaDl73E1A1z2ue4P0-vPcvI5K4ALenYq?usp=sharing)

---

# ML

**Responsible:** Dzhamilia Fatkullina, Elina Kuzmichyova

Link to ML contribution: [CLICK HERE](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/ml)

---

## Individual commitments

---

| Team member              | Telegram alias  | Contribution                                                                                                                                                                                  | Link                                                                                                       |
| ------------------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Dziyana Melnikava (Lead) | @meldilen24     | Write part of report, implemented new Analysis Output and Feedback components, established authentication                                                                                     | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=meldilen)            |
| Anastasia Kuchumova      | @n_rngk         | Created Main and User Profile pages, implemented custom calendar, wrote unit tests                                                                                                            | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=Ann24-02)            |
| Dzhamilia Fatkullina     | @jam11a         | Researched psychological feedback models, researched locally hosted llms capable of extracting key insights, implemented insight extraction, tested prompts                                   | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=DzhamiliaFatkullina) |
| Elina Kuzmichyova        | @lin_anile      | Researched models for emotion recognition from text and approaches to multimodal emotion recognition (based on text and voice)                                                                | [Link](https://github.com/IU-Capstone-Project-2025/VoiceDiary/tree/main/ml/models/experimental)            |
| Olesia Novoselova        | @doiwannaknoww8 | Implemented user authentication using HTTP-only cookies with a 30-day expiration period, added secure password handling, wrote unit tests, developed integration tests for key API endpoints. | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits/main/?author=olesia8novoselova)   |
| Danil Davydyan           | @chocop         | Set up CI/CD Pipeline, set up Docker, integrate new ML model to backend                                                                                                                                                                       | [Commits](https://github.com/IU-Capstone-Project-2025/VoiceDiary/commits?author=Dan1lD), [Worlflow](https://github.com/IU-Capstone-Project-2025/VoiceDiary/blob/main/.github/workflows/tests.yml)                    |

---

### **Plan for Next Week**

#### ML

- Do emotion recognition model orchestration
- Conduct research on additional feature models

#### Frontend

- Improve UI/Ux
- Implement new features that will be introduced by ML team
- Collaborate with backend team on connecting calendar to database

#### Backend

- Implement logic for loading users' avatars
- Modification of the go->python contract for more optimal use of ml models and easier deployment
- Setting up the test environment

### **Confirmation of the code's operability**

We confirm that the code in the main branch:

- [✓] In working condition.
