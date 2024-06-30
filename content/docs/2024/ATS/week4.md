# **External Feedback**

Currently, we are halfway through the course and the execution of our project plan. In the fourth week, we concentrated on developing our product, which included implementing core features and testing various ideas to ensure functionality and usability. Additionally, we began gathering feedback on our product concept and its beta features. This user input is essential for us to identify strengths and areas for improvement, allowing us to refine and enhance our product as we progress toward the final stages of development.

We conducted a survey among the students of Innopoliss University and obtained the following results:

1. We conducted two live interviews
2. Collected feedback from 8 students using google form

## **Google form statistics:**

![statistics](/2024/ATS/stat1.png)
![statistics](/2024/ATS/stat2.png)
![statistics](/2024/ATS/stat3.png)
![statistics](/2024/ATS/stat4.png)
![statistics](/2024/ATS/stat5.png)
![statistics](/2024/ATS/stat6.png)
![statistics](/2024/ATS/stat7.png)
![statistics](/2024/ATS/stat8.png)
![statistics](/2024/ATS/stat9.png)
![statistics](/2024/ATS/stat10.png)
![statistics](/2024/ATS/stat11.png)
![statistics](/2024/ATS/stat12.png)

## **Conclusion:**

Based on the survey we made the following conclusions:

1. Our target audience is people who already have experience in trading and want to study this area more deeply from the side of AI and trading algorithms as additional tools for prediction and analysis of market behaviour.
2. The majority of respondents preferred a web interface and a mobile application for setting up and interacting with our system. Therefore, in future iterations of the project following the Capstone MVP, we can transition from focusing on the functional components to developing a direct user interaction interface. This will enable users to engage with the project without needing to access or customize the source code themselves.
3. We discovered that we need to enhance our product positioning and work on reducing the entry barrier for using our product.
4. One of the interviewees proposed the idea of trading not on cryptocurrency exchanges, but on exchanges where currency pairs are traded. He believes that in this market, predictive algorithms and AI would yield the highest profits.
5. Most of the respondents find the idea of such a format of investing and trading in ATS mode attractive and interesting to explore.
6. We have been informed that our potential competitors include Freqtrade and Octobot.

# Testing and narrowing the scope of the project

We are now implementing a new system to document our experiments and tests throughout the product development process. Our plan includes creating video recordings of our results to showcase them during our meetings with the TA. Through this approach, we aim to clearly demonstrate our progress and the outcomes of our development efforts.

**What we have tested and what results we have achieved:**

1. Test runs of trading algorithms were executed successfully on the exchange.
2. We established and tested an environment for our AI agent to continue training it using reinforcement techniques.

**ML achivments during testing process:**

**This behaviour of agent before training using reinforcement techniques:**

![statistics](/2024/ATS/ml1.jpeg)

**It's after traning:**

![statistics](/2024/ATS/ml2.jpeg)

# Iteration and refinement

We continue to adhere to our established plan, which includes rigorous iterative planning sessions and frequent team meetings aimed at maintaining synchronization and clarity across all project aspects. This past week has proven pivotal as we engaged in detailed discussions to refine our product vision. By doing so, we have successfully articulated a renewed strategy that aims to position our product effectively within the market landscape.

Additionally, a key focus has been on establishing and maintaining a robust backlog management system. This systematic approach enables us to prioritize tasks effectively based on their importance and urgency. By consistently updating and refining our backlog, we ensure that our development efforts remain aligned with strategic objectives while also enabling us to swiftly adapt to changing project requirements. This proactive management of tasks not only enhances our productivity but also fosters a responsive development environment that can swiftly incorporate feedback and emerging insights from stakeholders and users alike.

## **Progress Report**

### ML component:

**Done:**

- [X] Assembled environments to train the agent
- [X] Tested a simple model without data preprocessing
- [X] Implemented data preprocessing

**Key tasks for next week:**

- Train and compare two agents based on two ideas:

  - The agent is switched on when the price changes sharply (the moment is determined when the threshold is crossed) and is trained only on such moments.
  - The agent is trained on all available data, including the one described above.
- Make visualisation as part of agent comparison
- Cloud storage of training data
- On the basis of the comparison choose a future development strategy for ml module

### Backend component:

**Done:**

* [X] Connected db, create logs when trading
* [X] Created CLI for management
* [X] We connected algorithms to the system that use data from the stock exchange for the last interval.
* [X] Updated README. Added simple documentation for the project

**Key tasks for next week:**

* Try to implement more advanced trade algorithms
* Develop and customise API interface for communicating with ML component
* Improve the trade decision-making mechanism based on algorithms suggestions

### Frontend & Design components:

    Done:

* [X] Dashboard design finilized
* [X] Algorithm comparison screens

Link for final design: [https://www.figma.com/design/01rc3K1AUBfTan3Pw3I8eI/ATS-Mockup?node-id=0-1&amp;t=tQI0KO4DD47yE9Yt-0](https://www.figma.com/design/01rc3K1AUBfTan3Pw3I8eI/ATS-Mockup?node-id=0-1&t=tQI0KO4DD47yE9Yt-0)

Key tasks for next week:

* Create and customise the application in Vue.js, start writing the frontend

### Challenges & Solutions

1. Currently, we are facing challenges with limited feedback and incomplete implementation of key features necessary to effectively showcase our product. To overcome these obstacles, our strategy involves prioritizing the acceleration of feature development to ensure core functionalities are completed promptly. Additionally, we aim to intensify efforts in gathering user feedback, utilizing early-stage prototypes or mockups to solicit insights even before full implementation. This approach will enable us to iterate through testing and refinement phases, focusing on enhancing usability based on early user input.
2. Currently, our project lacks a CI/CD setup for both the backend, frontend, and ML components. In the upcoming fifth week, our plan is to establish an automated testing system and explore transferring the project to a remote server via GitHub Actions to enable offline functionality.
3. Thus far, we have implemented basic trading algorithms that have not yielded the anticipated results. Moving forward, our strategy involves delving deeper into theoretical and scientific realms to identify and incorporate the most promising ideas into future implementations.

# Conclusions

In conclusion, our progress through this phase of development has been marked by significant strides in refining our product vision and strategy. The insights gathered from user feedback have been instrumental in guiding our direction, particularly in shaping our interface preferences and refining our target audience. Moving forward, our focus remains on accelerating feature development, enhancing our testing and refinement processes, and addressing technical challenges to ensure our product meets and exceeds expectations. With continued dedication to iterative improvement and stakeholder collaboration, we are poised to deliver a robust solution that effectively addresses the needs of our market.
