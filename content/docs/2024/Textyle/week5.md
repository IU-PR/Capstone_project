---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

- **Feedback collection plan**

At this point of our project working prototype will be ready only during next week so considering our inability to get a feedback on our work we decided to conduct 4 customer development interviews about usage of this product. 2 interviews were with students from linguistic university and other 2 were with students from tech university.

Also we conducted a survey to recognise if people need it.

- **Conducted user surveys or feedback sessions**

This is the list of questions and main ideas of answers on each of them:
- What is the main purpose of using the text rephrasing service? 

  The main purpose is to improve the structure and language of the text.
- What kinds of texts do you typically want to rephrase?

  For students from linguistic universities essays and term papers. For students students from tech university reports and academic papers.
- How often do you use rephrasing services?

  For students from linguistic universities it needs several times a month. For students students from tech university couple times a month.
- What are your expectations from the rephrasing service?

  Paraphrased text with meaning preserved and readability improved.
- Which rephrasing formats are most important to you (formal, conversational, etc.)?

  Formal and academic
- What features or capabilities do you consider essential for a rephrasing service?

  Ability to choose different styles and level of formality.
- What difficulties do you encounter when using current rephrasing services?

  Lost of meaning of the text.
- How would you rate the importance of rephrasing quality compared to its speed?

  Quality is way more essential.

On survey we recived 51 answers. These are questions and results:

- How often do you need to write different types of text?

  11,8% - several times a month.
  
  35,3% - 1-2 times a month.

  35,3% - rarer than once a month.

  11,8% - never.
- How do you change text style? (multi-choice question)

  41,2% - using services.
  
  88,2% - by themselves.

  5,9% - asking a friend.
- If we suggest a product which can do this would you use it?
  
  41,2% - Yes.

  41,2% - would try.

  17,6% - no.


- **Analyzing feedback, identifying and prioritizing issues**

According to servey a lot of students will need this product. At this point our top priority is to finish the MVP and continue to improve the quality of the rephrased text. 
Also we got the idea that we can add levels of formality but this is not essencial right now.


## **Weekly Progress Report**:

**Frontend:**

Done: 

- Connected with a backend
- History (or account) page was implemented
- Dynamic routing and navigation were added 
- The requests to the server and responses from it have been properly handled (and tested)
- One bug in the scalability of the application by the change of the window size was fixed
- The user-friendly display of errors during the login/sign up process was added

Plans:

- Add functions at the account page (delete, clear history)
- Wait till the full connection with AI, test and fix some emerging bugs
- Implement more comprehensive error handling by adding additional checking to the JS files that are related to ProxiAPI (sending requests and receiving responses), implement an appropriate behavior of the project to the different errors and the situations when they could happen

**Backend:**

Done:

- Autorization token.
- Connected to frontend.

In progress:

- Completing the database to store the query history of each user.

Plans:

- Create proper handling of errors.
- Connect the model to server.
- Complete the database to store the query history of each user.

**AI:**

Done:
- Russian BPE tokenizer.
- Methods of changing existing tokens.

Plans:
- Model fine-tuning.
- Existing tokens replacement. Merge Russian BPE and existing Llama tokenizer.
- Embedding layer fine-tuning. Train on Ru + En wikipedia corpus.
- Connect with frontend.

