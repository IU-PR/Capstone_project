---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

- **Feedback collection plan**

We have made a few manual tests of the websites from students and an expert in UX/UI. We gathered valuable feedback for future work enhancements.

- **Conducted user surveys or feedback sessions**

We are planning to make a google form for user experience after we host our platform.

- **Analyzing feedback, identifying and prioritizing issues**

When we will collect feedback from users, we will identify and prioritize issues on which we should work.

## **Roadmap**:

- **User Feedback Integration**
    **Current State:** Initial feedback mechanisms.
    **Future Work:** Implement a more comprehensive user feedback system to gather insights on pronunciation accuracy and user experience. Use this data for continuous improvement.

- **Real-Time Pronunciation Assessment**
    **Current State:** Batch processing of pronunciation data.
    **Future Work:** Upgrade the platform to support real-time pronunciation assessment and feedback, leveraging fast inference techniques and edge computing where applicable.

- **User Interface and Experience**
    **Current State:** Basic UI/UX.
    **Future Work:** Enhance the user interface to make it more intuitive and user-friendly. Add features like visual aids for pronunciation and progress tracking dashboards.

- **Integration with Educational Platforms**
    **Current State:** Standalone application.
    **Future Work:** Integrate the platform with major educational platforms and LMS (Learning Management Systems) to reach a broader audience and provide seamless learning experiences.


- **AI Model Enhancement**
    **Current State:** Basic models for phonetic translation and comparison.
    **Future Work:** Improve AI models for better accuracy in phonetic translation and comparison. Incorporate state-of-the-art models like wav2vec 2.0 for enhanced speech recognition capabilities.

## **Weekly Progress Report**:

Our team did…
- Enhanced the user experience and the user interface: 
- Added a landing page, separated the sections in different pages.
- Added design for login and registration and profile page.
- Introduced a drawer on the left that allows for easier navigation of the website.
- Found and manually tested the phonemes model (audio to phonemes).
- Designed the pipline of the initial pronounciation correction feature.

### **Challenges & Solutions**

Choosing a layout for the landing page. 
Encountered issues with the color settings of vuetify. We skipped changing the colors until later. We decided to focus on adding functionalities for now.
The user usually forgets to press "stop recording" button, so We will add an algorithm to stop the recording when it is silent for some time

### **Conclusions & Next Steps**

We concluded that the new design is better for understanding the main functionality of the website. 
The ML model is working well generaly as we tested it manually for now.
The ML model also works on characters so no need to implement some wav similarity measure to classify characters.


**For the frontend:**
Choosing a fixed color palette to use for the website, and finding media to display that would enhance the user experience.

**For the ML part:**
We should find the best comparison algorithm between the true phonemes and the predicted phonemes.( For now we have longest-common-subsequence).
We should make a full pipeline to be able to test all the parts that we have automatically and evaluate our model.
Add the algorithm to stop the recoding when the user is not speaking.