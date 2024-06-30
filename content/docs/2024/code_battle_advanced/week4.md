---
title: "Week #4"
---

# **Week #4**

## **External Feedback**

Leaving only the key feedback points, we have gathered several issues:

- The color scheme of the site left several testers plenty unsatisfied. 

- There is no way to scroll the web application in pages where there are more entries that fit on a page.

- Some of the most crucial pages are not decorated and are impossible to use without guidance

- Several buttons are not working.

- The field for time selection is very inconvenient as it requires entering the exact date and time by hand in a fixed format.

- Lack of control over an existing contest.

- Why does it say “Already have an account? Sign up” on the sign up page

- Why is the Login button labeled “Get started”

- The descriptions on everything make all contests and tasks take up way too much space and are not friendly to users that are used to a concise interface.

- The page where the task is supposed to be looks severely broken.

- We really should add [LaTeX](https://ru.wikipedia.org/wiki/LaTeX) to our tasks so that the equations are not that ugly

We knew about most of these issues, but some of them were new to us, although, after further consideration it was apparent that they were, in fact, problems that needed addressing. Some of these new feedback points include scrolling, because in all our tests we did not bother adding more content to the website, and the fact that it did not work came as a surprise to most of us. Another interesting suggestion was to incorporate LaTex into our tasks, but we’ve yet to figure out how.

## **Testing**

For our testing we have concluded that the current functionality is not sufficient to test any user-end characteristics in any meaningful ways, as the project is in a stage of active development and we knew most of the issues raised since they are blatantly obvious. However, we have found several critical errors and missing functionalities that were not mentioned by our guests, such as:
 
- Re-uploading the task every time there is a minor change is tedious at best.

- The logo on the contest and task pages does not lead to the main page.

- The task archive and publicly available contests should be available for everybody, not just logged-in users.

It is safe to say that fixing both reported and tested problems is our main priority for the upcoming week.

## **Iteration**

After receiving the feedback from our guests we have highlighted the regions of improvement and will be dividing the foregoing tasks to refine the working parts and fix the broken ones. Our team is constantly enhancing the project using the iterative method, but other than stating this very fact, there is very little to be said.

We are planning to iterate through our current design, since that was a major point that we got from feedback. Additionally, we plan to improve contest management to make it more user-friendly and feature-complete, with the ability to customize contests by adding custom buttons, text and images into the contest. Furthermore, we need to develop more content for the website itself, as there is very little to test with as of now. Moreover, we need to better our cybersecurity, as the current stance leaves the system vulnerable to attacks from all sides. 

For the current state of the project, please refer to the [Github repository](https://github.com/IU-Capstone-Project-2024/code-battle-advanced).

### **Challenges & Solutions**

1. When making a java testing code I could not create a java code for A + B. Embarrassing, but at least I learned about BigDecimal and its applications.
2. When testing java it took a lot of time to realize where the issues are from my part and where the functionalities are simply malfunctioning. Makes for some bonding time though.
3. Inattention to project updates(working on secondary branch and forgetting about the primary one) led to substantial code corrections: the two works have been made on a single code snippet that caused inability to merge both changes into one, afterwards realizing a specific work done by a teammate did not bring any benefits as the other work already covered all the issues tackled by this code part.
4. The code file that manages contest-participant data (i.e. how many points the contestant has, are there any effects active) was initially planned to be loaded from the database at each place where it was needed, bringing in a plethora of issues such as race conditions and general bloating concerns. This is why we decided to move all operations relating to the management of contests to a separate container and talk to it via [gRPC](https://grpc.io/). 
5. While merging every team members’ work together, several issues arose in that the tables did not have the same fields as the page to upload tasks was renewed to have more fields. We should avoid changing the format of the database in the future, and include the work to bring every change into the unified format into the task itself.
6. It is very time-consuming to write pure CSS for a constantly changing website, so we decided to finalize the pages and focus on improving their design.

### **Conclusions & Next Steps**

This week our team gained valuable insight from the feedback, which should pull this project towards a better user-experience, which is one of the main goals. The mistakes and shortcomings will be mitigated and fixed in the upcoming weeks. 


So, as a plan for the week we plan to work on the said issues and also add some contests and tasks for them. The latter should make us interact with the system, so that we could test it and understand sides for future development.
