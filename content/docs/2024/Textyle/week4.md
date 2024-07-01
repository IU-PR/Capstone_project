
# **Week #4**

Welcome to Week 4 of the Capstone Project! This week is dedicated to the crucial phases of testing, feedback integration, and continuous iteration. As you embark on iterative development on your projects, it is essential to understand the significance of these processes in ensuring the delivery of a high-quality, functional product that aligns with your original vision.


## **External Feedback**
At the moment we don't have a working prototype, so we decided to conduct customer development interviews with 2 students. One student is from linguistic university and one from tech university.

These some insights from interviews:

- Students in linguistic universities write essays several times a month so this feature will be very usefull for them.
- Students in tech universities write academic papers or essays rarely.
- Ability to quicly leave feadback about the work of model is necessary for improving future work.
- For students from teck universities model has to be able to work with terms.
- It could be good to add highlighting of changed parts so student will be able to see the fields for improvement in future tasks.


## **Testing**
Since we don't have a ready product yet, we decided to conduct test sales.

We told to 10 university students about our project and described some of possible ways of using it. For example to rephrase text to formal academic writing on Russian for academic essay and papers or to professional and respectful email format on Russian for writing to professors.

6 out of 10 students thought that this product can be useful for them during their study time. This is very impressive statistics telling that our product may be in demand for university students.

The estimated price comfortable for students was 3-5 dollars per month.


## **Iteration**
In our project we already changed the design of the site once. Also in future we will need to add more features. For example ability to leave a feadback for users on site or auto highlights in the text. 
Thats why we understand how important iteratinos are.

---
## **Progress reports**  
**Frontend:**

Done: 

Conducted the meeting with backend team and discussed the endpoints which are going to be feed(for AI/neural network), login and singUp. 

Also discussed the request format. Server will return you 3 fields:
- Status - code (error, like your token is outdated, wrong data, or everything is correct).
- Data - all the data.
- Message - text, we sent to the user, for example registration is correct.

Plans:

- Finish and test requests.
- Add authorization tokens.
- Add an account page with user history.

**Backend:**

Done:

- Meet up with frontend team and decided on andpoints and request formats.
- Change the data base connection. Now it is opened (no more temporary connections, they are pulled from connection pool and used same way as threads).
- Data base is now working in multithreaded mode.
- Server is now multithreaded.
 
Plans:

- Create proper handling of errors.
- Connect test python code to server.
- Connect the model to server.
- Complete the database to store the query history of each user.

**AI:**

Done:
- The datasets for fine-tuning are partially chosen. (You can check database here https://huggingface.co/datasets/ai-forever/MERA/viewer/rudetox).
- The method for fine-tuning is chosen. (You can look into details of this method here https://huggingface.co/blog/mlabonne/orpo-llama-3)
- Method for checking grammar in tokenisation was developed. It is method of replacing the least frequent tokens of the source tokeniser with tokens of the tokeniser for the target language.

Plans:
- Meet up with backend team and connect model to server.
- Continue fine-tuning. Feed dataset to model, track the results and compare them to the results of the previos week.

