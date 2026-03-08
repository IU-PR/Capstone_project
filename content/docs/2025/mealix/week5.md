# Practicum Project Summer 2025 Report 5
**Team mealix**  

---

## 1. Feedback  

### Session:  
- **Session 1** User A (20 years old student) noted that there is no price range control for cheaper recipes.   
- **Session 2** User B (a 25-year-old student) noted that the final answer is rather crookedly structured. The lines have strange tabs and extra spaces.
- **Session 3** User C (a 21-year-old student) noted that links to products from the pyaterochka catalog appear very slowly and the query "salt" was answered by "red beans". 


### Analyze:
 - **Problem 1** There are no necessary and important limitations. (Medium)
 - **Problem 2** Crooked text when displaying menus and recipes. (High)
 - **Problem 3** Slow loading of the store's catalog. (High)

## 2. Iteration & Refinement 
After the feedback, we: 
1. Add limitations to control price and energy value.
2. Fixed tabs in menus and recipes.
3. Fixed loading of products' links.


### Performance & Stability
Only that we fixed about time - is loading time of products. About 30s -> 5s.


## 3. Documentation
The project documentation includes Swagger for easy interaction with the API, a README with launch instructions, and basic JavaDoc to explain the key points of the code. Everything has already been implemented in accordance with the requirements, no additional improvements are required. Swagger is available at a standard address, the README contains the minimum necessary steps for deployment, and the JavaDoc covers the main difficult places. Everything is ready to use.

## 4. Deployment
We deployed the server on Ubuntu and created a separate user for CI/CD, generating an SSH key for him and configuring access rights. Dokker and Dokker Compose have been installed on the server to work with containers. To integrate with Git, we created an SSH key, added it to the repository, and registered the necessary secrets. The trigger branch was changed to main, and an .env file with environment variables was prepared on the server. These steps allowed you to set up automated application deployment.


---

## 5. Weekly commitments  

### Individual contributions  

**Alexander Kachmazov (ML):**  
- Added budget-based generation, and now going to format the parsed recipes with new ones and refine the rag.
- [Code link](https://github.com/IU-Capstone-Project-2025/mealix/commit/7461cdb0f412c493bbc53dc55c6e28033e28c4e1)  

**Samat Iakupov (Frontend):**  
- Put the domain on the deploy server, installed nginx and transferred it to https, there is no branch on github for this, and rewrote the telegram bot in python and rewrote the dockerfile for it.
- [Code link](https://github.com/IU-Capstone-Project-2025/mealix/tree/new-tg-bot)  


**Dmitrii Antipov (Backend):**  
- Did everything about deployment. (Part 3. Deployment) 
- Write javadoc
- [Code link](https://github.com/IU-Capstone-Project-2025/mealix/tree/backend_javadoc)  


**Danil Eramasov (ML):**  
- Add product-matching using vector representations and cosine similarity into the code and now bot is working faster.
- [Code link](https://github.com/IU-Capstone-Project-2025/mealix/tree/llm_agent_code)  

**Albert Shammasov (Data Analyst):**  
- Solved the problem of excessive reassembly of the Docker image for the ml service when the code did not change.
- [Commit link](https://github.com/IU-Capstone-Project-2025/mealix/compare/main...ml_dockerignore)  

### Plan for next week.

---

## 6. Confirmation of the code's operability  

We confirm that the code in the main branch:  
- Is in working condition  
- Can be run via docker-compose (or alternative method described in README.md)  