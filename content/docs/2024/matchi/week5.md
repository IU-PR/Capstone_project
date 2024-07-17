---
title: "Week # 5"
---

## Match&Watch: Project Report for Week 5

### Continuous Feedback & Enhancement

During this week, we collected valuable feedback from a diverse group of students focusing on the usability, design, and overall user experience of our platform. This feedback has been instrumental in refining our product, allowing us to make targeted improvements and ensure that we are on track to achieve our intended goals.

**Feedback Collection:**

- **Interviews:** We arranged meetings with additional potential users, including fellow students that provided us with valuable insights on how to deliver the best User experience in our platform.
- **General Questions:**
  - What can be improved or changed in the Lo-Fi design, to provide a better user experience?
  - Should we provide the user the ability to skip questions during the movie matching phase?
  - What do you like about this idea in general and what can be improved ?
  - Do you think that additional filtering can give better curated result for the user or questions are enough?
- **Feedback outcome:** Based on the majority of the answers, we understood that we need to keep our website simple with 2-3 screens and dedicating them to the main purpose of the platform which is matching movies, we should build our Hi-Fi design in a modern and sleek way and incorporating dark mode because it is more visually appealing and topic related (most movie related platforms use dark mode), in our AI we should take into consideration description of the movie, IMDB rating, Rotten Tomatoes rating, and user hype keywords for better matching.
- **Implementation of Feedback:**
  - Sleek and modern Hi-Fi design
  - Responsive website with animations
  - Enhanced AI that takes into consideration additional features for better sorting and matching
  - Robust backend that can handle a decent load and a big user base
  - Filtering before matching to give users more flexibility

### Iteration of Week 5

#### UX & UI

**Completed Tasks:**

- Overall Hi-Fi design
- Main Page Design
- Login New Design
- Sign Up New Design

**Upcoming Tasks:**

- Design Hi-Fi History page
- Design Hi-Fi simple Profile page
- Finalize the Hi-Fi design & do some prototyping in Figma

**Design Preview:**

![Sample Image](/2024/matchi/week5-1.png)

![Sample Image](/2024/matchi/week5-2.png)

#### Frontend

**Completed Tasks:**

- Developed and refined the login and signup pages.
- Implemented a low-fidelity design for the new pages: home, history, profile, questionnaire, and output.
- Ensured basic functionality for navigation and interaction on these pages.
- Implemented the structure of the Questionaire and output Pages

**Upcoming Tasks:**

- Reintegrate the new Hi-Fi design structure into the frontend side + style it
- Integrate the questionnaire with backend systems to collect user preferences.
- Add a logout feature.
- Implement a feedback system for continuous user input.
- Finalize the interface implementation for a single user (coordinate with backend on required fields).
- Develop filters for refining search results.

#### Backend

**Completed Tasks:**

- Developed the initial authentication system.
- Constructed the CI pipelines with building and pushing docker images to dockerhub.
- Laid the groundwork for the user preferences section.
- Collaborate with the ML and frontend teams to gather requirements and dependencies.
- Design the API for the recommendation microservice based on gathered requirements.
- Developed the backbone of the recommendation system based on user query or keywords.
- Developed a testing pipeline with k6 stress tests for the recommendation system

**Upcoming Tasks:**

- Develop the question generation mechanism for the questionnaire.
- Build and test the recommendation system for individual users.
- Scale the recommendation system to support multiple users.
- Commit all backend code to the course organization repository.
- Set up CI/CD pipelines for the frontend.

![Sample Image](/2024/matchi/week5-3.png)

![Sample Image](/2024/matchi/week5-4.png)

#### AI

**Completed Tasks:**

1. Extract Embeddings for Main Features:
   Extract embeddings for the four main features (description,type,genres,emotions) from the Netflix movies dataset and
   Combined the extracted embeddings for each movie into a single vector by taking the mean of the four feature embeddings.

2. Take input from the user regarding their preferences.
   Extract embeddings from the user's input to represent their preferences in the same feature space as the movies.

3. Find Closest Movies Using Cosine Similarity

Calculate cosine similarity between the user's preference embedding and each movie's combined embedding.
Identify and recommend the top 5 movies with the highest cosine similarity scores.

**Upcoming Tasks:**

1. Validate Embeddings Quality

Evaluate the quality of the extracted embeddings.
Perform tasks such as clustering, visualization (e.g., t-SNE or PCA), and checking for coherence in clusters to validate embeddings.
Fine-tune the embedding model if necessary to improve quality.

2. Extend the Dataset
   Incorporate additional features into the dataset, such as user ratings, reviews, release year, runtime, etc.,
   Collect and integrate data from other streaming platforms (e.g., Amazon Prime, Hulu, Disney+).

3. Enhance Recommendation Algorithm
   Experiment with different methods of combining embeddings (e.g., weighted mean, concatenation).

![Sample Image](/2024/matchi/week5-5.png)

![Sample Image](/2024/matchi/week5-6.png)
