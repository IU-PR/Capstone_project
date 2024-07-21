---
title: "Week #6"
---

# **Week #6**

## Overview

This week, our primary focus was on polishing the project to ensure it meets all MVP functionalities and preparing a compelling presentation. Below is a detailed account of our progress and current status.

## Key Accomplishments

### Exam Generation Feature

- **Completion**: We have successfully implemented the exam generation feature. This functionality now generates exam variants with correctly defined extracts (text passages) and accurately refers to these extracts within the generated exams.

### Code Refactoring

- **Technology Transition**: We are in the process of refactoring the codebase, transitioning from React to Next.js. This shift is aimed at improving the performance and maintainability of the project.

### Bug Fixes

- **Content Segments**: We addressed and resolved issues where content segments were interfering with each other, ensuring smoother functionality and improved user experience.

![Generate](/2024/A-Level/generate_a.jpg)
![Generate](/2024/A-Level/geneate_b.jpg)
![Generate](/2024/A-Level/generate_c.jpg)
![Generate](/2024/A-Level/generate_d.jpg)

### Model Performance and Integration

- **Inference Timer**: We have evaluated the performance of our models with the following results:
  - **Multinomial Naive Bayes (MNB)**: 121,677 samples per second.
  - **PyTorch Model**: 3,729 samples per second.

- **Model Deployment Strategy**: Based on the inference times and accuracy analysis:
  - We will deploy both models in production.
  - A queue system has been implemented to manage model utilization efficiently:
    - **PyTorch Model**: Used when the queue is less congested.
    - **MNB**: Utilized during high-load periods due to its faster inference time, albeit with slightly reduced accuracy.

### Continuous Deployment (CD) and Integration

- **Constant Integration**: We have made significant progress in integrating the Constant platform.
- **CD Implementation**: Current efforts are focused on setting up Continuous Deployment (CD), including rewriting the codebase to Next.js and incorporating KANs (Kernel Attention Networks) for enhanced interpretability.

## Upcoming Tasks

- **Deployment**: Our primary goal for the upcoming week is to finalize the deployment of the project.
- **Presentation**: We will also concentrate on polishing and completing the presentation to effectively communicate the project's features and benefits.

## Conclusion

We have made substantial progress this week, addressing critical issues and enhancing our project’s functionality and performance. We are on track to deploy the project next week and will continue to refine the presentation to ensure a comprehensive and compelling delivery.