# Conducting User Surveys and Feedback Sessions

## Feedbacks

From the very beginning of the product development, we actively conducted
interviews to explore the needs and preferences of the target audience. In the
early stages, we conducted two custdevs with end users and an interview with the
administration of Innopolis University.

### Feedback collection plan

For our product, we have identified two primary groups, each of which plays an
important role in the development and success of our project:

1. **End Users (Students)**:
   - **Who**: Students and others who will potentially live together in some
     place (e.g., dorms or co-living spaces).
   - **What we want to know**: User experience, including product usability,
     functionality, overall satisfaction, and identification of problems and
     suggestions for improvement.

2. **Customers (Administration)**:
   - **Who**: Owners and managers of dormitories or other residential facilities
     (e.g., co-living spaces, dormitories, etc.).
   - **What we want to learn**: Understanding how to facilitate deals. This
     includes identifying the administration's needs, their expectations of the
     product, and the factors that influence their buying decisions.

Now let's talk about methods for gathering feedback and key questions for each
of these target audiences.

1. **End users (Students)**:
   - **Interviews and face-to-face meetings**: Conduct meetings and interviews
     to deeply understand the user experience.
   - **Online Surveys**: Distribute surveys to students and other end users to
     gather quantitative feedback on various aspects of the product.
   - **Social media and forums**: Create discussions in targeted groups to
     gather qualitative feedback and suggestions.

2. **Customers (Administration)**:
   - **Interviews and Meetings with Administration**: Conduct meetings and
     interviews to understand the administration's needs and expectations.
   - **Surveys and Questionnaires**: Develop surveys for the administration to
     identify factors influencing their buying decisions.
   - **Analyzing Current Deals**: Examine successful and unsuccessful deals to
     identify patterns and improve the sales process.

During the interview, we should elicit responses to the following aspects

1. **End users (Students)**:
   - How user-friendly is the product interface?
   - What features are most useful to you?
   - What problems or inconveniences do you experience when using the product?
   - What features or improvements would you like to see in the future?

2. **Customers (Administration)**:
   - What are the main factors that influence your decision to purchase our
     product?
   - What features or services are most important to you?
   - What problems or inconveniences do you see in the current version of the
     product?
   - What would increase the likelihood of closing the deal?

Questions do not have to be asked directly. Using various techniques, we must
ensure that the answers we collect are of high quality.

### Conducted user surveys or feedback sessions

We conducted two custdev interviews to collect data on the user experience of
students at Innopolis University. These interviews were conducted six months
apart and included over 200 responses to the first interview and 53 responses to
the second interview.

#### CustDev \#1

The purpose of the first interview was to gather data about the students'
current user experience and find out what they want to see in future versions of
the product.

![Screen 1](/2024/roomreco/screen1.jpg)

![Screen 2](/2024/roomreco/screen2.jpg)

![Screen 3](/2024/roomreco/screen3.jpg)

**Note**: The screenshots show part of the questions.

#### CustDev \#2 (6 months later)

The purpose of the first interview was to assess changes in user experience and
to identify the level of adaptation and socialization of first-year students.

![Screen 4](/2024/roomreco/screen4.jpg)

![Screen 5](/2024/roomreco/screen5.jpg)

![Screen 6](/2024/roomreco/screen6.jpg)

**Note**: The screenshots show part of the questions.

#### Feedback from the administration

Recently we had a live meeting with the administration of the Innopolis
University campus. During the talks, we received information that helped us
adjust our plan to promote our product. In addition, agreements were reached to
use Randorm for the distribution of freshmen in 2024.

### Analyzing feedback, identifying and prioritizing issues

During a Capstone project, we constantly collect and analyze feedback from our
target audiences to continuously improve our product. This process helps us
understand user and customer needs, identify problems and find ways to solve
them. Based on the information gathered, we can prioritize tasks and effectively
plan for future product development.

Since the first version of our project was tested last year before InnoBootCamp
2023, we have made numerous decisions and conceptual changes aimed at enhancing
the user experience and focusing on the commercial aspects. This is why we
strictly separate end users from customers.

From the feedback gathered, several common themes and patterns emerged:

1. Usability Improvements:
   - Both students and administration highlighted the need for improved
     navigation and interface usability.
   - This indicates that user interface enhancements should be a high priority.
2. Functionality and Integration:
   - There is a strong demand for more integrations with other services, which
     is crucial for both students and administration.
   - Adding features for notifications, reminders, and communication is also
     highly requested by students.
3. Performance and Stability:
   - Bugs was a common issue among students, indicating a need for performance
     optimization.
4. Reporting and Analytics:
   - Administration emphasized the importance of robust reporting and analytics,
     suggesting this area needs significant improvement.
5. Customization and Flexibility:
   - Administration’s desire for customizable features and flexibility points
     towards a need to make the product more adaptable to different use cases.

Based on these findings, we have identified the following key issues to address:

- Enhance navigation and overall usability to make the product more
  user-friendly.
- Optimize the product for better performance and stability.
- Develop integrations with other services to enhance functionality.
- Improve reporting and analytics features to meet the needs of the
  administration.
- Add more customization options to make the product more adaptable to different
  use cases.

Immediate action will be taken to address these issues, with usability
improvements and performance optimization being prioritized.

You can see all of our issues and their priorities in the
[Randorm projects](https://github.com/orgs/randorm/projects).

## Roadmap

You can see all of our goals in the
[Randorm roadmap](https://www.notion.so/randorm/4f38e24232c143549c0ccd5831f1e653?v=eaa81c6fc01c4f65a5a4a1ac3f3240b9).

![Notion Roadmap](/2024/roomreco/notion-roadmap.jpg)

## Weekly Progress Report

### Backend Challenges and Solutions

#### What's new

1. We have implemented a Telegram authentication mechanism to allow users to log in with their Telegram accounts.
2. A memory database adapter has been created to store all information in memory, primarily for testing purposes.
3. The MongoDB database adapter has been finalized and several bugs have been resolved.
4. Comprehensive unit tests have been created (totaling 454 tests with 98% code coverage and 4,500 lines of code covered).
5. Work on user services and GraphQL API is starting to move forward using the hexagonal architecture.

#### Challenges

1. The user entity in the Telegram application is a complex object with several fields. During the authentication process, not all required information is available, and the application needs to request missing information from the user. Additionally, the same callback URL is used for both registering new users and logging into existing accounts, which leads to inconvinience in API design and handler implementations.

#### Solutions

1. The logic for handling authentication callbacks in Telegram has been improved. First, we parse and validate the incoming data by computing and comparing the hash digest of the message. If the message is valid, we check whether the user is already registered in our system. If they are, we generate a new JSON Web Token (JWT) for them and redirect them to the main page. Otherwise, we redirect them to the registration page, providing all the necessary information for a second call for registration from front-end side.

#### Next Steps

1. Finalize GraphQL API implementation and integrate it with the Telegram authentication mechanism.
2. Recreate Telegram Bot from previous iterations
3. Deploy the application to the cloud


### ML Challenges and Solutions

1. Creating custom metrics for testing and comparison of proposed solutions
- Due to the specificity of our hybrid student recommendation and allocation systems, existent metrics felt insufficient for our purposes. Therefore, the following solutions were proposed:
  - 1.1.  Recommendational system
    - The previous hybrid metric was updated by a logarithmic scale, producing better clusterization and separation of the data. Moreover, cosine similarity measure for multi-choice question has been changed to Jaccard similarity, due to non-ordinality of the data.
  - 1.2. Allocation system
    - New Graph similarity metric - relation of existing connections inside an allocated room to all possible connections for the roommates. As well as preservance of two-way "matches" in the graph
1. Implementing and testing Simulated Annealing for allocation
- Results on several metrics showed that SA behaves worse than greedy search on our data. Therefore this option was discarded, due to the presence of a better algorithm from the previous weeks.
1. Debugging recommendational system
- Our recommendational system is a complex combination of ML methods (like FAISS) with custom algorithms, so it took a couple of week to fully debug and thoroughly test. But we can finally rest assure on that accord.

## Conclusions and Next steps
This sprint we have successfully addressed a series of challenges related to the development and optimization of hybrid student recommendation and allocation systems. Through targeted solutions, significant progress was made in improving system performance and reliability.
For the following weeks, we will mainly focus on integration with backend, as well as potential NLP solutions for full-text questions in student profiles.