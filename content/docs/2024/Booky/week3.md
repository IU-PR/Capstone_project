# Week 3 Progress Report

## Overview of Week Work
In Week 3, we focused on hands-on development to create the first functional prototype of our project. This involved setting up the technical infrastructure, developing both backend and frontend components, managing data, and conducting initial rounds of testing.

## Technical Infrastructure

### Server Side
- **Setup:** Created and set up a virtual machine and S3 in cloud.ru.
- **Tools:** Installed Docker, PostgreSQL and Go.
- **Access:** Only the backend developer needs direct connection due to their expertise in cloud infrastructure, while other team members have basic knowledge.

### Development Infrastructure
We ensured all team members have access and basic skills in the following tools:
- **Figma:** Used for UI/UX design and creating diagrams.
- **Blue Stack:** Used as an emulator for simplifying app testing and showcasing.
- **VScode:** Used for code writing.

## Backend Development
- **Architecture:** Developed with gRPC API architecture.
- **Protobuf File:** Created and initialized the Interface Definition with CRUD (Create, Read, Update, Delete) operations for courses and notes(posts).
- **Implementation:** Completed the implementation of these CRUD operations and dockerized the application.

## Frontend Development

### Basic Design
- **Initial Development:** Developed a basic design to construct a prototype for testing user experience and layout.
- **Tools:** Used standard components extensively from the [Material Design Kit](https://www.figma.com/community/file/1035203688168086460) to speed up the process.
- **Screens:** Developed 8 screens covering all basic functionalities by the end of the sprint.

### Design Implementation in Flutter
- **Parallel Development:** Started implementation in parallel with design development, ensuring there was material to work with after a 1-day delay.
- **Project Structure:** Organized code into strict categories to follow the DRY (Don't Repeat Yourself) principle.

#### Project Structure:
```
├───common
│   ├───app_colors.dart
│   ├───constants
│   └───widgets
├───features
│   ├───courses
│   │   ├───data
│   │   │   └───bloc
│   │   │       └───courses_cubit
│   │   ├───screens
│   │   └───widgets
│   ├───notifications
│   │   └───widgets
│   ├───post
│   │   ├───domain
│   │   │   ├───entities
│   │   │   └───enums
│   │   └───presentation
│   │       ├───screens
│   │       └───widgets
│   └───settings
└───proto
    ├───client
    ├───generated
    └───server
```

- **Progress:** All 8 screens were implemented with stubs for client-server connection by the end of the week.

## Data Management
- **Focus:** Kept the functionality simple but ensured it worked perfectly.
- **Setup:** Created a basic PostgreSQL database with tables for courses, notes, and course-note relations. Also set up an S3 Object storage bucket.

## Prototype Testing
- **Backend Testing:** Conducted by our tester using Postman, which revealed 5 bugs.
- **Frontend Testing:** Manually tested by team members on their phones and emulators. Identified 5 design implementation bugs and 2 device compatibility issues.

## Progress Report

### Prototype Features
- **Implemented Features:** 
  - Backend CRUD operations for courses and notes.
  - Basic frontend screens covering essential user interactions.
  - Data management with basic database operations.

### User Interface
- **Screenshots and Interactive Prototypes:**
  - **Video:** [View here](https://drive.google.com/file/d/1fgwClSIwMEs-9S5SJZ9FiywMyTBEOKvB/view?usp=sharing)
  - **App Download:** [Download here](https://drive.google.com/file/d/1n-mI9r7-kLTUig6l4tPsV2vzkg5IOEae/view?usp=sharing)

### Challenges and Solutions
The main challenge this week was quickly implementing working prototype parts and starting to test them. Our team had significant time management issues.

#### Designer
- **Challenge:** Starting layout from scratch.
- **Solution:** Overcame 'blank paper' fear by inspecting [Material 3 Foundations](https://m3.material.io/foundations), using the [Material 3 Design Kit](https://www.figma.com/community/file/1035203688168086460), and searching Pinterest for references.

#### Frontend
- **Challenge:** Layout issues in extreme test cases.
- **Solution:** Conducted bug-fixing sessions with the frontend developer and designer to improve performance.

- **Challenge:** Establishing gRPC connection between server and user.
- **Solution:** Worked collaboratively to resolve connection issues.

## Conclusion
This week, we successfully developed and tested the first functional prototype of our project. We encountered and overcame several challenges, and we are now well-positioned to refine the prototype and continue development in the coming weeks.

### Next Steps
For the next week, we plan to:
- Conduct a survey about prototype user experience.
- Improve user interface based on survey feedback.
- Implement changes in frontend.
- Connect the app with backend CRUD operations for files.
- Fix the client-server connection issue.
- Conduct functional testing, write a checklist.