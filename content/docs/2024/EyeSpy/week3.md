---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

  The infrastructure and backend development are scheduled for another week. This week, we concentrated on the main feature – face detection.

- **Backend Development**:

  Backend development tasks will be addressed in the upcoming weeks. Our current focus is on the front-end and core features.

- **Frontend Development**:

  Significant progress was made on the app's front end. We successfully implemented face recognition and landmark drawing. These features are now functional, providing a solid foundation for further development.

- **Data Management**:

  Data management isn't applicable in our case since we don't store any user data. Proctoring sessions are temporary and exist only while running.

- **Prototype Testing**:

  For testing, I used myself as a subject in different lighting conditions and environments to ensure the accuracy and reliability of face detection and landmark drawing. This practical approach helped us refine the feature and prepare for more extensive testing.

  ![Week3_Progress](/2024/EyeSpy/Week3_Progress.jpg)

  > Me and my eyes

## **Weekly Progress Report**:

Our team focused on landmark recognition and successfully implemented eye cropping. This involved understanding the coordinate space of landmarks and using the low-level Quartz framework for image cropping. We needed to ensure real-time cropping with minimal resource usage, preserving performance for CoreML processing.

### **Challenges & Solutions**

One of the biggest challenges was understanding the coordinate space for landmarks and performing image cropping using the Quartz framework. This was essential to achieve real-time processing without using excessive resources. We tackled this by diving deep into the Quartz documentation and experimenting with different approaches until we achieved the desired performance.

### **Conclusions & Next Steps**

This week, we made significant progress in landmark recognition and eye cropping, setting the stage for the next phase. The next steps include converting our PyTorch model to CoreML and integrating it into our recognition flow. This will enable us to leverage the full capabilities of CoreML for efficient and accurate eye-tracking.
