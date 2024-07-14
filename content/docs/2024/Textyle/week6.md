---
title: "Week #6"
---

# **Week #6**

## **Presentation**:

https://docs.google.com/presentation/d/1_ugH1E313bctcsm5MgM7MVP4RIK3iKTSVjBW9vY09tU/edit?usp=sharing

## **Weekly Progress Report**:

**Frontend done:**

- Improved the account page by connecting it to the backend
- Implemented and tested user history retrieval and deletion
- Developed a notification system for user actions through tests and various attempts, enhancing the user experience
- Tested the text submission function for styling

**Backend done:**

- History storage bags fixed
- Clear history route
- All routes are connected with frontend

**AI:**

Done: 

- Made a comparison between two methods: fine-tuning and Instruction tuning, deciding that fine-tuning is the suitable one.
- Datasets prepared.
- Russian tokenizer is done.
- Tokenization time is decreased by 10%.

In progress:

- Fine-tuning
- Combining 2 tokenizers

### **Challenges & Solutions**

**Frontend:**

Challenge:

- One of the main challenges we faced this week was implementing the notification display for user actions. 

Solution:

- We experimented with many different approaches, striving for an aesthetically pleasing and functional solution. Through extensive testing and iterations, we developed our own solution that met our quality standards and worked effectively.

**Backend:**

Challenge:

- Design a way to store history of requests, which must be memory efficient, compatible with diesel and easy to use. 

Solution:

- Array of jsonb type. Jsonb is stored in bit representation on json, which allow faster read/write operations compared to regular json. Array type allows to load data partially, and that decreases response type from server and present more comfortable user experience(only last 5/10/20 e.t.c request are loaded at once, which result in faster response and less mess on the screen). Main issue with this decision is write operations. Diesel is currently not supporting array_append sql operation, and this forced us to created a custom sql command, which must me hardcoded into program so diesel can run this query

**AI:**

Challenge: 

- As we already use the Instruct model, not the baseline, we needed to fine-tune the instruct one. Despite a huge search, we barely found 2 tutorials how to implement it.

Solution: 

- After spending a lot of time, I've found the suitable article that helps in fine-tuning.



### **Conclusions & Next Steps**

**Frontend plans:**

- Add account deletion function to the account page
- Make final design adjustments

**Backend plans:**

- Load model to server

**AI plans:**

- Finish fine-tuning this week
- Replace the current model with the fine-tuned one


