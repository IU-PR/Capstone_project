---
title: "Week # 1"
---

# Match&Watch: Project Report for Week 1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member          | Telegram ID    | Email Address                   |
| -------------------- | -------------- | ------------------------------- |
| Team Member (Lead) 1 | @LouayFarah    | l.farah@innopolis.university    |
| Team Member 2        | @KaramKhaddour | k.khaddour@innopolis.university |
| Team Member 3        | @LaithNayal    | l.nayal@innopolis.university    |
| Team Member 4        | @aymendaassi   | m.daassi@innopolis.university   |
| Team Member 5        | @SaleemAsekrea | s.asekrea@innopolis.university  |

#### **Value Proposition**

- Identify the Problem:

  The problem is that most people struggle with selecting a movie or series to watch as they are faced with an endless selection whenever they open a streaming platform.

- Solution Description:

  Our solution, "Match&Watch", is a website that analyses a person's or group's current mood through a personal profile, a questionnaire, and/or other interactive methods. It then uses AI to suggest movies, series, or anime based on the analysis.

- Benefits to Users:

  Users will save time and avoid the frustration of scrolling through endless options. They will receive personalized recommendations that match their current mood and preferences.

- Differentiation:

  Unlike other recommendation platforms, "Match&Watch" takes into account the current mood of the user, making our recommendations more personalized and accurate. Also, the website will store past user preferences to help decide on a better suitable pick in the future.

- User Impact:

  The impact on users will be significant. They will be able to make quicker decisions about what to watch, leading to less frustration and more enjoyment. The personalized recommendations will also enhance their viewing experience, as the watchers will be more thrilled to discover the proposed picks for the first time.

- User Testimonials or Use Cases:

  1. Individual User: John had a rough day at work and is in a bad mood. He logs into "Match&Watch", answers some random life situation questions, and the website suggests a comedy series that is known for its uplifting and humorous content. John starts watching and finds himself laughing and forgetting about his tough day.

  2. Family User: The Smith family, including two children aged 8 and 12, want to watch a thrilling movie that is suitable for all ages. They use "Match&Watch" and based on their inputs, the website suggests a thrilling adventure movie that is rated PG. The Smith family watches the movie together and enjoys a thrilling yet family-friendly movie night.

## **Lean Questionnaire**

1. What problem or need does your software project address?

   Our website addresses the problem of decision fatigue and time wasted when trying to choose a movie or series to watch.

2. Who are your target users or customers?

   Our target users are individuals, children, couples, families, or anyone who enjoys watching movies, series, or anime and wants personalized recommendations.

3. How will you validate and test your assumptions about the project?

   We will validate and test our assumptions about the project through user testing and feedback. We will create a minimum viable product (MVP) and have a group of beta testers (mainly fellow students and family members) use our service. We will collect their feedback and use it to validate or invalidate our assumptions. Additionally, we will use A/B testing to compare different features and see which ones perform better.

4. What metrics will you use to measure the success of your project?

   We will use several metrics to measure the success of our project. These include the accuracy of our recommendations (measured through user feedback), user retention rate (how many beta testers continue to use our service over the next 6 weeks after trying it first), and technical metrics like precision, F1 score, and recall. Finally, we will implement load and stress tests using k6 in order to assure the envisioned performance of our website in a concurrent environment.

5. How do you plan to iterate and pivot if necessary based on user feedback?

   We will continuously collect user feedback from the course team, through surveys, and user testing sessions. If we find that a feature is not working as expected or if users express a need that our service is not currently meeting, we will iterate on our product by making necessary changes. If user feedback indicates a need for a major change in direction (pivot), we will reassess our user stories and make the necessary adjustments.

## **Leveraging AI, Open-Source, and Experts**

Our team plans to leverage AI, open-source software, and domain experts in the following ways:

- **AI (Artificial Intelligence):** We will use AI to analyze the user's mood and preferences from their profile and questionnaire responses. Moreover, AI is our main tool to classify the client's current mood based on his answers, his personal profile, and hist past preferences. Finally, We will use a ML model that is responsible for selecting the pick (movie, series, or anime) based on the classfication by training it on a public dataset from a well-known source (imdb or kaggle for example).
- **Open-Source:** We will leverage open-source software to speed up our development process and build upon the work of others. This includes using open-source libraries and frameworks for web development, machine learning, and data analysis. For example, we could use a pretrained public ML model and tune it for our own purposes.

- **Experts in relevant domains:** We will seek advice mainly from the course team. We could also read some research papers to get a deeper understanding of our topic, especially in the classification with AI part.

## **Defining the Vision for Your Project**

- Overview:

  "Match&Watch" is an innovative website designed to solve the issue of decision fatigue when choosing a movie, series, or anime to watch. By leveraging AI, we analyze a user's current mood and preferences, gathered through a personal profile and a unique questionnaire. This allows us to provide personalized recommendations, saving users time and enhancing their viewing experience. Our project stands out by considering the user's current mood, making our recommendations more personalized and accurate. The intended benefits for users include quicker decision-making, less frustration, and more enjoyment from watching content that aligns with their mood and preferences. Stakeholders, such as streaming platforms and content creators, could also benefit from our service by gaining a better understanding of viewer preferences and improving user engagement.

- Tech Stack:

The project work will be divided into 3 main parts:

1. Frontend (UI): We will use the Vue.js framework to develop a simple interface for inputting user data, preferences, and answers; and showing the selected picks after running the selection and classification model(s) on the backend and applying filters if used.

2. Backend Microservice: In general, we will be using FastAPI Python framework for implementing the RESTFul API, and Postgres as a relational database management system.

3. Machine Learning: We will use Pythong language and some of its popular libraries like Keras, tenserflow, and scikit-learn for training the necessary models.
