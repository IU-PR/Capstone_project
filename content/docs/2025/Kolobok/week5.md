---
title: "Week 5"
---

# Week 5 Progress Report: User Feedback & Final Adjustments

## Executive Summary

In Week 5, the Kolobok team shifted focus from system deployment to gathering valuable **user feedback** and finalizing adjustments based on real-world usage. We focused on refining user experience (UX), conducting **user acceptance testing (UAT)**, and addressing feedback to improve the platform's functionality and usability.

Feedback from internal testers and external stakeholders helped us identify areas for improvement in terms of model predictions, error handling, and overall workflow. This week was pivotal in refining the user journey, ensuring that the system met the expectations of end-users, and preparing for **final delivery**.

---

## Feature Refinements Based on User Feedback

### User Feedback Collection

After deploying the system to a staging environment, we collected feedback from external testers, including **TA feedback** and **peer review**. We specifically focused on the following:

- **User Interface (UI) Testing**: Observed how intuitive and responsive the interface was.
- **Model Performance**: Evaluated the accuracy of model predictions, especially in real-world scenarios with suboptimal conditions (poor lighting, unusual tire types).
- **Error Handling**: Identified user-reported issues related to failed predictions and miscommunications from the system.

Feedback methods included:
- **Survey** with a Likert scale (1–5) focused on UI, ease of use, and system reliability.
- **Direct User Interviews** with 3 external users.
- **Usability Testing Sessions** with 4 participants, each performing different tasks (e.g., uploading images, correcting predictions, etc.).

### Key Insights and Adjustments

#### **Ultra-Fast MySQL Indexing**
- **Feedback**: Users noticed slow performance when retrieving results for large batches of tire data.
- **Adjustment**: We implemented **ultra-fast indexing** on MySQL using **polars** for accelerated data retrieval, reducing query times from several seconds to milliseconds.

#### **OCR Model Accuracy**
- **Feedback**: Users reported issues with OCR when the tire text was partially obscured or had low contrast.
- **Adjustment**: We refined the **OCR pipeline** by enhancing the preprocessing pipeline. We also introduced additional data augmentation for **faint tire marks** to improve accuracy. We updated the dataset with synthetic tire text data generated via **Unity**, ensuring better generalization for edge cases.

#### **Improved User Journey**
- **Feedback**: Testers found some of the error messages unclear when the system could not process certain images.
- **Adjustment**: We improved **error feedback** by providing users with **specific suggestions** on how to improve image quality (e.g., "Increase brightness" or "Ensure tire text is clear").

---

## CI/CD & Optimization

### Ultra-Fast Indexing & Performance Improvements

In response to the performance bottleneck feedback, the team enhanced both the **backend and database performance**:
- **Ultra-Fast MySQL Indexing**: We deployed a new indexing technique on MySQL, resulting in significant speedups for data queries.
- **Polar’s Ultra-Fast Indexing**: By implementing **polar indexing** on large data columns, we optimized the speed of data retrieval, especially for complex queries related to tire images and OCR outputs.
- **Error Handling**: Additional robustness was introduced in the backend to ensure smoother error detection, logging, and resolution during high-load conditions.

---

## ML Model Updates

### Model Refinement

Following feedback and further analysis, we conducted the following model refinements:

#### **Unwrapper Model (ML)**

- We optimized the **unwrapper model** code written in **Python** for more efficient performance, particularly on image preprocessing tasks like flattening curved tire sidewalls for OCR analysis.
- **Performance**: The wrapper model now runs **twice as fast**, with improved efficiency in handling distorted or oblique images.

#### **Spike Detection and Classification**

- We tested and fine-tuned the classification stack to improve performance on tire spikes under various environmental conditions.
- **Model Configuration**: Fine-tuned **ResNet models** for better performance on small, low-contrast spike data.
  
#### **New Dataset Parsing**

- We further refined the dataset pipeline, particularly for the **OCR** tasks, to handle **larger datasets** with more diverse tire text examples.
- A **new dataset parsing module** was added to clean and preprocess OCR input, speeding up both training and inference times.

---

## Key Technical Contributions

### **Ultra-Fast MySQL Indexing**  
**Nikita Menshikov** led the development and implementation of ultra-fast indexing on MySQL, reducing query times significantly, particularly for large sets of tire data. This enhancement allowed the system to handle large data batches more efficiently, improving the overall user experience.

### **Optimized OCR Model & Dataset Enhancements**  
**Nikita Zagainov** drove the improvement of the OCR pipeline, focusing on data augmentation for synthetic tire text samples and preprocessing enhancements. The result is a more accurate OCR model that handles low-contrast and obscured tire text much better than before.

### **Polar Indexing for Faster Data Retrieval**  
**Darya Stepanova** worked on improving the **polar indexing** method used within the MySQL database to speed up tire image retrieval times. This change improved query execution speeds and reduced bottlenecks in high-load conditions.

### **Unwrapper Model Code Enhancement**  
**Dmitry Tetkin** refactored and optimized the code for the **unwrapper model**, making it more efficient and able to handle diverse input images faster. This resulted in a more responsive system, particularly under varying lighting conditions and tire orientations.

---

## Next Steps & Roadmap

- **Final Model Fine-Tuning**: Continue to gather feedback to enhance model performance based on user interactions, with a focus on edge cases.
- **Documentation**: Enhance API and user documentation based on the final system state, incorporating feedback from UAT testers.
- **Production Deployment**: Prepare for **final production deployment** following further minor optimizations and final user training.

---

## Team Contributions

| Team Member            | Contributions |
|------------------------|---------------|
| **Nikita Menshikov**    | Led the ultra-fast MySQL indexing implementation, fine-tuned error handling, coordinated final testing and feedback integration |
| **Nikita Zagainov**     | Optimized the OCR pipeline, improved dataset parsing and augmented data, enhanced model accuracy with real-world feedback |
| **Dmitry Tetkin**       | Optimized unwrapper model code, enhanced speed and preprocessing pipeline for faster image processing |
| **Vladislav Strelkov**  | Ensured CI/CD pipeline integration, optimized deployment for large datasets, implemented automatic rollback mechanisms |
| **Sergey Aitov**        | Led backend testing efforts, verified bug fixes related to image processing, ensured smooth system interactions with the backend |
| **Ekaterina Petrova**   | Led frontend testing, UX/UI improvements, and ensured seamless data flow between frontend and backend |
| **Darya Stepanova**     | Refined frontend components, implemented polar indexing in MySQL, worked on final usability improvements |

---

## Confirmation of System Operability

- ✅ All tests passing locally and in CI
- ✅ Code in repository is in working condition
