---
title: "Week #5"
---

# **Week #5**

Due to us having a product, specialized for a well defined group of clients (Leroy Merlin website and their users), we cannot rely on the feedback from fellow students or any public survey options.

## **Feedback**
> Can a "Would you click this?" form be a feedback?
## **Improvements based on the received feedback**

## **Weekly progress report:**
Seeing as the project is now being finalized and prepared for deployment, our main goals for this week were to fix problems outlined in the last report and consider other resources for potentially making our UI look better and user-friendly.

### **Challenges, issues and solutions**

- **Little bugs and unpredictable behaviours**:  
  As the project grows bigger, the number of mistakes grows too. As an example, an hour of our teams time was wasted on a bug that caused the translation model to translate to the same language as the original message.  
  **Solution**: Debugging and cooperation between team members.

- **Security issues**:  
  Part of our code uses private keys to access Yandex's API, which cannot be shared publicly.  
  **Solution**: Store the API keys separatly in a file, that has to be added to the .gitignore or add the keys to the Python virtual environment and add access them from venv.

- **Docker and CUDA interaction**:  
  Using docker in the project comes with its own issues, namely the issue where docker doesn't recognize CUDA, required for launching models using GPU resources. This problem has been around since last week and caused us to postpone the deployment of our project.  
> can we please get an expert to the scene :)   
**Solution**: 

### **Conclusions & Next Steps**

## Potential improvements on report:
### one