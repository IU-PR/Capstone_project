---
weight: 1
bookFlatSection: true
title: "InnTime"
---

# **Week #1**

### **Team Members**

| Team Member            | Telegram ID   | Email Address       |
|------------------------|---------------|---------------------|
| Nikita Grigorenko      | n1kgrigorenko | n.grigorenko@innopolis.university  |
| Evgeny Gerasimov       | dzendos       | e.gerasimov@innopolis.university   |
| Boris Zarubin          | Poseidondon   | b.zarubin@innopolis.university     |
| Vladimir Ryabenko      | Vldmr11       | v.ryabenko@innopolis.university    |
| Insaf Yusupov          | yuzsx         | i.yusupov@innopolis.university     |
| Ivan Chebykin          | doechon       | i.chebykin@innopolis.university    |
| Makar Vavilov          | Prudens       | m.vavilov@innopolis.university     |


### **Value Proposition**

**Identify the Problem:**
- The main problem of the existing shedule is the difficulty of finding the right schedule for a particular group. In case of many electives and subjects which students want to choose for the semester it is hard to find a propriate schedule for individual student. The bottleneck of the existing google sheets schedules is not comfortable search of the study year, main group #, electives and group of the electives.  

**Solution Description:**
- Our project will allow you to simply upload existing Google tables with a schedule. And make your schedule for each group, subgroup, and each selected elective. All this will be displayed on the website. And then the end user can simply select his group, electives, and groups of electives. The schedule administrators will also be able to make changes to it. For example, to change the room for a class or to change its time. However, the main difference of our tool will be the following thing: the administrator will be able to simply enter a new event in the field in any form. Our tool will understand by itself what information to get from there and where to insert it into the schedule. Secondly, the compiled schedule can be exported to Excel or Google format.

**Benefits to Users:** 
- Thanks to the use of our tool, the user will be able to reduce the time of searching and drawing up their schedule, especially in those semesters when electives exist. Moreover, an administrator (for example, a professor) will be able to easily make changes to the class schedule and they will be displayed in real-time. Also, many people like to make their schedules in Google or Excel format. Our solution will do it for them.

**Differentiation:** 
- Users should prefer our solution to others because our solution offers the ability to export schedules in Google and Excel format. And also easily make changes to the schedule without using unnecessary telegram channels or bots. However, the project itself will bring convenience to viewing the schedule at the university.

**User Impact:** 
- Students will be able to get their full schedule faster. And also export it in a convenient format for further editing. However, now teachers do not have to spend a lot of time searching for a specific chat to warn students about changes in the schedule. All this will be done on one site.

**User Testimonials or Use Cases:**
- In our course, some people often try to make a schedule themselves so that it is more convenient to use it. Moreover, many complain that the schedule is quite inconvenient in the format presented. Therefore, we decided to make a project that will make a schedule for you.


## **Lean Startup Questionnaire**

1. The project solves the problem with the existing schedule at the university. Thanks to the project, it will become much more convenient and faster to work with a schedule.
2. Students and Instructors.
3. When we have the prototype of the project ready, we will be able to test the beta version of the project on some students.
4. The number of students and instructors who will use it.
5. After receiving the user's comment, we need to get together as a team and discuss and analyze his comments. To understand whether his remarks make sense or not. If so, we will fix it.


## **Leveraging AI, Open-Source, and Experts**

- **AI (Artificial Intelligence):** We are going to use AI to write small pieces of code that take time, but do not require mental investment.
- **Open-Source:** We can use open sources for any large projects to gain knowledge about elegant solutions to problems. And also to simplify writing code (not to reinvent the wheel)
- **Experts in relevant domains:** There are people in our circles who work in the areas that we will use in our project. Therefore, for additional information that can help us add some new tools to our project, we can refer to them.


## **Inviting Other Students**

- We are going to survey students to clarify points regarding the usability of the current schedule. We will also ask them what they want to see in the new tool, and what are the requirements for it. And what they think is superfluous. After creating a prototype, we will invite several students to test our project. We will wait for feedback from them.

## **Defining the Vision for Your Project**

- **Overview:** Our project provides students and instructors with a schedule that can be easily found on one site, without using multiple telegram groups, tables, and so on. The user will be able to easily specify their groups, and electives and see a ready-made schedule for him, as well as export it to Google or Excel format. Our project solves the problem of speed and ease of use of the existing schedule. You don't have to look for a schedule in different places and open incomprehensible tables every time. Also, the schedule can be updated in real-time directly on the website, so that instructors do not have to write information somewhere in different places every time. As a benefit for users, our project provides the ability to quickly schedule in one place, as well as make changes in real-time.

- **Schematic Drawings:**

- *Flow of the Project*
<div class="wrapper" style="display: flex; justify-content: left; align-items: center;">
    <img src="/InnTime/graph.png">
</div>

- *Structure of the Project*
<div class="wrapper" style="display: flex; justify-content: left; align-items: center;">
    <img src="/InnTime/architecture.png">
</div>

- **Tech Stack** For our project we choose the next list of the languages and frameworks:
    - Backend: Python
    - Frontend: HTML, CSS, JavaScript, React
    > ***Scalability***:
    React's component-based architecture makes it easy to modularize the code and build reusable UI components. Because it is the main one on the market, it is supported by Facebook (which, by the way, is extremist in the territory of the Russian Federation). This is a library and it is lightweight compared to the Angular framework. A huge community around the world. React cross-platform (react native for mobile phones) 
    JavaScript has a large ecosystem of libraries and frameworks.
    HTML provides a clear structure to the web pages, making it easier to maintain and update them as needed.
    Python has a large ecosystem of libraries and frameworks that can be leveraged to add new functionality to the application as needed.
    >
    > ***Performance***:
    React's virtual DOM allows it to efficiently update only the parts of the page that need to be changed, resulting in faster rendering times.
    JavaScript's event-driven architecture allows for asynchronous processing, which can further improve performance by preventing the browser from becoming unresponsive.
    CSS can be optimized for better performance through techniques such as minification and compression.
    >
    > ***Security***:
    React's use of a virtual DOM can help prevent certain types of attacks, such as cross-site scripting (XSS).
    JavaScript has built-in security features, such as strict mode, that can help prevent common security vulnerabilities.
    HTML and CSS provide a clear separation of content and presentation, which can help prevent certain types of attacks, such as SQL injection. 
    Python has a built-in set of security features, including modules for encryption, hashing, and secure socket communication.
    Python's strong type checking and error handling features can help prevent common security vulnerabilities, such as SQL injection and cross-site scripting (XSS).
    >
    > ***Ease of development***:
    React's declarative programming model makes it easier to reason about your code and can lead to fewer bugs.
    JavaScript's dynamic typing and flexible syntax make it easy to write and modify code quickly.
    HTML and CSS are easy to learn and use, and provide clear guidelines for structuring and styling web pages. 
    Python's large standard library and extensive third-party package ecosystem provide many pre-built tools and solutions for common problems, further accelerating development.
    Python's interactive shell and support for functional programming paradigms make it well-suited for rapid prototyping and experimentation.

- **Anticipating Future Problems:**
    > ***Technical complexity:*** The project involves parsing multiple tables and displaying them in a unified format on a web page. Depending on the structure and formatting of the tables, this process could be quite complex. Additionally, real-time editing functionality will require careful consideration of concurrency issues.
    Mitigation strategy: we can break down the project into smaller, more manageable tasks and implement them incrementally. also use best practices for database design and table parsing to ensure a robust and scalable solution. And test the project early and often to identify and address any concurrency issues.
    >
    > ***Resource limitations:*** The project may require significant server resources in case of updating information and saving the schedule for each user. 
    Mitigation strategy: we can try to develop the application using a scalable architecture that can accommodate growing user numbers over time. Also, we need to consider using cloud-based hosting services that allow scaling up or down based on demand.
    >
    > ***Also, it can be hard for us to parse the Excel tables into one database. In case of that, we need to read more information in this field and ask experts about it.***

- **Elaborate Explanations:**

    We have two main critical components in the project: 
    1. Parsing tables into usable format for the database
    2. Real-time updates could lead to concurrency issues

    **Core functionalities of the project:**

    >***Table parsing:*** The project's core consists of a set of algorithms that can combine the data from several tables into a single format. No matter how many tables are there, this capability enables users to examine their schedules in real-time.

    >***Group selection:*** The program gives users the option to choose their favorite study group, thereby enhancing the user experience. This function selects the pertinent information from the parsed tables and only shows what is crucial to the chosen group.

    >***Selection of electives:*** Choosing electives for each study group is another project component. Students can select available electives for their specific degree using this function and add them to their timetable.

    >***Real-time editing:*** The program also enables users to make changes to their schedules in real-time. The database is automatically updated and stored whenever the schedule is modified. All users have easy access to current information thanks to this feature.
    

    **Unique technologies:**
    
    >Real-time updates and real-time editing that is completely connected with data saving are two unique features of this system. Our Schedule project is the perfect option for students who want to efficiently arrange their time because it also makes it simple to filter by groups and electives.
