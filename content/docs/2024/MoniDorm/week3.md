---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**: 

Currently, all the technical infrastructure for the prototype is ready. We deploy all microservices on remote virtual machines and support them using CI/CD. All pipelines run on self-hosted runners:
<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/Monidorm/self-hosted_runners.jpg">
</div>

Since all microservices run in Docker containers, it is easy to add new functionality without the problems of changing server infrastructure:
<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/Monidorm/docker_container.jpg">
</div>

We also follow the Git-flow approach in developing the code:
{{<mermaid>}}
gitGraph
  commit
  branch api-server
  commit
  checkout main
  branch telegram-bot
  commit
  commit
  checkout api-server
  commit
  commit
  checkout main
  branch frontend
  commit
  commit
  checkout telegram-bot
  commit
  checkout main
  merge frontend
  merge api-server
  merge telegram-bot
{{</mermaid>}}

- **Backend Development**: Start implementing the backend functionality of your prototype. This involves developing the server-side logic, ML model development, and APIs necessary to support the desired features. Focus on building the core functionality that will enable the primary user interactions and data management.

- **Frontend Development**: Begin developing the frontend components of your prototype. Use the wireframes created earlier as a guide and start building the user interface elements using appropriate technologies and frameworks. Pay attention to creating an intuitive and user-friendly interface that aligns with your MVP feature set. Make sure that you are implementing all main components. Secondary feature set can be postponed till second or third iteration. Prioritize functionality over appearance.

- **Data Management**: Implement the necessary data management capabilities for your prototype. This may involve setting up databases, designing data models, and implementing data retrieval and storage functionalities. Ensure that your prototype can effectively handle and manage user data as required by the prioritized features. Make it as simple as possible, but initial version of your database should do some basic operations from the MVP feature set.  

- **Prototype Testing**: By the end of the week 3, conduct initial rounds of testing to identify and address any usability issues or bugs in your prototype. Test the implemented features against the defined user flows and scenarios to ensure they function as intended. Collect feedback from your team members to gain insights and make necessary refinements to improve the user experience.

---

## **Progress report**:  
As a key deliverable for this week, we kindly request a progress report showcasing your first prototype. We understand that sharing code directly in the blog might not be preferable for everyone, so if you feel comfortable to provide a link to your prototype - this would be wonderful. However, if you prefer not to share the code publicly, we kindly ask you provide screenshots of your prototype to clearly illustrate the state of affairs.

The progress report should offer insights into the development process and highlight the significant milestones achieved during this week. It should include the following elements:

 - Prototype Features: Outline the features and functionalities that you have successfully implemented in your prototype. Include any core interactions, user flows, or data management capabilities that are essential to your project's goals.

 - User Interface: Showcase the user interface design of your prototype through screenshots or interactive prototypes. Highlight the key screens and explain how users will interact with your application. If your project has no UI elements, you may skip this part.

 - Challenges and Solutions: Share any challenges or obstacles you encountered during the development of your prototype. Describe how you addressed these challenges and provide insights into the solutions you implemented.

- Next Steps: Discuss your plans for the upcoming weeks and outline the features or improvements you intend to focus on. Create a priority list of features needed to be implemented. This will demonstrate your project's trajectory and provide a glimpse into the future development phases.

---