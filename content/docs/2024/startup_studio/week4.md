---
title: "Week #4"
---

# **Week #4**

This week we successfully transitioned the website to a multi-page application using React Router, enhanced the backend with essential functionalities, and addressed significant challenges with migrations and metric accumulation.

## **Frontend Development**

We integrated React Router, which transformed our website into a multi-page application. Additionally, we created a page for projects and another for project creation.

![Welcome page](/2024/startup_studio/welcome_page.png)
![Project creation](/2024/startup_studio/project_creation.png)
<!-- 
Now in progress we have pages such as application creation and project info:

![Welcome page](/2024/startup_studio/application.png)
![Project creation](/2024/startup_studio/project_info.png) -->


## **Backend Development**

This week we implemented refresh token functionality and created an endpoint for it. We added a list of projects and applications, implemented project and application deletion functionality, and created endpoints to get application and project details. We also fixed migration issues, refactored the project, reviewed merge requests from the whole team, and made minor improvements and refactoring in the authorization process.

### **Cluster Manager**:

We developed API response models to improve the clarity and usefulness of our responses. Instead of returning simple success/failure messages, the API now sends links to resources when creating a project or application. We also wrote examples and schemas for response models to make it easier for frontenders to work with handles.

Initially, we aimed to write examples for the entire model at once, but found it more convenient to add examples for each field. This approach allows the general example to form automatically, applies aliases to the examples (e.g., target_port becomes targetPort), and automatically updates the example of the external model if the nested model changes.

Additionally, we decided to replace the return type of JSONResponse routines with Pydantic models and dicts. This change moves serialization and documentation to [FastAPI](https://fastapi.tiangolo.com/advanced/response-directly/#returning-a-custom-response), making the process more streamlined and reducing the need for developer intervention.

### **Monitoring System**:

We created dashboards for the entire cluster, namespaces, and nodes. This allows us to have a clear overview of the system's performance and health. Next week, we plan to add cAdvisor to the cluster to fully monitor containers, namespaces, and pods. With these dashboards, new users will also be able to monitor their applications.

![Namespace Dashboard](/2024/startup_studio/namespace.png)
![Namespace Dashboard](/2024/startup_studio/namespace2.png)
![Pods dashboard](/2024/startup_studio/pods1.png)
![Pods dashboard](/2024/startup_studio/pods2.png)

## **Challenges & Solutions**

**Migrations problem:**\
We encountered problems because we created new columns with constraints nullable=False in tables that already contained data, which broke the constraints and caused the migrations to fail. We solved this by rewriting the auto-generated migrations, first creating new columns, entering information into them, and then changing the constraints.

**Metrics Accumulation:**\
We had the difficulty with accumulating metrics for a single namespace and the lack of ready dashboard versions for our needs. We will resolve this by using [cAdvisor](https://github.com/google/cadvisor) for monitoring containers, namespaces, and pods, and by searching for similar dashboard variants, borrowing some graphics, and configuring them to fit our requirements.

**Token Refresh Endpoint:**\
We had an issue with the token refresh endpoint, where the refresh token was passed through the query, causing problems. We resolved this by changing it to pass through the body.

## **Plans for next weeks**

- Fix hover errors on all endpoints.
- Add cAdvisor to monitor everything in the cluster.
- Develop pages to display projects and applications.
- Implement handling for authorized users.
- Test the product with potential users to identify issues and gather recommendations.