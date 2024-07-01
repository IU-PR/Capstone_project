---
title: "Week #4"
---

# **Week #4**

## **External Feedback**:

Extensive user feedback was collected from classmates, who represent the initial target audience of students, after testing the chatbot application. The feedback received includes the following points:

1. **Response Issues:** Users experienced a delay when pressing old buttons, giving the impression that the bot is processing something, although it ultimately does not respond.
2. **Email Support:** The application does not support *innopolis.ru* email addresses, only supporting *.university* domains.
3. **User Interface:**
    - The addition of an avatar is recommended.
    - The message *"everything is interrupted, you are at the main menu now"* appears ambiguous when the `/menu` command is activated.
    - A final message at logout is suggested to replace the current message ending with a multi-dot.
4. **Notification Preferences:** Users requested a subscription feature for notifications specific to buildings of interest, rather than receiving notifications for all buildings.
5. **Positive Feedback:**
    - The bot's name is well-received.
    - The system is generally considered user-friendly.
    - The controls are minimalistic and largely intuitive.

### **Planned Improvements**

Based on the feedback, the following enhancements are planned:

- Implement mechanisms to handle invalid messages or clicks to improve user experience and responsiveness.
- Add an avatar to enhance the visual appeal and user interface.
- Extend support to include *"innopolis.ru"* email addresses for user login.
- Revise the response to the `/menu` command to ensure clarity and avoid confusion.
- Introduce a definitive final message at logout, replacing the ambiguous multi-dot message.
- Develop a subscription feature allowing users to opt-in for notifications specific to buildings they are interested in, rather than receiving all notifications.

Future feedback will be solicited from the hostel administration via the admin panel, which will include detailed statistical analysis to further refine and enhance the MoniDorm system.

## **Testing**:

The testing for a Telegram bot was conducted by a potential future users. There were complaints about UX of the bot and we fixed all the problems. By feedback of the users we rethought some  deleting messages with commands. As for testing the API Server database connection, absolutely all methods of working with data using TestContainers have been tested. When running the tests, a virtual environment is created that runs docker containers with PostgreSQL and Liquibase. Migrations to the database are automatically established, and after that the Spring Boot context starts.

## **Iteration**:

During the development process the code base of the bot and the fault detector became too difficult to maintain, so the code was rewritten. This happened at the moment when we created the interface for subscribing to crash notifications — due to the implicit transmission of values by link, a huge number of buttons about disabling notifications could be added endlessly to the keyboard.
After opening a pull request in GitHub, a number of jobs are launched that conduct unit and integration tests on the application, as well as linter that checks the purity of the code and shows errors.

---

## **Progress report**:

For this week we have significant improvements in our project:

- Added handling of incorrect or unexpected messages and button clicks

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/Monidorm/action.jpg">
</div>

- Improved the appearance of the bot profile

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/Monidorm/newui.jpeg">
</div>

- Added *innopolis.ru* mail support

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/Monidorm/regex.jpg">
</div>

- Improved the UX of the dialogue with the bot

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/Monidorm/logout.jpeg">
</div>

- Implemented an algorithm for detecting potential failures
- Implemented notification of users about failures (if they have *"subscribed"* to receive these notifications)
- Implemented a language model to obtain additional information on the failure from user messages
- Rewrited a significant part of the code for its extensibility

This week, we have expanded the set of tests that check the operability of controllers (API endpoints). As for future improvements, we plan to connect SonarQube to lint the code so that it finds all kinds of errors and vulnerabilities.

---
