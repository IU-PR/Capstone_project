---
title: "Week #4"
---

# **Week #4**

## **External Feedback**

Over the past week, we made a concerted effort to collect valuable feedback from friends and colleagues about our
desktop application. To make the process efficient and respectful of everyone's time, we utilized Google Forms. This
form featured various rating options for different functionalities of our application, allowing users to rate each
feature on a scale of 1-10 and provide additional comments if they chose. You can find the form
[Here](https://forms.gle/M3eoJdfNbbahjobx9)

The feedback we received was incredibly insightful and highlighted several important issues that required prompt
attention. For example, one user noted that "The image preview delays noticeably when navigating between photos." We
addressed this issue after receiving the feedback. Another user mentioned, "...
too much space for sidebars or between folders and groups." Recognizing the significant impact this had on
user experience, we prioritized and going to fix this issue. Additionally, feedback regarding the UI provided us with
crucial insights that led to further enhancements.

In summary, gathering direct feedback from users has proven to be extremely valuable. It brought several key issues to
our attention and provided us with essential insights for future enhancements. We will ask users to test our
application once more, to see how the fixes of the application have improved or worsened the opinion
of our user in order to create the most User-friendly application

## **Testing**

Prior to integrating the machine learning components, we conducted several days of testing to ensure the stability of
the selected model. After this we have started integrating the model into the desktop application and testing it
accordingly.

This thorough testing phase allowed us to identify and resolve issues and bugs in various areas such as database
integration, UI blocking during model loading, and improper image loading. Moreover, it provided us with valuable
insights on how to effectively work with future models that will be incorporated into our application.

Moreover, every contributor of our project had testing session, to find all bugs, new ideas and suggestions in an
organized manner. This approach allowed us to find and fix some errors with the connection of the database with the
application, as well as flaws in the UI

## **Iteration and Refinement**

### **Iterations with UI**

We conducted several iterative cycles to gather feedback and identify flaws in our User Interface. The external feedback
we received was invaluable, providing us with critical insights that greatly informed our improvements. As a result, we
were able to significantly enhance the User Interface, addressing key areas of concern.

Furthermore, we took this opportunity to reassess our overall goals and functionality. By doing so, we were able to make
thoughtful adjustments, ensuring that our UI not only resolved the identified issues but also aligned more closely with
our overarching objectives. This holistic approach has allowed us to create a more intuitive and user-friendly
interface, ultimately enriching the user experience.

### **Iterations with UX**

All team tested UX of the application and we found several bugs with database. We partially resolved the issues, but
this part needs to be improved. We will continue testing and iterating to succeed in a user-friendly UX

### **Iterations with models**

Throughout the development process, we encountered numerous bugs while connecting the model to the application. Despite
these challenges, we successfully resolved the issues and rigorously tested the functionality. As a result, the desktop
application is now fully operational, offering complete functionality of the blur-detection model.

## **Weekly Progress Report**

### **User Interface improvement**

As we mentioned before, we spend a lot of time to find and resolve issues in the UX/UI. External feedback also was
really helpful for this stage
Here you can see example of UI improvement, first screenshot old version and second new variant:
![First image](/2024/A-Shot/week04/UI-upd/old.png)
![Second image](/2024/A-Shot/week04/UI-upd/new.png)

As you can see on this example, we removed the large, awkward gaps of the sidebars. The selection box has also 
been converted to numbering with a color selector. Moreover, we have replaced the unnecessary demonstration of 
pictures in the group on the right sidebar with a neat slide bar

### **Database integration**

We integrated Room database into our product this allowed us to remove the unnecessary loading of directories into our
application every time the application is restarted. Now, when the directory is downloaded for the first time, it gets
into the database and needs to be downloaded again only in case of an update

### **Frontend Development**

We continued to develop the frontend of our application, meticulously enhancing it to address various UI issues and
improvements. This ongoing development process allowed us to refine the visual and interactive aspects of the interface,
ensuring a more seamless and engaging user experience. By implementing UI fixes and making strategic adjustments, we
have significantly elevated the overall design and functionality of our application’s frontend.

### **Testing**

All team participated in the testing phase of the product. This was useful for different views on certain details of
the product.

### **Challenges & Solutions**

- **Challenge 1: Build project on our machines**  
  *Problem*: Package did not include correctly to the system, so we can't build our application
  *Solution*: We spend some time to search problems and create ultimate guide for the installation

- **Challenge 2: Analyze feedback and improve UI**  
  *Problem*: Users and we as contributors were not happy with the interface to a greater extent
  *Solution*: We brainstormed the issues, searched for interesting UI-solutions and make more user-friendly interface

### **Conclusions & Next Steps**

- **Beta-testing**: We want to contact more people, to give them access to the beta-test of our product. We will ask
  them to test and analyze functionality of the product and provide feedback. This way may give us more insights and
  help to identify any flaws
- **Dark Theme**: As the instrument for the photographers, A-Shot in dark theme might be useful to a lot of people,
  because a dark theme may put less strain on the eyes in the evening or at night than a white one. Moreover, it is much
  more
  convenient for the human eye to look at photos on a dark background than on a light one
- **Multiplatform deploy**: In plans to adaptive the application to the Windows and MacOS
