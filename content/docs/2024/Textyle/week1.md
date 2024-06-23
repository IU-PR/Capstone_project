---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID       | Email Address                      |
|--------------------------|-------------------|------------------------------------|
| Mikhail Tezin (Lead)     | @MikeTezin        | m.tezin@innopolis.university       |
| Nickolai Petukhov        | @Nickolaus_SDR    | n.petukhov@innopolis.university    |
| Ilnaz Magizov            | @mazik_il         | i.magizov@innopolis.university     |
| Borutya Igor             | @scrofx           | i.borutya@innopolis.university     |
| Mikhail Stepanov         | @MichaelStep      | m.stepanov@innopolis.university    |
| Yaroslava Bryukhanova    | @YaroslavaYara159 | y.bryakhanova@innopolis.university |
| Dmitrii Kuzmin           | @ikkiren          | d.kuzmin@innopolis.university      |

### **Value Proposition**

- Identify the Problem:
In lots of cases it's hard to explain your thoughts in the right manner and they need to be fastly paraphrase into needed style. 

- Solution Description:
Create site with pre-learned ML model for changing the text into needed style.

- Benefits to Users:
User will be able to clearly express his thoughts to other in the correct style.

- Differentiation:
Chat gpt is not always makes it good. Our ML will be trained specificaly for Russian language with big dataset.

- User Impact:
User will be understood by the reciever and no mishaps are going to apeare due to inappropriate style of the language.

- User Testimonials or Use Cases:
For example writing to the professor and being unable to write correctry in the formal style.

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address? 

   The software project addresses the need for users to easily and effectively paraphrase text into various styles, such as Characterisation, scientific style, official-business style, publicistic style, and conversational style. This can help users tailor their writing to different contexts and audiences.

2. Who are your target users or customers?

   The target users or customers for this software project could include writers, students, professionals, content creators, and anyone who needs to adapt their writing style for different purposes.

3. How will you validate and test your assumptions about the project?

   To validate and test assumptions about the project, user testing and feedback sessions can be conducted with a diverse group of users representing the target audience. This feedback can help identify any usability issues, preferences for certain styles, and suggestions for improvement.

4. What metrics will you use to measure the success of your project?

   Metrics to measure the success of the project could include user engagement metrics such as the number of paraphrases generated, user retention rates, user satisfaction scores, and feedback on the effectiveness of the different paraphrasing styles.

5. How do you plan to iterate and pivot if necessary based on user feedback?

   Based on user feedback, the project team can iterate by making adjustments to the user interface, improving the accuracy of paraphrasing in different styles, adding new features based on user requests, and addressing any issues identified during testing. If necessary, the project can pivot by focusing more on the most popular styles or making significant changes based on user needs and preferences. Regular feedback loops and continuous improvement processes will be essential for adapting to user feedback effectively.

## **Leveraging AI, Open-Source, and Experts**

Our team will analyse existing LLMs with open-source code and choose the most sutable one for future trainings.

## **Defining the Vision for Your Project**

Overview

The architecture involves a JavaScript frontend, a Rust Rocket backend, and a Python-based machine learning model. The frontend collects user input and sends it to the backend, which processes the data and directly interacts with the Python ML model to get predictions, then returns the results to the frontend.

Technologies Needed

Frontend:

- HTML/CSS

- JavaScript (with optional frameworks/libraries like React.js or Vue.js)

Backend:

- Rust

- Rocket framework

- PyO3 (for Rust-Python interoperation)

- reqwest (for making HTTP requests if needed)

ML Model:

- Python

- scikit-learn (or another ML library)

- joblib (for model serialization)

- maturin (for building Python extensions)

Build and Deployment:

- Cargo (Rust package manager)

- pip (Python package manager)

- Rocket.toml (Rocket configuration)

- Docker (optional for containerization)

Architecture Diagram:

+-----------------+          +-----------------+          +-------------------+

|  JavaScript     |  ---->   |  Rust - Rocket  |  ---->   |  Python ML Model  |

|  Frontend       |  ---->   |  Backend        |  ---->   |  (via PyO3)       |

|  (Client Side)  |  <----   |  (Server Side)  |  <----   |  (Server Side)    |

+-----------------+          +-----------------+          +-------------------+
Detailed Components and Communication
1. Frontend (JavaScript)
Technologies:

HTML
CSS
JavaScript (with fetch API for communication)
Functionality:

Collect User Input:
A form to collect user input.
JavaScript to handle form submission and make API calls.
API Calls:
Use fetch to send data to the Rust backend.
Display Results:
Display the results returned from the backend.

2. Backend (Rust with Rocket)
Technologies:

Rust
Rocket framework
PyO3 (for calling Python code from Rust)
Functionality:

API Endpoint:
Receive data from the frontend.
Call the Python ML model using PyO3.
Return the prediction to the frontend.

3. ML Model (Python)
Technologies:

Python
scikit-learn (or another ML library)
joblib (for model serialization)
Functionality:

Model Loading and Prediction:
Load the pre-trained ML model.
Provide a function to make predictions based on input data.

Deployment and Communication
Frontend:
Deployed on a web server (e.g., Netlify, Vercel).
Communicates with the backend via HTTP requests.
Backend:
Deployed on a server (e.g., DigitalOcean, AWS EC2).
Uses Rocket framework to handle HTTP requests and serve static files.
Calls the Python ML model directly using PyO3.
ML Model:
Embedded within the Rust backend.
No separate server needed.
Python code is executed within the Rust backend process.

*Feel free to add more sections as needed. You are the owners of your project!*
