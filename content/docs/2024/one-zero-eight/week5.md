---
title: "Week #5"
---

# Week 5 - Feedback Analysis and Roadmap

## **Feedbacks**

- **Feedback collection plan**

  The most important feature of our product is search engine for study materials. So, we need to somehow collect the
  metrics to understand the relevance of the search responses. One way is to collect feedback personally from our users:
  are the answers to their queries relevant, or not. Another way is to introduce more algorithmic method — add buttons
  “like” and “dislike” for the query responses on the website, and write clicks to the database.

  Also, we have Yandex Metrika installed on the website. It provides us the way to see the number of people who use the
  website. Also, we can view their path on the pages, record clicks, mouse movements and other actions. It will help us
  to understand whether our website is convenient for people to use.

  We are looking forward to releasing the public version of the website. We will collect feedback form from students and
  employees who will use the service.

- **Conducted user surveys or feedback sessions**

  **Description:** our initial approach was to present our website to a selected group of individuals who could offer
  valuable insights based on their familiarity with our platform or their unique perspectives as potential end-users. We
  chose to show our site to 20 friends who are students ranging from the 1st to the 4th course, along with several
  alumni. This selection ensured a mix of fresh perspectives and experienced viewpoints, providing us with a broad
  spectrum of feedback.

  **Format:** mainly feedback was collected during oral sessions. This decision was made to encourage open dialogue,
  allowing participants to express their thoughts freely without the constraints of structured forms.

  **Findings:**

    - **Usability Concerns:** several participants highlighted issues related to search results inaccuracy due to
      simplicity of current search approach.
    - **Design Suggestions:** there were numerous suggestions for improving the visual appeal and layout of the website.
    - **Feature Requests:** participants requested additional functionalities that they believed would enhance their
      experience, such as creating and visualizing knowledge graph or implementing generation part with use of LLMs.
- **Analyzing feedback, identifying and prioritizing issues**

### Feedback Analysis

- **Positive Reception**: Users expressed strong enthusiasm for the browser extension, particularly appreciating the
  Moodle Autologin feature. This feedback highlights the importance of releasing the extension as soon as possible.
- **Search Engine Reaction**: The search engine garnered significant attention and feedback, indicating a high demand
  for its functionalities. Users are eager for its completion and release.

### Identified Issues and Prioritization

- **Interactive Feedback**: It is necessary to come up with an interactive form for receiving feedback from users in
  order to interest them in the development of our product
- **Accelerated Development**: The search engine development needs to be fast-tracked to address the high user demand
  and interest.
- **Additional Data Sources**: Prioritize integrating the newly identified data sources (EduWiki, Innopolis University
  website, dormitory website, etc.) to enhance the search engine's utility and comprehensiveness.

## **Roadmap**

### 1. Improve Search Accuracy with Rerankers

To enhance the relevance of our search results, we will implement rerankers. Rerankers will re-evaluate the initial
search results and prioritize the most relevant ones based on additional criteria, improving overall search accuracy.

### 2. Mobile Platform Adaptation

Given the increasing use of mobile devices, we will ensure that our platform is fully responsive and optimized for
mobile use. This adaptation includes refining the user interface and experience to provide seamless functionality across
different screen sizes and mobile browsers.

### 3. Advertising and Promotion

To increase user engagement and visibility, we will launch targeted advertising campaigns. These campaigns will focus on
platforms such as @one_zero_eight, Opportunities For You, and other relevant communities and social media channels. We
aim to reach a wider audience of potential users, including students and educators.

### 4. Integration of New Data Sources

We will continuously enhance our search engine by integrating new data sources. Some of the identified sources include
EduWiki, the Innopolis University website, and dormitory information. This expansion will provide users with a more
comprehensive and diverse range of study materials.

### 5. Incorporate LLM-Based Generation Features

To provide advanced functionalities, we will integrate large language models (LLMs) for generating content. This feature
will assist users in creating summaries, extracting key points, and generating insights from study materials, thereby
enriching their learning experience.

### **Timeline and Milestones**

**Q3 2024:**

- **July:**
    - Start implementing rerankers for search accuracy.
    - Begin mobile platform adaptation and design optimization.
    - Launch initial advertising campaigns in selected channels.
- **August:**
    - Complete reranker integration and conduct testing.
    - Finalize mobile platform adaptation, ensuring full responsiveness.
    - Continue advertising and gather initial user feedback.
- **September:**
    - Integrate EduWiki and Innopolis University data sources.
    - Enhance search functionality with the newly integrated data.
    - Evaluate the effectiveness of advertising campaigns and adjust strategies accordingly.

**Q4 2024:**

- **October:**
    - Develop and test LLM-based generation features.
    - Begin integration of dormitory information into the search engine.
    - Host a webinar to showcase new features and gather live feedback.
- **November:**
    - Optimize LLM generation based on user feedback.
    - Expand advertising to additional relevant channels.
    - Conduct a second round of user feedback sessions to assess improvements.
- **December:**
    - Finalize integration of all planned data sources.
    - Release a major update incorporating all new features and improvements.
    - Conduct a comprehensive review and plan the roadmap for 2025.

### **Conclusion**

By following this roadmap, we aim to significantly enhance the usability, accuracy, and functionality of our platform.
Each milestone is designed to address user needs and improve their overall experience. Through continuous feedback and
iterative development, we will ensure that our platform remains a valuable tool for students and educators.

## **Weekly Progress Report**:

This week, our team continues to actively work on the project. The phase of refining the existing code and optimizing it
is underway. The active development of the necessary functionality for the final product continues.

**Moodle Browser Extension:**

The development of a browser extension for the ability to send files from the moodle to the project server continues

**Frontend Development:**

New functionality was defined for the user's ability to interact with the site, and minor edits for the site were also
identified.

**Backend:**

Significant work has been done on the project's backend:

- Implemented methods for searching document metadata, such as the source.
- File metadata is uploaded to MongoDB, while the files themselves are stored in MinIO. Data search by file metadata has
  been implemented.
- Optimized PDF processing.

**AI Development:**

A script has been written to generate test queries and evaluate their relevance, helping us refine our search
algorithms.

**Telegram Bot:**

At the weekly meeting, the functionality that needed to be supplemented and updated was identified, and work continues
on code optimization.

**Team Communication:**

The team actively interacted with each other throughout the week. We had two face-to-face meetings with the whole team,
as usual during the TA meeting and on Friday's weekly team meeting.

### **Challenges & Solutions**

Prioritizing and addressing identified issues: With various feedback and identified issues, prioritizing and resolving
them in a timely manner can be challenging.

Using an agile development approach has helped us effectively prioritize and adress identified issues. By breaking down
feedback into manageable tasks and prioritizing them based on impact and user needs, we can ensure that key issues are
addressed promptly while providing continuous improvement of the product.

### **Conclusions & Next Steps**

Our feedback collection plan is designed to capture user engagement metrics, such as likes and dislikes, while ensuring
protection against spam by tracking individual user interactions. We will leverage Yandex Metrics to gain deeper
insights into user behavior. Additionally, post-launch, we plan to distribute a feedback form to collect more detailed
user opinions.

The user surveys conducted with 20 students and alumni were instrumental in identifying key areas for improvement. These
sessions highlighted the need for better search result accuracy, enhancements in visual design, and additional features
like knowledge graph visualization and the integration of LLM-based generation.

From the feedback analysis, we identified several priorities:

1. **Interactive Feedback**: Developing an interactive form to better engage users and gather valuable feedback.
2. **Accelerated Development**: Fast-tracking the search engine development to meet high user demand.
3. **Additional Data Sources**: Integrating new data sources such as EduWiki, the Innopolis University website, and
   dormitory information to enhance the search engine's functionality.

Our roadmap to address these priorities includes implementing rerankers to improve search accuracy, adapting the
platform for mobile use, promoting our platform through targeted channels, and incorporating LLM generation features.

Based on the insights and priorities identified in our feedback analysis, we have outlined the following next steps to
refine our platform and meet user expectations: We will polish the design of the frontend and ensure it is fully
responsive for mobile devices, enhancing visual appeal and usability. For the browser extension, we plan to improve the
accuracy and comprehensiveness of course data collection. On the backend, we will implement search functionality for
content gathered from Telegram chats, expanding the scope and utility of our search engine. By following this plan, we
aim to refine our platform, align with user expectations, and deliver a robust, user-friendly product.