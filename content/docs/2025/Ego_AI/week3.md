# MVP Development. Week #3

## Implemented MVP Features  

For the MVP, we have implemented the core functionalities that will form the foundation of the final product.  

### Backend API  
We designed a PostgreSQL database and a RESTful API to interact with it. During API development, we integrated Google OAuth for seamless login and sign-up functionality. Now, users can join **Ego AI** using their personal Google accounts.  

![Api image 1](https://github.com/setterwars/Capstone-project-2025/blob/main/API_page_1.png?raw=true)

![API image 2](https://github.com/setterwars/Capstone-project-2025/blob/main/API_page_2.png?raw=true)

### Frontend Screens  
For the MVP, we developed four key frontend screens:  

1. **Main Page**  
   The landing page users see upon accessing **Ego AI** for the first time.  

   ![main page](https://github.com/setterwars/Capstone-project-2025/blob/main/DEMO_main_page.png?raw=true)

2. **Registration Page**  
   Features one primary actions: **Sign Up with Google**.  

   ![Registration page](https://github.com/setterwars/Capstone-project-2025/blob/main/DEMO_auth_page.png?raw=true)

3. **Calendar Page**  
   Includes:  
   - A top navigation bar  
   - Weekly task time allocation at the bottom of the navigation bar  
   - A left-side menu for adding tasks, focus sessions, targets, or other work  

   ![calendar page](https://github.com/setterwars/Capstone-project-2025/blob/main/DEMO_calendar_page.png?raw=true)

4. **AI Chat Interface**  
   Allows users to interact with the AI, ask questions, and receive advice.  

   ![AI chat](https://github.com/setterwars/Capstone-project-2025/blob/main/DEMO_AI_chat.png?raw=true)

## Demonstration of the Working MVP  

### Demo in mp4
https://drive.google.com/file/d/1xPhl6JW4ipyOKznf5BJUgksSzRikI2xZ/view?usp=sharing

## Machine Learning (ML) Integration 

We use machine learning to power an intelligent chatbot that helps users explore and refine ideas through interactive conversations. The AI model operates in Grok API mode, ensuring high-quality response handling and smooth communication. Also using Grok you can add some task in your calendar. Currently, speech-to-text conversion is implemented on the backend using Whisper, enabling seamless voice input processing.

In the future, we also plan to enhance the system with AI-powered suggestions for rescheduling. This feature will intelligently analyze user availability and preferences to offer optimal alternatives, making time management more efficient and personalized

## Internal Demo  

When you open the Ego AI website, you will see the home page with all the basic information. This is where you can begin using the service. After that, you should navigate to the sign-up page, which utilizes Google authentication to create your account.

Upon successful registration, you will be directed to the calendar section. Here, you can create tasks, adjust their duration, add discription, and specify when they should occur.
Following that, you can access the AI chat interface. This interface is connected to Grok AI and utilizes the Grok API. If desired, you may log out and return to the home page.

---  

# Weekly Commitments  

## Individual Contributions  

- **Dmitriy Ryazanov**: Test all needed API endpoints, fixed all problems what have arisen, connect backend API with frontend

   **Links:**  

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/6aa44b8bd86624d94a72940fa6cf2e6109cac486

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/6bd99372e18ac83778e654d49ced7124f184cd7c

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/6aa44b8bd86624d94a72940fa6cf2e6109cac486

- **Diana Tsoi**:  She's in the hospital and has legal excuse

- **Stepan Sarantsev**: Integrate API interaction to work with AI chat and spech to text with backend

   **Links:** 

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/aaae85fcdd8c714b3d775894a26e3ab9cc01596e 

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/d1d9dd1b6998858cf8a3856d90aa8c0aa7cd6a72

- **Andrey Zhdanov**:   Create API interaction to work with AI chat and speech to text

   **Links:**

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/8c3e38d8ab6f505c2206bac2aedaacd556e23f24  

- **Artyom Lapin**:  set up hiding passwords and important data from Docker compose.

   **Links:**

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/41c795e688b7453b525ac6e544bdec5a7368d20d

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/5432639e6d17c1ed63096f970a90fe5d7019143b

- **Mikhail Sofin**:  Create AI chat page, refacter all frontend structure

   **Links:**  
   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/8766fca59109f8742abf7f8ce95e8e02b0438ba3

- **Salavat Zaynulin**:  Create registration page, connect Frontend with backend, write report, setup domen using duckdns.org .

   **Links:**  
   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/8b7a46dbf6c1326281f44fd290dcce2dbe2af9c0

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/efb055738441039402c4d2f97a9f5f4ee6633e40

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/76d10e31ede108de175565936e2c471898e16005

   - Link to commit: https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/a3484ebecac81d0bb26289c435fb546afd7a8d0f

## Plan for Next Week  

- Fix bags that are available.

- Create a smart suggestions page.
  - Front-end page for intelligent suggestions.
  - Back-end endpoints.
  
- Minor updates regarding functionality.

## Code Operability Confirmation  

We confirm that the code in the `main` branch:  
- Is fully functional  
- Runs seamlessly via Docker Compose  

---