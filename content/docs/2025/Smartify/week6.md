---
title: "Week #6"
---

# **Week #6**

---

# Links

- [Deployment](http://213.226.112.206:22025)
- [Swagger documentation](http://213.226.112.206:22025/swagger/index.html)
- [Design](https://www.figma.com/design/7D72pnxGyyRk9lh58vzCFY/Smartify?node-id=0-1&p=f&t=ifQCyMjOgBWRaDFr-0)
- [Demo](https://drive.google.com/drive/folders/1NXxsR6Fa9s7O0JoYjUtntHd4RsM2u29l?usp=sharing)
- [Presentation](https://docs.google.com/presentation/d/1xDfDES4q_WClc6Rm1P2zCx-SJXgj_lXOmnvMENQyY1U/edit?usp=sharing)

# Project overview 
Smartify is an educational platform for Russian high school students that helps them choose a profession, choose the right university, prepare for the Unified State Exam, and find a tutor. The main feature is the use of artificial intelligence for personalized recommendations that make the path to admission clear and accessible.

The platform offers four main page. In the career guidance page, students complete a questionnaire indicating their interests, academic performance, and hobbies. Based on the answers, the system suggests specific professions, immediately indicates the necessary subjects for admission and explains why this profession is suitable.

The university selection page allows you to filter universities by region, form of study (budget/fee) and direction. It is possible to compare universities by passing scores, tuition fees and rating.

The ЕГЭ preparation page offers a list of necessary subjects depending on the chosen profession and university, forms an individual curriculum, contains built-in mini-tests and a progress tracker.

The tutor page allows you to search for teachers by subject, teaching style (friendly, strict, etc.), as well as view detailed profiles with information about education and experience.

Since our project is quite large and difficult to fully implement in 2 months, we plan to continue working on it and maintain

---

# Features

# 🟨 Frontend

## 1. 🔐 Authentication

### Registration (Multi-step)
- **Email validation** with confirmation code
- **5-digit code input** (via `pin_code_fields` package)
- **Password strength check**:
  - Minimum 8 characters
  - Must include digits and special symbols
  - Strength visualization with color indication

### Password Recovery
- Full cycle:
  - Reset request → code verification → new password setup
- Data validation at each stage

## 2. 🧭 Main Interface

### Navigation
- Transitions between main sections:
  - Universities, Exams, Careers, Tutors
- **Side menu with SlideTransition animation**

### Responsive Design
- Fixes for overflow issues and text wrapping
- **Clickable cards** with visual effects (`InkWell`, hover animations)
- **Mobile layout optimization**

## 3. 📊 Data Management

### JSON Handling
- Parsing:
  - `professions.json`
  - `spheres_stats.json`
- Filtering logic:
  - Spheres → Sub-spheres → Professions

### Global Search
- Dynamic filtering of professions
- **Search result highlighting**

### Databases
- Initial implementation of the **university list**

## 4. 📝 Questionnaire

### Dynamic Loading
- Parsing of DOCX/XML files using `archive` and `xml` packages

### Question Types
- Single / multiple choice
- Scales (1–5 / 1–7)
- Text fields (e.g., "Other")

### Validation
- Required field checks
- Smart suggestions
- Default values for sliders

## 5. 🎯 Recommendation Page

### Display
- **Large cards** for top 3 recommendations
- **Compact adaptive cards** for the rest
- Sections:
  - Pros
  - Cons
  - Description
- **Color-coded blocks**
- **Field mapping** using `subsphere`

## 6. 🗂️ Profession Navigation

### Hierarchical Structure
- Spheres → Sub-spheres → Professions
- **Parameterized navigation**

### Detailed View
- Unified `ProfessionCard` component
- Section-based content layout
- **Bulleted lists** for key characteristics

## 7. ⚙️ Technical Solutions

### State & Animations
- State management via `StatefulWidget` / `setState()`
- Smooth transitions, hover animations

### Optimization
- **Data preloading**
- **JSON caching**
- **Dynamic lists** via `ListView.builder`

## 8. 🌐 Localization

- `app_localizations_en.dart`: English translations added
- `app_localizations_ru.dart`: Russian translations added

---

# 🟦 Backend

### 1. 🔐 **User Authentication and Login**  
- Secure sign-in and authentication flow for users

### 2. 🧭 **Data Storage in MongoDB**  
- Persistent storage of specific user or app data using MongoDB

### 3. 📊 **Data Storage in PostgreSQL**  
- Relational data storage for structured information

### 4. 📝 **Access and Refresh Tokens**  
- Token-based authentication for secure session management

### 5. 🗂️ **Local Data Storage with SharedPreferences**  
- Lightweight key-value storage for client-side data persistence

### 6. 🎯 **Secure Token Storage on Client**  
- Storing access and refresh tokens using secure storage mechanisms

### 7. ⚙️ **Client-Side University Data as Files**  
- University data stored locally on the client as static files

### 8. 🌐 **Multiple API Endpoints for Communication**  
- RESTful endpoints for structured client-server interaction

### 9. 🔐 **Access Token Refresh Flow**  
- Automatic renewal of expired access tokens using refresh tokens

### 10. 🧭 **Backend Dockerization**  
- Containerized backend services using Docker

### 11. 📊 **Initial Data Loading on Backend Startup**  
- Automated import of data from files into the database during initialization

### 12. 📝 **CI/CD Deployment to Public Server**  
- Continuous integration and delivery pipeline for deployment to a public IP server

### 13. 🗂️ Tutor parser  
- Automated extraction of tutor information from structured or unstructured sources

### 14. 🎯 Parallel tutor parsing and MongoDB upload  
- Simultaneous parsing and storage of tutor data in MongoDB for performance optimization

### 15. ⚙️ ML integration with backend  
- Connecting machine learning modules to the backend for predictions or intelligent features

### 16. 🌐 User data tracking and server-side storage  
- Secure storage of user-specific data such as progress trackers on the server

---

# 🟥 ML

### 1. 📊 The code outputs the pros and cons of a suitable profession
### 2. 📝 Writes the percentage of match
### 3. 🎯 Displays a description of the profession, the sphere and the subsphere

---

# Tech stack

# 🟨 Frontend

**Main Framework:**  
Flutter — cross-platform development for Android, iOS, and Windows.

## Key Dependencies

- `percent_indicator`: for displaying progress indicators  
- `intl`: for internationalization and localization  
- `pin_code_fields`: for PIN code input fields  
- `archive` and `xml`: for working with archive files and XML data  
- `flutter_secure_storage` and `shared_preferences`: for secure and local data storage  
- `cupertino_icons`: for iOS-style icons

## Development Tools

- `flutter_test`: for unit and widget testing  
- `flutter_lints`: for static code analysis  
- `flutter_launcher_icons`: for generating app launcher icons

## Data & Resources

- **Static files:**  
  - JSON files for universities and professions  
  - DOCX files for tests and documents  
  - PNG and JPG images for visual assets

- **Localization:**  
  Handled using the `intl` package.

---

# 🟦 Backend

## Programming Languages
- **Go**
- **Dart**
- **Python**

## Key Libraries and Frameworks

### Go
- **Web & API:** `net/http`, `encoding/json`  
- **Databases:** `database/sql` (for SQL), `mongo-go-driver` (MongoDB), `github.com/lib/pq` (PostgreSQL)  
- **Web Scraping:** `github.com/PuerkitoBio/goquery`  
- **Security:** `golang.org/x/crypto/bcrypt`  
- **Standard Library:** `context`, `log`, `fmt`, `os`, `time`, `errors`, `regexp`, `strings`, `strconv`


### Python
- **Web & API:** `json`, `fastapi`

## Databases

- **SQL**  
  - PostgreSQL  
  - Driver: `github.com/lib/pq`

- **NoSQL**  
  - MongoDB  
  - Driver: `mongo-go-driver`

## Containerization and Automation

- **Docker** — containerization of applications  
- **Docker Compose** — multi-container orchestration and service management  
- **CI/CD** (GitHub Actions / GitLab CI / Jenkins) — automated build, test, and deployment pipelines  
- **YAML** — configuration language for Docker Compose and CI/CD workflows  
- **Shell scripting** — automation scripts within Dockerfiles and CI/CD pipelines

---

# 🟥 ML

## Programming Language

**Python (3.8)**  

**Used for:**  
- Core data processing logic  
- MBTI type determination (`determine_mbti`)  
- Profession scoring (`score_profession_normalized`)  
- Recommendation generation (`process_student`)

**Libraries:**  
- `json`: For reading and writing JSON files (e.g., `dataset_career_test.json`, `professions.json`, `profession_recommendations.json`)  
- *Potential additional libraries:*  
  - `pandas`: For working with structured data (students, professions)  
  - `numpy`: For advanced numeric and statistical operations (e.g., normalization)

## Data Format

**JSON**  

**Used for storing:**  
- **Student data** (`dataset_career_test.json`):  
  Includes `mbti_scores`, `subject_scores`, `interests`, `values`, `work_preferences`, and `exclude`.

- **Profession data** (`professions.json`):  
  Includes fields like `sphere`, `subsphere`, `name`, `description`, `ege_subjects`, `mbti_types`, `interests`, `values`, `role`, `place`, `style`, `education_level`, `salary_range`, and `growth_prospects`.

- **Recommendation results** (`profession_recommendations.json`):  
  Includes `name`, `score`, `positives`, `negatives`, and `description`.

**Advantages:**  
Lightweight, human-readable format ideal for data exchange between systems and easy local processing.

## Database

**File-based storage (JSON)**  

**Current implementation:**  
All data is stored and managed in JSON files, which is suitable for small-scale projects and local data processing.

---

# Setup instructions

Clone repository locally:
   ```sh
   git clone https://github.com/IU-Capstone-Project-2025/Smartify.git
   ```
Starting the app:
   ```sh
   cd Smartify/frontend
   flutter run
   ```

---

# Weekly commitments

## Individual contribution of each participant

## 🎨 UX/UI

Responsible - **Kuchukbaeva Regina**
 - Privacy policy page
 - Redesign the professions page
 - Page with individual profession

✅ Related artefacts:
- [Figma](https://www.figma.com/design/7D72pnxGyyRk9lh58vzCFY/Smartify?node-id=0-1&p=f&t=ifQCyMjOgBWRaDFr-0)
- [Privacy policy page](https://github.com/IU-Capstone-Project-2025/Smartify/issues/113)



## 💻 Frontend

Responsible - **Chugaeva Mariia**

- Custom logo display
- Fixed the main menu page
- Fixed bugs in the questionnaire field
- Updated the recommendations page
- Added the spheres_page.dart page 
- Added the subspheres_page.dart page
- Redesigned the professions page has been redesigned
- Updated the design of the cards on all pages
- The application form button is available from each stage of the profession

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/139)


Responsible - **Zakirov Karim**

- University cards
- Tracker and calendar
- The page with tutors
- Multilingualism
- Dark theme

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/141)



## 🛠️ Backend

Responsible - **Mayorov Daniil**
- Documentation for all endpoints in the Swagger
- The ability to save trackers on the server
- The ability to download trackers from the server
- Connected everything to flutter so that everything worked on the application
- Side guides, updated the login logic, now the tokens are still stored on the server before logging in

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/140)


Responsible - **Antipov Alexey**
- Uploading questionnaires to the client
- Visualize which tables we have in PostgreSQL
- Visualize mongodb
- Parsing of tutor profiles

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/140)



## 🤖 ML

Responsible - **Andruwenko Valery**
 - Added 14 areas of work 
 - Added sub-spheres for all areas
 - 347 professions now, will be increasing

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/142)



## 📥 Project Management 

Responsible - **Basanov Maxim**
 - Establishing communication between each participants in the Telegram
 - Emerging problem solving, meetings organization
 - GitHub repositories, Backlog and all documentation maintaining
 - Demo recording
 - This report writing

✅ Related artefacts:
- [Backlog](https://github.com/orgs/IU-Capstone-Project-2025/projects/2)



## Future plans

### 🛠️ UX/UI

- Keep the design of the our project beautiful and modern even after the end of the Capstone

### 🛠️ Frontend
- According to the Figma-design, keep the frontend-part of the our project beautiful and modern even after the end of the Capstone

### 🛠️ Backend

- Maintain the project and deployment in a working state

### 🛠️ ML

- Improve MLs metrics 
- Expand all DB



## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
