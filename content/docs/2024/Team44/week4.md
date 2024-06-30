
# **Week #4**

## **External Feedback**

We aimed to collect feedback from our colleagues and friends on the prototype, which initially focused solely on the ML model for quiz generation due to ongoing backend and frontend connection issues. Our friends graciously assisted in testing our model, providing valuable insights.
Firstly, we asked our two friends from our course to test our program. They had to send their notes and get the answers for them. One of them used the book part from the "Database" course, while another sent us some notes from the " Introduction to MLOPs " course. They evaluated the relevance, conciseness, and waiting time of our quizzes.
For instance, the first respondent evaluation is below:
"The quiz generator for "Intro to MLOps" aligns strongly with provided content, scoring 9/10 for question relevance. It effectively covers key topics such as machine learning challenges, MLOps versus DevOps distinctions, and MLOps goals. While generally clear and concise, with an 8/10 for question conciseness, some answer choices could be clearer. With a generation time of 49.6 seconds, it performs adequately but could benefit from optimization for quicker output. Minor adjustments to refine answer clarity and enhance speed would further improve the quiz's effectiveness in assessing MLOps principles."

Another friend of ours also said some words about our program:

"The quiz generator scores 8/10 for relevance, effectively covering key database concepts like redundancy and storage, but could benefit from more detailed questions. It rates 7/10 for conciseness, generally clear but with some overly lengthy answer choices. It's efficiently optimized with a quick generation time of 19.5 seconds (9/10), though further speed enhancements could be considered. Improvements in front-end engagement and back-end optimization for faster performance would enhance the quiz generator's user experience and overall quality."


Based on feedback from our colleagues and friends, our quiz generator prototype shows strong alignment with the content for both "Intro to MLOps" and database courses, scoring well in relevance and efficiency metrics. To enhance its effectiveness further, we will focus on refining answer clarity, optimizing generation speed, and improving user engagement through front-end enhancements. These adjustments aim to elevate our quiz generator's overall quality and user experience as we continue development.

## **Testing**
Testing throughout the project has been rigorous and thorough. We have focused on ensuring all implemented features' functionality, reliability, and performance. Comprehensive testing has been conducted for each endpoint in the back end, utilizing automated tests to validate correct operation under various scenarios. This approach has allowed us to identify and address issues promptly, ensuring a stable and efficient application.

## **Iteration**
Our iterative process is driven by feedback from user testing groups and ongoing evaluations. Based on this feedback, we prioritize improvements such as enhancing the clarity of answer choices, optimizing backend processes to improve performance metrics (such as reducing quiz generation times), and refining the front-end user interface to enhance engagement and usability. Additionally, we are actively developing a summarization model to expand the application's capabilities. These iterative steps aim to continually enhance the application's functionality, user experience, and educational effectiveness.


## **Progress reports**  

### Machine Learning
Significant progress was made in deploying and configuring models. Asynchronous processing was researched, and information was gathered for future implementation.

### Back-end
In the back end, we connected all the requests that the front end can make, including implementing the email verification endpoint /authentication/api/email-verify, fixing the sign-out endpoint to work with an empty POST request, updating the sign-in endpoint to no longer return a token with Django managing authorization, and requiring login for the /quiz and /summary endpoints. Additionally, we completed basic tests for all endpoints, changed the sign-out request to a GET with an empty body, and clarified that the sign-up process now requires users to verify their email to log in without revisiting the sign-up endpoint after email verification.

### Frontend
Due to some illness issues with our front ender, Ivan, we had some braking on our front part. However, we will catch up in time and finalize our work. Also, we will help him facilitate this process by helping him divide the tasks from our side. Contacting each other more often is vital so such issues can be decreased.

On the front, we are aiming to add email verification functionality by routing the **signup token** from /authentication/API/email-verify?uid=*uid*&token=***token*** to the backend (user will receive this link on their email). Additionally, we will connect all the existing endpoints from the backend. We also decided to use Google's open-source Materialize framework for CSS for a simple, convenient, and responsive UI. During the next week we will need to add more UI elements to ensure full functionality of our app.

### Summary
We made significant progress across multiple fronts in our recent development cycle. We are working on deploying and configuring the models in machine learning while preparing for future asynchronous processing capabilities. All front-end requests are integrating the back-end, including implementing email verification, refining sign-in and sign-out functionalities, and enforcing login requirements for critical endpoints like /quiz and /summary, alongside comprehensive endpoint testing. The front end saw advancements with the integration of email verification and the adoption of Google's Materialize framework for enhanced UI responsiveness. Looking forward, our focus shifts to developing a summarization model and expanding UI elements to meet our next MVP goals, with plans to iterate based on user feedback to enhance overall application functionality and user experience.