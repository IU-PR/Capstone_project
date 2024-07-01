---
title: "Week # 4"
---

# Match&Watch: Project Report for Week 4

### External Feedback

To gather feedback, we asked some of our friends to test our current prototype. As the frontend and authentication system were the only parts operational, the feedback focused on the user interface, user experience, and the format of the questions we are using in the registration and the recommendation system.

**Summary of Feedback:**

- The design should be more interactive.
- The user experience should be more enjoyable.

**Action Plan:**

- We plan to add animations to make the website more engaging and fun to use.

### Testing

**Current Status:**

- We are integrating k6 load and stress tests to make sure time and memory threshholds are not breached in concurrent scenarios.
- At this stage, we do not have computational endpoints to stress test, only the registration and login functionalities are available. So, we worked on a dummuy example to showcase our goal:

![Sample Image](/2024/matchi/week4-1.png)

![Sample Image](/2024/matchi/week4-2.png)

![Sample Image](/2024/matchi/week4-3.png)
**Upcoming Testing Tasks:**

- Write unit tests to mock database operations.
- Use scenarios and thresholds to stress test and load test concurrent user scenarios.

### Iteration

#### Frontend

**Completed Tasks:**

- Enhanced the design, transforming the website from a basic structure to a unified theme.
- Added a profile page.
- Connected the frontend with the backend for the authentication system.

![Sample Image](/2024/matchi/week4-4.png)

![Sample Image](/2024/matchi/week4-5.png)

![Sample Image](/2024/matchi/week4-6.png)

![Sample Image](/2024/matchi/week4-7.png)

**Upcoming Tasks:**

- Refine the design.
- Make the design responsive.
- Develop the "Previous Matches" page.

#### Backend

**Completed Tasks:**

- Modified the authentication system.
- Began building the CI/CD pipeline.
- Developed the preferences section for the user profile page.
- Finished the structure for the recommnedation backend microservice.

**Upcoming Tasks:**

- Integrate the recommendation system (if ready).
- Complete the CI/CD pipelines for frontend and backend repositories.

#### AI

**Dataset Preparation:**

- Cleaned and tokenized the dataset.
- Extracted ten unique emotions using ChatGPT.
- Identified and included the top two emotions for each movie based on descriptions and genres.

![Sample Image](/2024/matchi/week4-8.png)

![Sample Image](/2024/matchi/week4-9.png)

![Sample Image](/2024/matchi/week4-10.png)

**Current Status:**

- The dataset is ready with the extracted emotions and necessary features.
- Initial work on extracting embeddings has been done, but some issues need to be addressed.

**Upcoming Tasks:**

- Fix problems with embedding extraction.
- Re-train the embeddings.
- Integrate embeddings from categorical features with numerical ones for the recommendation system.
