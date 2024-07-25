---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member | Telegram ID | Email Address                   |
| ----------- | ----------- | ------------------------------- |
| AlexStrNik  | @alexstrnik | a.strijnev@innopolis.university |

### **Value Proposition**

- Identify the Problem:

  In today's digital age, ensuring the integrity of remote exams and interviews is a big challenge. Traditional proctoring methods often invade user privacy by sending video streams to external servers for monitoring. This not only raises privacy concerns but also risks exposing sensitive data to unauthorized access. There is a clear need for a solution that balances security and privacy without disrupting the user experience.

- Solution Description:

  Our app tackles this issue by using advanced eye-tracking technology to monitor where users are looking during remote exams and interviews. The key feature is that all video processing happens locally on the user's MacOS device. This means no data is transmitted outside, keeping everything private. Whenever the app detects that the user is not looking at the monitor, it triggers an alarm, ensuring the user remains engaged and reducing the chances of cheating.

- Benefits to Users:

  With our app, users can enjoy a high level of privacy since all data stays on their device. The continuous eye gaze monitoring ensures that users stay focused on their tasks, upholding the integrity of exams and interviews. The app operates smoothly in the background, offering a hassle-free proctoring solution that respects user privacy and provides peace of mind.

- Differentiation:

  Our app stands out because it processes video streams locally, unlike other proctoring solutions that send data to external servers. This approach guarantees that user data remains secure and private. Additionally, the advanced eye-tracking technology delivers precise and reliable monitoring, ensuring users stay engaged throughout their exams or interviews.

- User Impact:

  By addressing privacy concerns and enhancing the security of remote proctoring, our app significantly improves the user experience. Students and professionals can confidently participate in exams and interviews, knowing their data is protected. Educational institutions and companies benefit from a trustworthy solution that maintains the integrity of their assessments without compromising user privacy.

- User Testimonials or Use Cases:

  Students have found the app to be a game-changer for online exams, feeling more secure knowing their data isn't being sent anywhere. Professionals appreciate the focus it ensures during remote interviews, helping maintain fair and honest practices. Educational institutions have streamlined their proctoring processes, finding the app reliable, respectful of student privacy, and effective in maintaining exam integrity.

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address?

   Our software addresses the challenge of ensuring integrity during remote exams and interviews while protecting user privacy. Traditional proctoring methods often compromise privacy by transmitting video streams to external servers, which can lead to data breaches and unauthorized access. Our app keeps all video processing local, ensuring that sensitive data never leaves the user's device, thus maintaining privacy and security.

2. Who are your target users or customers?

   Our target users are primarily students taking remote exams and professionals participating in remote interviews. Educational institutions and companies conducting these exams and interviews are also key users, as they need a reliable and privacy-conscious solution to ensure the integrity of their processes.

3. How will you validate and test your assumptions about the project?

   To validate and test our assumptions, we plan to conduct an experiment involving a group of students divided into two subgroups. One subgroup will attempt to cheat during the exams, while the other will not. By monitoring both groups, we can assess the effectiveness of our eye-tracking technology and local processing in detecting cheating attempts. We will measure the success by analyzing the true/false positives and negatives to ensure our app accurately distinguishes between genuine and cheating behaviors.

4. What metrics will you use to measure the success of your project?

   We will measure the success of our project by examining the rates of true positives, false positives, true negatives, and false negatives. True positives occur when the app correctly identifies cheating behavior, and true negatives happen when it accurately recognizes non-cheating behavior. False positives and false negatives will help us understand any inaccuracies or areas needing improvement. By analyzing these metrics, we can gauge the app's accuracy and reliability in real-world scenarios.

5. How do you plan to iterate and pivot if necessary based on user feedback?

   Based on user feedback, we plan to iterate and pivot by refining the eye-tracking algorithms and improving the user interface to enhance accuracy and usability. If users report issues or suggest enhancements, we will prioritize those adjustments in our development cycle. Continuous feedback will guide our updates, ensuring the app meets user needs and maintains high standards of privacy and security. By staying responsive to user input, we can ensure our app evolves to better serve its purpose.

## **Leveraging AI, Open-Source, and Experts**

Our app uses cutting-edge AI and open-source technology to track eye gaze effectively. We start with an open-source PyTorch model called gaze-estimation, which predicts where you're looking based on images of your eyes. To make it run faster on MacOS, we convert this model to CoreML, letting us use the computer's hardware more efficiently. This means our app works in real-time without needing a high-end video card.

We also reviewed many studies to find the best models for real-time eye gaze estimation. This helps us ensure our app uses the latest and most efficient technology available. By combining advanced AI, open-source solutions, and expert research, we provide a reliable, high-performing eye-tracking app that keeps all data processing local for maximum privacy.

## **Defining the Vision for Your Project**

- Overview:

  Our project aims to create a privacy-focused MacOS app that uses eye-tracking technology to ensure the integrity of remote exams and interviews. By leveraging advanced AI and local processing, we ensure that user data remains secure on their device. The app monitors eye gaze in real-time and triggers an alarm if the user is not looking at the screen, helping to prevent cheating without compromising privacy.

- Schematic Drawings:

  ![app_scheme](/2024/EyeSpy/App_Scheme.png)

- Tech Stack:

  Our tech stack combines several powerful tools and frameworks to deliver a high-performing app. For app development, we use CoreML, Swift 5, Vision Framework, AppKit, and UrlSession. To prepare the model, we rely on coremltools, Python, and Pytorch. For the backend, we use Python and FastAPI. This combination ensures that our app is both efficient and capable of processing data locally, maintaining user privacy while delivering real-time eye-tracking capabilities.
