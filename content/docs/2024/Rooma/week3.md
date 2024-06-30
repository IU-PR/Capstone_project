---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

  To facilitate efficient collaboration and development, we have established a shared environment on GitHub, which is accessible to all team members. We also use Miro to track tasks' progress, make schemas, and define game logic. These tools provide a solid foundation for the development of our first prototype.

- **Backend Development**:

  This week, our back-end developers worked on implementing our first games' (Hide and Seek's) logic and adding functionality such as logout, several game settings, etc. They worked on receiving and sending data on game settings, user information, and others.

- **Frontend Development**:

  Our front-end team has improved and added pages such as game settings, rules, game progress, and others to the UX/UI design for Hide and Seek. The team also has initiated the implementation of the web pages for this game.

- **Data Management**:

  Implementing the Hide-and-Seek game, we have carefully considered the data structure required to store game-related information. We have defined a dedicated collection for storing data, which consists of the following fields:
  - Duration: Integer, representing the duration of the game.
  - Seeker percentage: Integer, representing the percentage of players designated as seekers (from 0 to 100).
  - Comment: Optional string field for additional comments or instructions related to the hiding game (can be set by the game's host).
  - Hiders: Dictionary where the keys are Telegram IDs of players and the values are codes generated for each player. The seeker uses the code to identify a person as found.

- **Prototype Testing**:

  As our front- and back-end developers write code, they perform local unit testing to verify the functionality of individual components and modules. This process helps identify and resolve issues early in development, reducing the likelihood of bugs and errors in the final product.  

  We utilize the Postman for API testing, which allows us to send requests to our application's endpoints and validate the responses. This platform helps us ensure that our APIs comply with the defined specifications and function as expected.  

  Once the prototype is complete, we will thoroughly test it to evaluate functionality, usability, and user experience. We will involve internal and external testers to provide valuable feedback on the prototype's performance, identify any remaining issues, and suggest improvements.

## **Weekly Progress Report**  

This week, we made significant progress in developing our project prototype. We distributed the following tasks:  

- Frontend
  - Design and implement pages for login, game information display, settings selection, QR code game invite, feedback survey, and Hide and Seek gameplay.
  - Improve the previous week's code.

- Back-end
  - Implement the data structure, game logic and statistics of Hide and Seek.
  - Implemented account logout.

- Game Logic
  - Meet to discuss the logic for the Hide and Seek, including rules for starting and ending the game, the game process, rules, information displayed to users after the game ends, and sending feedback on the game.
  
  ![Hide and Seek logic](/2024/Rooma/logic.png)

- AI Integration
  - Discuss the use of AI in the project.  
  We will leverage AI for one of the following functions: matchmaking, chat filtering, or game analytics.

- Documentation
  - **Created API documentation: [Link](http://rooma-games.duckdns.org/api/docs)**, ERD, sequence diagrams, and others to describe the system architecture and functionality.

### **Prototype Features**

- user can authorize via telegram by button with a telegram bot
- user can create a game of Hide and Seek
- user can change the game settings when creating a game of Hide-and-Seek
- user can join the Hide and Seek game by QR code/link provided by the organizer
- user can leave feedback about the past game
- user can play Hide and Seek (not fully realized)
- user can log out of the account by the corresponding button

### **User Interface**

- Our team finalized the design of Hide and Seek, the main app pages, and the telegram bot in **Figma: [Link](https://www.figma.com/design/qw7g4wyOzcCV0dF3UBWqIh/Rooma?node-id=0-1&t=4g1ViXH8PQAYNEjx-0)**

### **Challenges & Solutions**

The main challenge for the team this week was to think through the business logic of Hide and Seek. This process involved defining the rules for the game, how it starts and ends, determining what information will be displayed to users after the game ends, and establishing the feedback process. Another problem we faced was determining the use of AI in our app for future development. In addition to that, we did not have a finalized prototype by the end of the week, as we struggled with managing our time efficiently.  
To overcome these challenges, we employed collective teamwork. We held brainstorming sessions to generate ideas and discuss different approaches. We also created diagrams and flowcharts to visualize the game logic and identify potential issues. We wrote down a pros and cons list for each idea of AI use, significantly shortening the list of options. To finish the prototype before our meeting, our team decided to hold extra meetings in smaller teams to work on developing Hide and Seek on back- and front-end parts.

### **Conclusions & Next Steps**

Our immediate next steps will be:

- Finalize the prototype implementation: This involves completing the remaining front- and back-end development tasks, ensuring the prototype is fully functional and meets all requirements.
- Start implementing AI in games: We will begin by exploring different AI algorithms that potentially apply to our games to enhance the user experience. We will then develop and integrate AI components into the prototype.
- Think about the next game: We will brainstorm ideas for a new game that is engaging and challenging for users. We will also consider incorporating AI into the game to make it more enjoyable.
