---
title: "Week #3"
---

# Week #3

## **Developing the First Prototype, Creating the Priority List**

### **Technical Infrastructure**

This week, we focused extensively on organizing our technical infrastructure:

- **Server Setup:** Rented a VDS server for deploying our machine learning and backend systems.
- **Access Rights:** Assigned appropriate access rights to team members responsible for these areas.
- **Training:** Conducted a session on navigating the Azure interface.
- **Frontend Infrastructure:** Established collaborative frontend development on Vercel.

We use a shared GitHub repository with different branches for various parts of the project (backend, frontend, machine learning). For data storage, we utilize a team Supabase workflow with a schema for user and conversation storage. Azure AI Studio resources are used to deploy serverless, auto-scalable open-source models and to store a vector database containing entries for different psychological techniques.

### **Backend Development**

Significant progress was made this week:

- **Integration:** Successfully connected the frontend chat interface with the large language model (LLM), enabling seamless communication between users and the AI.
- **Deployment:** Deployed the LLM on Azure AI Studio for robust and scalable hosting.

### **Frontend Development**

Our goal was to research and practice Next.js and start implementing the frontend by creating the dialogue page:

- **Research:** Conducted thorough research on Next.js, though there’s still more to learn.
- **Implementation:** Began structuring the dialogue window based on our research.
- **Challenges:** Faced difficulties with Next.js concepts, folder structure, and the `npm run dev` command. The whole team is working on resolving these issues.

### **Data Management**

Focused on implementing user registration using Supabase:

- **Security:** Supabase’s Row Level Security (RLS) ensures secure data access control.
- **Database Setup:** Initial setup designed to handle MVP feature set operations like user registration, data retrieval, and storage.

### **Prototype Testing**

Developed an AI psychologist Telegram bot, but due to user concerns about data security, we shifted to a web version:

- **Issue:** Encountered random errors with the bot’s keyword detection, causing unnecessary alarms.
- **Action:** Investigating the bot’s keyword detection algorithms and considering more sophisticated context analysis to prevent such errors.

![Bot test failing with the word “die”](/2024/ClearMind/screen_error.png)

### **Weekly Progress Report**

#### **Prototype Features**

Developed two important features this week:

1. **User Registration:** Created designs for the user registration page.
2. **Request Nature:** The model determines if a user issue is critical (e.g., life-threatening).

We search our vector database for the most suitable psychological technique based on user details. Using ML, we select a technique and refer to the RAG system for more information to reduce hallucinations and communicate effectively with users.

#### **User Interface**

- **Progress:** Created the welcome page with options for login, history of dialogs, etc.
- **Design:** Developed desktop and mobile designs, including a logo.
- **Redesign:** Redesigned previous interfaces to integrate login options.

- [Figma Design](https://www.figma.com/design/UwyAJLNxMfAARTkEx9Oril/ClearMind?node-id=0-1&t=1th8qwylMWuXTb1f-1) for mobile and desktop versions.
- [Website](https://clearmindai.ru) with the deployed dialog page; other pages are being implemented.

### **Challenges & Solutions**

1. **Therapy Methods:** Conceptualizing the implementation of therapy method selection was challenging. We hypothesized storing diagnoses in a vector database to match user inputs with existing data.
2. **Authentication Integration:** Redesigning the interface for authentication integration was challenging. We overhauled the design for secure user login without compromising usability.
3. **Next.js Understanding:** Research for better conceptual clarity helped us grasp the framework and apply it effectively.

### **Conclusions & Next Steps**

This week, we focused on developing the first prototype and creating a priority list. The technical infrastructure was set up, and significant progress was made in backend and frontend development. Data management and prototype testing were key focus areas, with ongoing efforts to address keyword detection issues.

**Next Steps:**

- Refine and test the AI model for accurate issue categorization.
- Improve the keyword detection algorithm to eliminate false alarms.
- Implement user login and secure data management in the frontend.
- Continue developing the user interface based on feedback and testing.
- Plan for integrating additional features and functionalities in the next development phase.
