---
title: "Week #2"
---

# Week #2

## Week 2 - Choosing the Tech Stack, Designing the Architecture

### Tech Stack Selection

1. Frontend (JavaScript)
Technologies:

HTML
CSS
JavaScript (with fetch API for communication)
Figma

2. Backend (Rust with Rocket)
Technologies:

Rust
Rocket framework
PyO3 (for calling Python code from Rust)

3. ML Model (Python)
Technologies:

Python
scikit-learn (or another ML library)
joblib (for model serialization)




### Architecture Design

1. Frontend (JavaScript):
- User Interface: Develop a user-friendly interface where users can input their original text and choose different styles for the output text.
- Text Processing: Implement functionality to send the user's input text to the backend for processing and receive the styled text back for display.
- Styling Options: Provide a selection of styling options such as font type, size, color, alignment, and other visual elements that users can customize.

2. Backend (Rust):
- API Endpoints: Create RESTful API endpoints to receive requests from the frontend, process the input text, and communicate with the ML model for generating styled text.
- Text Processing: Implement logic to preprocess the user's input text, pass it to the ML model for styling, and return the styled text to the frontend.
- Error Handling: Include error handling mechanisms to manage exceptions, validate input data, and provide meaningful error messages to the frontend.

3. Machine Learning Model (Python):
- Training Data: Collect and preprocess a diverse dataset of text samples with various styles to train the LLM.
- Model Architecture: Choose an appropriate LLM architecture (e.g., transformer-based models like GPT-3 or LSTM-based models) based on the complexity of styling required.
- Training Pipeline: Develop a training pipeline to train the LLM on the collected dataset using libraries like TensorFlow or PyTorch.
- Fine-Tuning: Fine-tune the pre-trained LLM on specific styling tasks to adapt it to the requirements of your project.


2. Data Management: 
Probably we will SQL.

3. User Interface (UI) Design:
There will be:
-Landing page.
-Text changing page
-Account page
You can have a first look at design of the site.

4. Integration and APIs: 

API Calls:
Use fetch to send data to the Rust backend.
API Endpoint:
Receive data from the frontend.

5. Scalability and Performance: 

For now our model is only scalable in Russia which is already a big market. 

6. Security and Privacy: 

There is going to be database with the users data but all of them are meaningless in most cases. But most likely we will impliment something for protecting this database. 

7. Error Handling and Resilience: 

 Include error handling mechanisms to manage exceptions, validate input data, and provide meaningful error messages to the frontend.

8. Deployment and DevOps: 

Frontend:
Deployed on a web server (e.g., Netlify, Vercel).
Backend:
Deployed on a server (e.g., DigitalOcean, AWS EC2).
ML Model:
Embedded within the Rust backend.
No separate server needed.

### Week 2 questionnaire:

1) Tech Stack Resources: 

At present, we are not utilizing project-specific books. Instead, we are heavily dependent on the documentation and resources offered by the frameworks we employ.

2) Mentorship Support: 
For now we don't have a mentor.

3) Exploring Alternative Resources: 
We use documentations of these blocks.

4) Identifying Knowledge Gaps: 
Frontend:
Learning the js again

Backend:
Learning PY03 for making ML - Backend relation.

ML:
Looking for suitable LMMs.


6) Engaging with the Tech Community: '
We didn't do that yet.

7) Learning Objectives: 
For our team the learning objects are:
- Figure out documentation problems
- Understand how to work with backlog properly


8) Sharing Knowledge with Peers: 
During the project we set ut meeting time by time and think about global problems of our project. But in most cases we solve the problem in private menner.


9) Leveraging AI: 
For that point in project we didn't rely on AI for making code.

### Tech Stack and Team Allocation


| Team Member           | Track               | Responsibilities                              |
|-----------------------|---------------------|-----------------------------------------------|
| Mikhail Tezin (Lead)  | Project Manager     | Team leading\reports                          |
| Ilnaz Magizov         | Backend             | Connecting LLM model with site                |
| Borutya Igor          | Backend             | Connecting LLM model with site                |
| Dmitrii Kuzmin        | ML                  | Finding and making contributions to LLM model |  
| Yaroslava Bryukhanova | ML                  | Finding and making contributions to LLM model |
| Nikolai Petukhov      | Frontend            | Site design                                   |  
| Mikhail Stepanov      | Frontend            | Site design                                   |

### Weekly Progress Report
Frontend:
- Design of the whole project 
- Architecture (pages and navigation)
- Two main pages were implemented in React 
- Proxy system to optimize sending requesr to server
- design on Figma here https://youtu.be/7X4nBLeaD7c

Backend:
- Server is up on local host
- Endpoint to exchange jsons working in single thread
- Json data exchange prototype is ready

ML:
- Analyze of the existing models


### Challenges & Solutions

Frontend team remade design several times due to dissatisfaction of the product by the other members of the team.

### Conclusions & Next Steps
For the next week:

Frontend:
- Implement other pages 
- Communicate with the Backend team to find the appropriate way to define a format of .json files and to exchange them (requests and responses)

Backend:
-Researches on PyO3
-Async endpoint
-Researches on threadpool

ML:
To do during the next week:
- Prepare benchmarks for the model
- Create the prototype of the AI side
- Model fine-tuning
