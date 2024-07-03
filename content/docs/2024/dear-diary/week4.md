# Progress report / Week 4

## External feedback

Feedback is crucial for product development. To gather it, we created a survey with both short and long questions and asked our peers. Here are the questions and key insights.

### [Questions can be found in this Google Doc](https://docs.google.com/document/d/1M22KP7II5Llm-k8ytnodT2h_IwuQaESo_rkZug9sgvI/edit?usp=sharing)

### Key findings

Across various age groups, occupations, and educational backgrounds, respondents consistently expressed a keen interest in using the app multiple times per week. Key features like journaling with AI assistance, emotion recognition, and personalized feedback garnered significant attention. The overall feedback on the app prototype interface was positive, although concerns centered around the clarity of features such as mood tracking and the paramount importance of data privacy. Addressing these concerns, ensuring transparent data storage practices, and reassuring users about non-sharing of data with third parties are critical. Suggestions for improvement included implementing a dark mode for nighttime usability, enhancing user guidance through tutorials and feedback mechanisms, adding password protection for enhanced privacy, incorporating peaceful or meditational music, and potentially including breathing exercises or meditations.

### [Precise statistics can be found in this Google Doc](https://docs.google.com/document/d/1cdh-CbmJ8e9Eo_pd0nxy0rkButdFIeAYwYZFKAA_DbA/edit?usp=sharing)

---

## Testing

Unfortunately, our teammates participated in a conference this week, so we will only describe the testing procedure for now and conduct the actual testing later.

For testing Android version, we will use tools like Android Studio's built-in features and libraries like Robolectric and Espresso to generate and automate our tests. We'll set up JUnit and AndroidX test libraries in our build.gradle file and use Room's testing utilities for an in-memory database. For generating tests, we'll leverage Android Studio's code generation capabilities and employ Robolectric for unit tests and Espresso for UI tests, ensuring comprehensive coverage. This approach will allow us to efficiently create, run, and manage tests, ensuring our app's reliability and performance.

For the backend and AI components, we will use the pytest library to test all endpoints comprehensively. Additionally, we will manually review the outputs of the language model to ensure they are not harmful to users. This manual testing will be conducted through a review session of the model’s outputs on a large sample of inputs (over 200).

To test the iOS version, we will use Xcode’s built-in testing framework, XCTest. We will set up unit tests for individual components and UI tests to verify the app’s interface and user interactions. Tools like Fastlane will be likely employed to automate the testing process, ensuring efficient and consistent test runs. This thorough testing strategy will help us ensure the iOS app's stability and performance.

---

## **Iteration**

Based on external feedback, we've chosen to implement the following features, considering their complexity and utility:

For the MVP version, we'll introduce safety alerts regarding user information transparency and a brief onboarding process for app usage.

In subsequent releases, we plan to include app password protection, a dark mode, and meditation features. We've decided against adding music due to potential licensing issues.

---

## Challenges and solutions

This week's main challenge was scheduling meetings with participants to receive their questionnaire responses. We aimed to meet in person to gain a deeper understanding of their answers. Additionally, this approach was more comfortable for both us and the participants, as they are our friends and family.

To overcome the scheduling difficulties, we used the following strategies:

- **Flexible Scheduling:** Offer a variety of time slots, including evenings and weekends, using tools like Doodle or Calendly.
- **Advance Notice:** Give ample notice to participants to arrange their schedules.
- **Convenient Locations:** Choose meeting times and locations that are convenient for participants.
- **Group Sessions:** Combine participants with similar schedules into small group meetings.

---

## Next steps

This week, we plan to design insights from the survey, focusing on safety alerts regarding user information transparency and a brief onboarding process for app usage. Collaboration with the development team will be crucial to ensure these improvements are effectively integrated. Additionally, we will continue working on the implementation of both iOS and Android versions. 

### Priority List for This Week:

1. **Continue Development:**
    - Implement iOS version
    - Implement Android version
2. **Design Insights from Survey:**
    - Focus on safety alerts regarding user information transparency
    - Develop a brief onboarding process for app usage
3. **Team Collaboration:**
    - Work closely with the developers to integrate improvements
    - Ensure effective communication and coordination
