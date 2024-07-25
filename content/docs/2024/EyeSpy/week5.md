---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

- **Feedback collection plan**

This week, we implemented a feedback collection plan by providing users with a demo app. The app highlights the estimated gaze point with a blue region on the screen. Users were asked to run the app in the background while performing their usual computer tasks. We aimed to gather feedback on how the app affects overall system performance and the accuracy of the gaze point estimation.

- **Conducted user surveys or feedback sessions**

We conducted surveys where users shared their experiences using the app. They provided insights into how the app impacted system performance and how accurate they felt the gaze estimation was compared to where they were actually looking on the screen.

- **Analyzing feedback, identifying and prioritizing issues**

After analyzing the feedback, we discovered that head position significantly affects the stability and accuracy of predictions. The estimations were most accurate when the user's head was centered in the camera's viewpoint. Based on this insight, we prioritized adding head position estimation and integrating notifications to alert users when their face is not well aligned with the camera. Additionally, we plan to add a warning in the web panel to inform administrators when the user is not well visible. Next steps include improving head position estimation and integrating these notifications to enhance the overall accuracy and usability of the app.

## **Roadmap**:

Since eye tracking is completed, our next steps are:

1. Implement the server and web panel.
2. Add an onboarding screen where users are asked for camera permissions and their name to connect to the current proctoring session.
3. Develop a web panel where administrators can monitor the presence of students and their behavior.

## **Weekly Progress Report**:

Our team conducted initial beta testing and fully implemented gaze estimation, including the conversion to screen coordinates. The challenging part was finding the right formula to convert the eye gaze vector from 3D space to a 2D position on the screen.

![Week5_Demo](/2024/EyeSpy/Week5_Demo.gif)

> 25Mbs and 20 seconds of blue dot following my eyes

### **Challenges & Solutions**

The primary challenge was determining the correct formula for converting the 3D gaze vector to a 2D screen position. We experimented with various mathematical models and approaches until we found a solution that accurately maps the gaze vector to screen coordinates.

### **Conclusions & Next Steps**

We successfully concluded that our client-side implementation is working as expected. The next steps involve implementing the entire infrastructure, including the server and web panel, followed by comprehensive end-to-end testing. This will ensure that the system functions correctly and meets all requirements for real-time proctoring.
