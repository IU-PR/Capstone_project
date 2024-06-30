---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

    The project infrastructure consists of a full-stack web application designed for language learning through AI-assisted pronunciation tools. The frontend is built with Vue.js, leveraging Vuetify for a modern and responsive user interface, and uses Axios for API interactions. The backend is powered by Django, providing robust authentication, handling file uploads, and performing speech-to-text processing. Audio files are recorded on the client side, uploaded to the server for analysis, and evaluated against user-provided phrases. The application supports user registration and login, allowing personalized experiences and progress tracking. The system is designed to be extensible, with potential for adding multi-language support and advanced pronunciation features.

- **Backend Development**:

    The backend infrastructure of the project is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. It manages user authentication, file uploads, and speech-to-text processing. The authentication system ensures secure login and registration functionalities, with tokens stored in local storage for session management. File uploads are handled efficiently, allowing users to submit recorded audio, which is then processed and analyzed to provide feedback on pronunciation. The backend also includes endpoints for text-to-speech conversion, enabling users to hear and practice phrases. The Django server is configured to handle various API requests from the frontend, ensuring seamless communication and data exchange between the client and server. Robust error handling and logging mechanisms are in place to ensure smooth operation and quick troubleshooting.

- **Frontend Development**:

    The frontend of the project is developed using Vue.js, a progressive JavaScript framework known for its versatility and ease of integration. Vuetify, a Vue UI Library with beautifully handcrafted Material Components, is utilized to create a responsive and aesthetically pleasing user interface. The application features a series of interactive components, including text input fields, audio playback controls, and dynamic waveforms for visualizing audio recordings. Axios is used for making HTTP requests to the backend, ensuring efficient data fetching and submission. The user interface is designed to be intuitive, guiding users through the process of entering phrases, recording audio, and receiving feedback. Conditional rendering is employed to manage the visibility of components, enhancing the user experience by showing relevant actions and feedback at the appropriate times. The frontend is structured to allow easy extension and customization, supporting future enhancements such as multi-language capabilities and additional learning tools.


- **Data Management**:

    Data management in the project is meticulously handled to ensure data integrity and security. User information, including login credentials and progress data, is stored securely in the backend database, managed by Django's robust ORM. Audio files uploaded by users are temporarily stored and processed for speech-to-text and pronunciation analysis, then deleted to maintain privacy and reduce storage costs. All interactions with the backend, such as file uploads and data retrieval, are facilitated through secure API endpoints, ensuring encrypted data transmission. Additionally, local storage is used on the client side to maintain session tokens and user preferences, allowing for a seamless and personalized user experience across sessions.

- **Prototype Testing**:

    Prototype testing in this project is conducted through manual testing. We have asked our friends to test the application, providing us with valuable feedback on the user interface, ease of navigation, and overall user experience. This hands-on approach allows us to identify and address issues from a real user's perspective. While automated testing is planned for future development stages, the current focus on manual testing ensures that immediate feedback can be incorporated quickly to refine the prototype and enhance its functionality and usability before broader deployment.


## **Weekly Progress Report**:

We used a model for denoising audio and implemented some features to our web application.

We found phonemes pronunciation simulation based on MRI imaging of experts of phonemes pronunciation. 

This simulation will make it easier for the learner to mimic the right mouth movement to produce the more accurate phonemes, you can view their work [here](https://seeingspeech.ac.uk/ipa-charts/?chart=1])


<video width="640" height="480" controls>
  <source src="/2024/language_teacher/animation2.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>




**This is the MRI imaging for pronouncing  the IPA phoneme letter “p”**



<video width="640" height="480" controls>
  <source src="/2024/language_teacher/animation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**This is the simulation based on the  MRI imaging for pronouncing  the IPA phoneme letter  “p”**


We Also found and tested the whisper open ai ASR model which is an alternative to wav2vec2 if it didn't perform will on our tests.

Finally, we calculated a similarity measure of two MFCC signals to show the user the overall accuracy of his pronounciation but we still need to normalize it.


### **Challenges & Solutions**

* **Saving audio files:**
    - **Challenge:** Saving user audio in an usable format for the speech to text model was not working.
    - **Solution:** To fix this we implemented a function that adds metadata to the audio and makes it usable by the speech to text model.

* **Detecting letters:**
    - **Challenge:** The currently used speech-to-text library "speech recognition” only supports words (tokens). Single letters being pronounced are not being detected by speech-to-text.
    - **Solution:** We will use the wav2vec 2.0 model instead of the library to check the correctness of pronunciation in letters.

### **Conclusions & Next Steps**


- Integrating our forced alignment solution for checking the pronunciation correctness instead of character by character comparison.

- We should add the phonemes' letters  pronunciation video with the description of the pronunciation to the website.

- Evaluation of the best model to use “Whisper” vs “wav2vec 2.0” 

- Use our model instead of the speech recognition library.

- Work on the design of the website

- integrate the similarity measure on the website

- normalizing the similarity measure to a percentage to show the user his pronounciation accuracy
