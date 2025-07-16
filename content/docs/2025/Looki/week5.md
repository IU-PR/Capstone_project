# Week #5

## Feedback

### Sessions

We conducted three testing sessions with people from our university and friends:

**Session 1:**  
   Tested by a classmate from 2-nd course. He wanted a feature to visually see how exactly the parameters are extracted from the photo for better understanding.

**Session 2:**  
   Tested by a friend from the university dormitory. She mentioned that the instructions for taking the photo were not very clear, which made it difficult to get good measurements the first time.
   
**Session 3:**  
Tested by a family member. They noted that the model almost correctly recognizes body parameters, but suggested reducing the generation time.

---

## Analyze

From the feedback, we identified the following main issues:
 
- **Visual feedback on parameter extraction (high priority):** Users wanted to see how the app extracts measurements from their photo for better understanding and trust in the results.  
- **Photo instructions clarity (high priority):** Lack of clear guidance led to poor photos and inaccurate measurements, making the first attempt often unsuccessful.  
- **Ability to retake photos (medium priority):** Users requested an easy way to retake photos if the first one was not satisfactory.  
- **Model generation time (medium priority):** Some users noted that the 3D model generation took longer than expected and suggested speeding it up or showing progress feedback.
- **Progress feedback (low priority):** Users suggested showing a progress bar or message during model generation.

---

## Iteration & Refinement

Based on the feedback, we made these changes:

- Added a “Retake Photo” button so users can try again if needed.      
- Worked on reducing the 3D model generation time and added a progress indicator during generation.  
- Fixed minor bugs and enhanced the profile settings screen for better usability.

Further testing with more users and continuous model improvement are planned.

## Performance & Stability

**How we measure performance:**  
- Time to generate a 3D model after uploading a user photo.
- Time to analyze a user’s photo to extract body parameters using the ML model.
- Average API response time under typical load.

**Current measurements:**  
- 3D model generation time (first run only): ~7 seconds.
- Photo analysis time (body parameters extraction): ~3 seconds.
- Average API response time: ~80–100 ms per request.

**How we tested it:**  
We manually measured the time required for the main operations during test sessions. Each step was timed multiple times to ensure consistency:
- Generating a 3D model from a photo takes about 7 seconds on average **on the first run only**.
- The 3D model does not need to be regenerated unless the user changes their body parameters.
- Extracting body parameters using the ML model takes about 3 seconds.

**Planned improvements:**  
- Optimize ML model loading and inference speed.
- Use asynchronous processing for parallel execution.
- Upgrade to a more powerful server, as the current one has minimal resources.



---

## Documentation

The project has the following documentation:
- **README.md** — Quick start guide, installation instructions, Docker setup.
- **API Documentation** — Describes available endpoints, authentication, and request/response examples, Swagger.

**Planned improvements:** 
- **User Guide** — Short manual for end-users on how to upload and view 3D models.
- **Developer Notes** — Instructions for developers on project structure, contribution rules, and testing.

---

## ML Model Refinement 

We use an ML model to extract body parameters from user photos.  
The pipeline uses OpenCV and MediaPipe to detect pose landmarks and calculate key base measurements (shoulder width `bia_di` and hip width `bit_di`), scaled by the user’s real height.  
These measurements, together with user input (weight, height, age, sex), are fed into a Random Forest Regressor to predict full body dimensions for 3D model generation.

The initial version of the model was trained on a small dataset. Based on real user sessions, we identified that accuracy needs to be improved to ensure more precise 3D model generation.

**How we refined the model so far:**  
- Implemented automatic landmark extraction for more reliable measurements.  
- Added a robust scaling mechanism to convert pixel values to centimeters.  
- Introduced a `StandardScaler` for input normalization and better model generalization.  
- Trained separate Random Forest Regressors for each body parameter.  
- Built an easy way to retrain the model if new data is available.  
- Deployed model versioning and safe loading with `joblib`.

**Planned improvements:**  
- Increase the training dataset by collecting verified body parameters from real user profiles (with user consent).  
- Add a feedback form so users can report inaccurate measurements directly in the app.  
- Use this feedback loop to retrain the model continuously.  
- Test the model on diverse edge cases (different body types, lighting, clothing).  
- Automate dataset updates and retraining to steadily increase prediction accuracy.

---

## Weekly Commitments

Nikita Shiyanov - Added new API endpoints for adding stores, started analyzing approaches for fitting clothes onto the 3D model, completed automated deployment to the server: now the project is built on GitHub, and only containers are deployed and automatically restarted on the server, fixed backend bugs, installed the MakeHuman project on the server to generate 3D models without needing to run the process locally on a personal computer.
Ilya Maksimov - added a diaper of a 3D human model according to user parameters and its update when parameters change
Aleksandr Gavkovski - migrated the project to new libraries, fixed bugs, improved the profile functionality, redesigned the body measurement flow, and added the option for users to retake their photo if needed


---

## Plan for Next Week

- Implement upload tutorial.
- Add access control feature (phase 1).
- Prepare for second round of user testing.
- Run performance tests with more load.
- Review Docker security best practices.

---

## Confirmation of the Code’s Operability

We confirm that the code in the main branch is:
- [x] Fully functional.
- [x] Runs via docker-compose according to instructions in README.md.

---

