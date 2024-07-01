---
weight: 4
bookFlatSection: true
title: "Week #4"
---

# **Week #4**

Welcome to Week 4 of the Capstone Project! This week is dedicated to the crucial phases of testing, feedback integration, and continuous iteration. As you embark on iterative development on your projects, it is essential to understand the significance of these processes in ensuring the delivery of a high-quality, functional product that aligns with your original vision.


## External Feedback
Based on a survey conducted with 10 participants, including our classmates and parents, we have gathered the following statistics regarding the satisfaction and usability of our Telegram bot that creates weekly menus based on user preferences:

### Survey Statistics

**Overall Satisfaction**

- Very Satisfied: 2
- Satisfied: 5
- Neutral: 2
- Unsatisfied: 1
- Very Unsatisfied: 0

Insight: 70% of participants were either very satisfied or satisfied with the overall performance of the bot.

**Preference Accuracy**

- Very Accurate: 1
- Accurate: 5
- Neutral: 3
- Inaccurate: 1
- Very Inaccurate: 0

Insight: 60% of participants found the bot to be accurate or very accurate in matching their preferences.

**Ease of Use**

- Very Easy: 6
- Easy: 4
- Neutral: 0
- Difficult: 0
- Very Difficult: 0

Insight: 100% of participants found the bot to be very easy or easy to use.

**Recipe Variety**

- Excellent: 3
- Good: 6
- Fair: 1
- Poor: 0
- Very Poor: 0

Insight: 90% of participants rated the variety of recipes as good or excellent.

**Recipe Quality**

- Excellent: 3
- Good: 4
- Fair: 2
- Poor: 1
- Very Poor: 0

Insight: 70% of participants rated the quality of the recipes as good or excellent.

**Customizability**

- Very Satisfied: 1
- Satisfied: 4
- Neutral: 3
- Unsatisfied: 2
- Very Unsatisfied: 0

Insight: 50% of participants were satisfied or very satisfied with the customizability options of the bot.

### Suggestions and Improvements
**Enhanced Algorithm Customizability**: Some users expressed dissatisfaction with the current customizability options. To address this, we will focus on making the algorithm more adaptable and responsive to user inputs, allowing for better personalization of the menus.

**Preference Matching**: To increase the percentage of users who find the bot very accurate or accurate in matching preferences, consider implementing more sophisticated algorithms or user feedback loops to fine-tune the preference matching.

**Recipe Quality and Variety**: Although already rated highly, continuous updates and expansions of the recipe database will help maintain and improve the satisfaction levels concerning recipe variety and quality.

### General Feedback
Participants have provided positive feedback overall, particularly highlighting the bot's ease of use and the variety of recipes. However, there is a clear indication that improvements in customizability and preference accuracy would further enhance user satisfaction.

### Conclusion
The survey indicates that the Telegram bot is well-received by most users, with high marks in ease of use and recipe variety. While overall satisfaction is positive, focusing on improvements in customizability and preference accuracy can drive even higher satisfaction rates. The feedback suggests a strong foundation with opportunities for refinement to better meet user needs and preferences.

## **Testing**
Our testing approach will include the following aspects:

- **Integration testing**: Verify the seamless communication and data exchange between the Telegram bot, the server, and the database. This includes testing scenarios where the bot sends requests to the server, the server processes the requests and interacts with the database, and the database responds back to the server, which then relays the information to the bot.

- **Functional testing**: Ensure that the Telegram bot is functioning as expected, handling user inputs, and providing the desired responses. This could involve testing various user commands, error handling, and the bot's ability to fetch and display information from the server and the database.

- **Performance testing**: Assess the system's ability to handle a large number of concurrent users or requests, and measure its responsiveness and scalability under different load conditions. This could include stress testing the system to identify any bottlenecks or potential points of failure.

- **Security testing**: Evaluate the system's security measures, such as user authentication, authorization, and data encryption, to ensure that the sensitive information stored in the database is protected from unauthorized access or manipulation.

- **End-to-end testing**: Simulate the complete user journey, from interacting with the Telegram bot to the data being stored and retrieved from the database, to validate the overall system's behavior and ensure that it meets the specified requirements.

## **Iteration**
The foundation of a successful project's development is constant iteration. This week, we deployed our API and bot, marking a significant step in our progress by managing to deploy our service on university virtual machine. Additionally, we started implementing an algorithm for generation of an optimal menu, which will consider calorie counts and the complexity of the menu. To enhance user experience, we improved the bot’s functionality for a more user-friendly interface by improving the connectivity between bot functions and making usage of bot more comfortable. In addition to these significant upgrades, we fixed a few small bugs in the bot's code. These iterations demonstrate our dedication to improving our product in response to suggestions and findings from testing. 
Next week, our focus will be on completing the optimal menu generation algorithm and adding a feature to allow users to mark recipes as favorites. This iterative process guarantees continual improvement and adaptability to user requirements and feedback in addition to assisting in bringing our solution closer to the original concept.

---
## **Progress reports**
### **Development progress**
This week, we deployed our API and bot on the university's virtual machine. We started implementing an algorithm for optimal menu generation, considering calorie counts and menu complexity. We enhanced the bot's functionality for a better user experience and fixed minor bugs. Next week, we aim to complete the menu algorithm and add a feature for users to mark recipes as favorites.
### **Challenges & Solutions**
While integrating various files with the Telegram bot's functions, we encountered significant compatibility issues among its components. These challenges required a careful review of the system design and specific solutions to ensure everything worked together smoothly. Additionally, the algorithm that creates menu sometimes produced excessively large amounts of certain ingredients, which complicated the process. To solve this, we thoroughly analyzed the algorithm's settings and made necessary adjustments, improving the accuracy and efficiency of the FindRecipe bot's operations.
### **Conclusions & Next Steps**
We are focused on improving the quality of our Telegram bot and enhancing the functionality of our algorithm. Currently, there are several key tasks for the algorithm: ensuring that the menu adheres to a specified calorie limit, minimizing the number of ingredients used, and making sure that lunch foods are not suggested for breakfast. These tasks are crucial for refining the bot's performance and delivering a more user-friendly experience.
