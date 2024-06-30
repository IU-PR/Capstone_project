---
title: "Week #4"
---

# **Week #4**

### Progress Report

During this week, we continued developing our first prototype. Our bot is now fully functional, with all basic functions implemented and major bugs related to connecting all three modules fixed. However, we are working on improving the quality of our recommendations, which currently need refinement. Additionally, we have started extensive testing of the bot to find and fix bugs. During the next iterations, we will focus on adding extra features and improving the bot's interface (buttons, hotel pictures, etc.).

---


### Challenges and Solutions

1. **LLM Deployment Issues**:
   - **Challenge**: Running the local LLaMA model requires significant GPU resources and presents challenges in deployment, making it difficult to scale and manage.
   - **Solution**: We realized the need to switch from a local LLM to an already deployed one, using REST API requests. This transition brought several challenges, including setting up a server and running our bot on the same server where the LLM is deployed, accessible via SSH connection.

2. **Remote LLM Regularly Being Down**:
   - **Challenge**: The remote LLM's frequent downtimes have significantly disrupted our development process.
   - **Solution**: We are considering alternatives such as utilizing more stable cloud-based LLM services or improving our infrastructure to better handle these downtimes.

---

#### Next Steps

In the next iteration, we plan to:
- Enhance the quality of our travel recommendations.
- Continue rigorous testing to uncover and fix any remaining bugs.
- Add extra features to the bot, such as interactive buttons and hotel pictures, to improve user experience.

---
