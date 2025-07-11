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

#### **Super-fast PostgreSQL Indexing**
- **Feedback**: Users noticed slow performance when retrieving results for large batches of tire data.
- **Adjustment**: We implemented **fast indexing** on PostgreSQL using **polars** for accelerated data retrieval, reducing query times from several seconds to hundred milliseconds.

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
- **Ultra-Fast PostgreSQL Indexing**: We deployed a new indexing technique on PostgreSQL, resulting in significant speedups for data queries.
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

## Next Steps & Roadmap

- **Final Model Fine-Tuning**: Continue to gather feedback to enhance model performance based on user interactions, with a focus on edge cases.
- **Documentation**: Enhance API and user documentation based on the final system state, incorporating feedback from UAT testers.
- **Production Deployment**: Prepare for **final production deployment** following further minor optimizations and final user training.

---

## Team Contributions

| Team Member            | Contributions |
|------------------------|---------------|
| **Nikita Menshikov**    | Wrote the report, fine-tuned error handling, coordinated final testing and feedback integration |
| **Nikita Zagainov**     | Led the development of OCR pipeline, researched and finalized model and architecture, added [validation](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/35eaf582509edae49dcf615ad57a9c39266fa3ff) to the pipeline |
| **Dmitry Tetkin**       | Ported visual on various platforms ([1](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/b2c6eae741c17c76fc84a45efc37b6539fbd7373), [2](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/581ca2464e562c8ae9fb63ce0dd20ba2720c2c77), [3](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/24875bc94d4807c6c35f9d88badd3a13fce8f457)), assisted with OCR [research](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/b0b183f96e8a7224143d85e07ec10d7355658fdf) |
| **Vladislav Strelkov**  | Implemented database service and [indexing](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/b38378afe3333155470e763b1cac4e28cf791c70) on MySQL and PostgreSQL |
| **Sergey Aitov**        | Tested OCR pipeline, [fine-tuned](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/a15fffbef9abd559965434e18bea7df9f6ab05c2) models and builded the pipeline |
| **Ekaterina Petrova**   | Added tire [preprocessing](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/44f79471d8e90e090c899c0df13c0c1c2252fb37) for OCR |
| **Darya Stepanova**     | Implemented [site](https://github.com/IU-Capstone-Project-2025/Kolobok/tree/my-frontend-update) MVP version, enhanced UX based on user feedback|

---

## Confirmation of System Operability

- ✅ All tests passing locally and in CI
- ✅ Code in repository is in working condition
