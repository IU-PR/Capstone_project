---
weight: 4
bookFlatSection: true
title: "Week #4"
---

# **LearnQuest**

# **Week #4**

Welcome to Week 4 of our Capstone Project! This week is dedicated to the crucial phases of testing, feedback integration, and continuous iteration.

## **Progress report**  


## **External Feedback**
We have received feedback from a survey based on our first prototype in dev environment [here](https://docs.google.com/forms/d/e/1FAIpQLSe4_dGe32kgBBy1LTaD1mpZg3FaW119kB_nNCoxNZNY8eOW3g/viewform). 

The responses we received are displayed below: 

1. ![Result 1](/LearnQuest/survey-result-1.png)
2. ![Result 2](/LearnQuest/survey-result-2.png)
3. ![Result 3](/LearnQuest/survey-result-3.png)
4. ![Result 4](/LearnQuest/survey-result-4.png)
5. ![Result 5](/LearnQuest/survey-result-5.png)
6. ![Result 6](/LearnQuest/survey-result-6.png)

## **Testing**

We have written unit tests for testing our Models, Serializers and Utility Functions in the Django backend. The tests can be viewed on [GitHub repo](https://github.com/abuwho/LearnQuest).

Also, we have conducted end-to-end testing for our API endpoints using [drf-yasj](https://drf-yasg.readthedocs.io/en/stable/readme.html). It helped us identify potential loopholes in the backend request-response model, related to authentication and HTTP response codes. Moreover, it helped us test the robustness of our backend. 

Furthermore, we have conducted end-to-end testing for the frontend components and make relevant changes based on any potentially broken components in the UI. 

During the testing process, we tried to follow the [TDD](https://en.wikipedia.org/wiki/Test-driven_development) guidelines. 


## **Iteration**

Based on the feedback received from the [survey](https://docs.google.com/forms/d/e/1FAIpQLSe4_dGe32kgBBy1LTaD1mpZg3FaW119kB_nNCoxNZNY8eOW3g/viewform), we have added some features to develop after the release of our MVP by the end of the course. 

Key features include: 
1. Adding Russian payment gateways such as (Mir, Yoomoney, SberPay, etc.)
2. Feature to gift a course to a friend
3. Free trial

However, it is important to note that abovementioned features will be implemented after the release of the MVP for future iterations. 
