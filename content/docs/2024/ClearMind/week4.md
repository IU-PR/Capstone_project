---
title: "Week #4"
---

# Week #4

## **Testing, feedback integration, and continuous iteration**

Our team worked diligently this week to integrate feedback, refine our system, and make significant progress on both backend and frontend development.

### External feedback

This week, we asked our classmates to test the project. After the meeting, we highlighted several points that could be improved:

1. **Long Texts:**
    - **Observation**: The texts are excessively long.
    - **Advice**: During stressful situations, users in a panic may struggle to read lengthy texts effectively. We will make the texts more concise to enhance readability.
2. **Referral to Psychologist**:
    - **Observation**: The system immediately redirects users to a psychologist.
    - **Advice**: It doesn't fully address the user's problem before referral. We will implement a more thorough problem-solving process before suggesting professional help.
3. **Paragraph Information Breakdown**:
    - **Observation**: Information is not segmented into paragraphs.
    - **Advice**: This reduces readability and comprehension. We will structure information in clear, concise paragraphs to improve understanding.
4. **Repetitive Apologies**:
    - **Observation**: Every message starts with "I'm sorry" or "Apologies."
    - **Advice**: Users find this repetitive and annoying. We will eliminate unnecessary apologies to improve the user experience.

### Testing and narrowing the scope

1. **Technique Familiarity Check**:
    - **Observation**: The system asks if the user is familiar with a technique before applying it.
    - **Issue**: This approach is inefficient during crises.
    - **Example**:

        User: "I can't concentrate."

        System: "What five items do you see?"

        User: "Table, bed..."

        System: "What three smells do you notice?" etc.

        ![screenshot1](/2024/ClearMind/screenshot1.png)

    - **Recommendation**: The system should directly engage in the technique without preliminary questions.
2. **Key Phrases and Words Orientation**:
    - **Observation**: Difficulty in navigating key phrases and words for choosing technique.
    - **Issue**: Inefficient processing of key phrases affects the system's responsiveness.

    ![screenshot2](/2024/ClearMind/screenshot2.png)

    - **Recommendation**: Improve the system's keyword recognition and response capabilities.
3. **Message Field Persistence**:
    - **Observation**: Text in the message field does not disappear immediately.
    - **Issue**: Causes confusion for the user.
    - **Recommendation**: Ensure the text field clears promptly after sending a message.

    ![screenshot3](/2024/ClearMind/screenshot3.png)

4. **Context Retention**:
    - **Observation**: System fails after sending four messages and loses context.
    - **Issue**: Context dependency may disrupt the flow of interaction.
    - **Recommendation**: Enhance the system's ability to retain context over multiple interactions.

    ![screenshot4](/2024/ClearMind/screenshot4.png)

![screenshot5](/2024/ClearMind/screenshot5.png)

1. **Command Misinterpretation**:
    - **Observation**: System crashes on certain words perceived as commands (die, kill, sleep).
    - **Issue**: Misinterpretation of words disrupts functionality.
    - **Recommendation**: Improve word recognition algorithms to distinguish between commands and regular input.

    ![screenshot6](/2024/ClearMind/screenshot6.png)

    ![screenshot7](/2024/ClearMind/screenshot7.png)

2. **Branch Navigation**:
    - **Observation**: System breaks down if unable to say "I’m sorry".
    - **Issue**: Limited response flexibility.
    - **Recommendation**: Ensure alternative responses are available for various conversational branches.

    ![screenshot8](/2024/ClearMind/screenshot8.png)

3. **Question Asking**:
    - **Observation**: Does not ask questions.
    - **Issue**: While providing good advice, the system lacks interactive questioning to engage users.
    - **Recommendation**: Incorporate questions into interactions to make the process more engaging.

    ![screenshot9](/2024/ClearMind/screenshot9.png)

4. **Key Word Visibility**:
    - **Observation**: System fails if key words are not visible.
    - **Issue**: Reliance on specific keywords limits flexibility.
    - **Recommendation**: Enhance the system’s ability to interpret and respond to a wider range of inputs.

    ![screenshot10](/2024/ClearMind/screenshot10.png)

5. **Errors that occurs independently of context.**

![screenshot11](/2024/ClearMind/screenshot11.png)

![screenshot12](/2024/ClearMind/screenshot12.png)

### Iteration and refinement

**Backend & ML:**

- **System instruction improvement**: We enhanced the system instructions for the language model by incorporating data collected from our extensive research on various psychological techniques. This iterative process involved analyzing which techniques are most effective in different contexts and situations.
- **Model selection and deployment**: We selected a new open-source language model known for its improved performance and fine-tuned it with better domain-specific system instructions to better handle psychological scenarios. We also successfully deployed this model on Microsoft Azure.
- **Database schema design**: We created a new Supabase instance and designed a schema for vector database storage. The vector database enables more efficient and accurate retrieval of relevant information, better contextual understanding in conversation with the user and response generation by the language model.

**Design and Frontend**

On the fourth week out goal was to connect frontend and backend and finish the dialogue window's design implementation on frontend. We also spent time continuing to research into Next.js and its properties. We were able to finish dialogue page and start working on the title page, which is still in progress.

## Conclusions & Next Steps

This week's feedback and testing have highlighted several areas for improvement in our product's usability and functionality. The insights gained will guide our upcoming iteration phase, where we aim to refine the existing features and introduce new ones based on the feedback received. In the coming week, we plan to focus on the integration of the frontend and backend, finalizing the design of the title page, and further enhancing our language model's performance.

### Next Steps

1. **Implement Feedback Improvements**: Make texts more concise, structure information better, and reduce repetitive apologies.
2. **Refine System Interactions**: Improve keyword recognition, context retention, and command differentiation.
3. **Continue Frontend Development**: Complete the title page design and further connect it with backend functionalities.
4. **Conduct More User Testing**: Gather additional feedback to ensure the refinements meet user needs and expectations.
5. **Monitor and Iterate**: Regularly assess progress and continue iterating based on feedback and testing results.