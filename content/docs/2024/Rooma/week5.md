---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

- **Feedback collection plan**

  This week, we conducted a thorough feedback collection targeting students from Innopolis University. We chose Google Forms as the primary tool for this survey due to its convenience and accessibility. We solicited feedback based on the following criteria:  

  - **UX/UI Design Rating and User Comments:** To gauge overall satisfaction and gather specific suggestions for design improvements.
  - **Functionality Rating and User Comments:** To understand the performance and usability of the app.
  - **Bugs Encountered:** To identify and catalog issues experienced by users.
  - **Suggested Features:** To gather ideas for potential enhancements to the app.
  - **Additional Comments:** To collect any feedback or observations, not accounted for previously.

- **Conducted user surveys or feedback sessions**

  A total of fourteen students from Innopolis University completed the survey. Although this sample size was limited, the feedback provided significant insights that can drive enhancements to our application. Below is a summary of the feedback received:

<img src="/2024/Rooma/uxui_statistics.png" alt="uxui statistics" width="500"/> 

<img src="/2024/Rooma/uxui_ranking.png" alt="uxui ranking" width="450"/> 

<img src="/2024/Rooma/functionality_statistics.png" alt="functionality statistics" width="500"/> 

<img src="/2024/Rooma/functionality_ranking.png" alt="functionality ranking" width="350"/> 

<img src="/2024/Rooma/bugs.png" alt="bugs" width="450"/> 

<img src="/2024/Rooma/features_comments.png" alt="features and comments" width="450"/> 

- **Analyzing feedback, identifying and prioritizing issues**
  
  Our analysis of the survey responses revealed several key insights:

  - **UX/UI Design Satisfaction:** Most users rated the design highly, with most ratings being 4 or 5. Comments suggested that they found the design aesthetically pleasing.  
  - **Functionality Satisfaction:** In general, users were not highly satisfied with the functionality due to the presence of bugs.  
  - **Bugs Identified:** Various bugs were reported, including:
    - New members take a long time to load in the lobby.
    - Incorrect display of tables in the lobby.
    - Difficulty reading rules from the main page on mobile devices.
    - Issues with customizing Hide-and-Seek settings.
    - Issues with redirecting to some pages.
  - **Suggested Features:** Users proposed new features, including "Tracking players on a map with position updates" and "More games."  

  **Prioritization of Issues:**  
  - **High Priority:** Fixing critical bugs that affect gameplay and user convenience.
  - **Medium Priority:** Enhancing features such as better rules display and faster member loading.
  - **Low Priority:** Adding completely new features and games.

## **Roadmap:**

Based on the feedback received, we have outlined the following roadmap to address the identified issues and enhance the user experience:  
  
- **Bug Fixes:** Fix and resolve all reported bugs. During our app review, the team identified more bugs that require attention.
- **Seamless User Experience:** Ensure the application functions smoothly and meets user expectations.
- **New Features:** Implement suggested features to enhance the application's functionality and usability.
- **Testing:** Work on a comprehensive testing strategy, which includes functional, usability, stress, and regression testing.
- **AI Integration:** Work on integrating AI to analyze and summarize user feedback, providing valuable insights for developers and game administrators.

## **Weekly Progress Report:**

This week, our team focused on the following tasks:  

- **User Feedback Collection:** Collected feedback from our target audience using Google Forms.  
- **Bug Fixes:** Addressed and resolved bugs identified by users and our team.
- **New Functionality:** Added a feedback collection feature to gather user post-game insights.
- **AI Integration Initiation:** Started integrating AI to analyze and summarize user feedback.
- **Testing Initiatives:** Began working on a comprehensive testing strategy, which includes
  - Functional Testing: Verifying that all features work as intended.
  - Usability Testing: Ensuring the app is user-friendly and intuitive.
  - Stress Testing: Evaluating the app's performance under high load conditions.
  - Regression Testing: Ensuring that recent changes have not adversely affected existing functionalities.

### **Challenges & Solutions**

One of the back-end issues was with the state manager. We neglected to include a check for a case where a state object in the database did not exist. This resulted in the redirection of the player to the seeker or hider page being incorrect. The solution was straightforward: include a check.
A significant front-end challenge we are addressing is developing an effective method for displaying occurring errors to users. Currently, errors are being handled without the user's intervention.  

### **Conclusions & Next Steps**

Our team has outlined a strategic plan for future development, which includes several key initiatives. Firstly, we will focus on refining Hide and Seek by addressing remaining issues, enhancing gameplay features, and improving user interface elements to ensure a seamless and engaging experience. Additionally, we will undertake a comprehensive code refactoring process to optimize performance, enhance maintainability, and facilitate future scalability. Looking ahead, we are also exploring the possibility of expanding our game portfolio by developing the second game titled "Facts".  
