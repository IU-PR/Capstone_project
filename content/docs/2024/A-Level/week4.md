---
title: "Week #4"
---

# **Week #4**

### **External Feedback**

This week, we conducted User Acceptance Testing (UAT) by presenting our Figma prototype to our actual users, Anastasia (A-level tutor) and Dmitriy (student currently preparing for the A-level exam). Their feedback was highly positive:

1. **Design**: Both Anastasia and Dmitriy praised the design, noting its aesthetic appeal and intuitive layout.
2. **Functionality**: They found the existing features very useful for both students and tutors.
3. **Suggestions**: Anastasia and Dmitriy suggested adding a playground page where users could test the automatic question-topic classification feature without downloading/uploading the exam PDF.

After internal discussions, our team decided that while the playground page is a valuable addition, it is not a high-priority feature at this stage. We will consider implementing it in later phases of the project.

Overall, the feedback was encouraging and validated our current design and functionality, providing us with constructive insights for future enhancements.

### **Testing**

This week, we conducted testing on several major components of the project:

1. **Frontend Features**:
   - File uploading
   - Image uploading
   - Task-related features
   - Others

2. **Machine Learning Model**:
   - Inference testing for topic classification

These tests allowed us to assess the functionality and reliability of the developed features and identify areas for improvement. The testing phase is crucial for ensuring a seamless user experience and addressing any potential issues before moving forward with further development.

### **Iteration**

We are effectively adapting our design, functionality, and features based on user feedback, team meeting decisions, and the bottlenecks encountered throughout the development process. This iterative approach ensures that we continuously refine and enhance our project to better meet our goals and user needs.


## Overall Weekly Progress Report

### Machine Learning

- **Data Augmentation**: 
  - Increased the dataset size to nearly three thousand samples, enhancing the robustness of our models.
- **Model Retraining**: 
  - Retrained all models, including Multinomial Naive Bayes (MNB), Word2Vec + SVC, and RoBERTa, using the augmented dataset.
- **Model Reevaluation**: 
  - **RoBERTa**: Achieved 94% accuracy, demonstrating high performance in classification tasks.
  - **Multinomial Naive Bayes (MNB)**: Achieved 87% F1 score, offering the best balance between speed and robustness.
  - **Word2Vec + Support Vector Classifer (SVC)**: Achieved 82% F1 score, showing decent performance but lagging behind RoBERTa and MNB.
  - **Inference Speed**: MNB showed the fastest inference time when called from the website (well below 1 second for a 40 question exam, including the overhead from HTTP communcation), making it the current choice for production deployment. However, we plan to transition to RoBERTa in the future for better accuracy.
- **Enhancements**:
  - Improved the DatasetReader utility for easier data handling and processing.
  - Cleaned and reorganized the Jupyter notebooks to enhance readability and maintainability for both current developers and future contributors.
  - Reran and refactored the exploratory data analysis notebook, ensuring up-to-date insights and better data visualization.

### Back-end

- **New Features Implemented and Tested**:
  - **File Uploading**: Enabled users to upload files seamlessly.
  - **Image Uploading**: Added functionality for image uploads.
  - **Task/Question Management**: Implemented creation, deletion, and prediction of tasks/questions using the ML model.
- **Integration**:
  - Successfully connected the back-end functionality to the front-end interface, ensuring smooth data flow and user interaction.
  - Integrated the ML model (currently MNB) with the back end, achieving high-speed predictions with inference times significantly below 1 second.

### Front-end

- **Developed Pages**:
  - **Browse File Page**: Allows users to browse and select files for upload or viewing.
  - **Upload File Page**: Facilitates file uploading with a user-friendly interface.
  - **Questions Page**: Displays questions and enables interaction with the task management system.
  - **Document View Page**: Provides a detailed view of uploaded documents.
  - **Edit and Create Question Page**: Allows users to create and edit questions seamlessly.
- **Routing**: 
  - Implemented URL routing to ensure smooth navigation between different pages.
- **Integration**:
  - Connected all developed pages to the back end, ensuring full functionality and interactive features.

### Summary

- **Progress and Achievements**:
  - Significant advancements in both machine learning and full-stack development.
  - Enhanced dataset and retrained models leading to improved performance metrics.
  - Successfully implemented and tested new back-end features and integrated them with the front end.
  - Developed and connected multiple front-end pages, providing a seamless user experience.
- **Challenges**:
  - No fatal bottlenecks or major hardships encountered this week.
- **Next Steps**:
  - Continue refining the ML models, with a focus on transitioning to RoBERTa for production use.
  - Further develop and test back-end and front-end features.
  - Maintain an iterative approach, incorporating ongoing feedback and testing results to enhance the project continuously.

Overall, the team is on track and making excellent progress towards our project goals.