---
title: "Week #3"
---

# **Week #3**

This week our team has been working on both the frontend and backend of our project. We prioritized finishing the authorization service and setting up monitoring, because we need a functional prototype by the end of the third week. In addition, we have started developing the cluster manager, which is one of the main components of our system. To monitor and help each other our team organized meetings several times this week.

### **Monitoring system**:

Regarding monitoring, we initially aimed to use Splunk but found it challenging to configure and not meeting our expectations. We switched to Prometheus, which offers more robust and ready-made solutions for cluster monitoring. We completed the configuration of Prometheus this week, and we now have fully functional dashboards in Grafana where we can monitor our namespaces. New user namespaces will also be displayed on these dashboards, allowing users to monitor their applications effectively.

![Grafana Dashboard](/2024/startup_studio/grafana_dashboard1.png)
![Grafana Dashboard 2](/2024/startup_studio/grafana_dashboard2.png)

### **Backend Development & Data Management**:

On the backend, we developed a comprehensive authentication service using FastAPI. This service handles user registration, login, and password hashing to ensure security. The primary feature of this service, user authentication, is nearly complete. The only remaining task is to integrate email confirmation to enhance account verification. For data management, we are utilizing PostgreSQL to store user information securely. 

### **Cluster Manager**:

For the cluster management service, we built the skeleton this week. This involved setting up essential modules, defining routers, establishing endpoints, and creating a repository structure. The logic of creating projects, as well as applications within these projects and their management was also prescribed.

### **Frontend Development**:

We successfully implemented the login and registration pages on the frontend. These pages are now fully functional and connected to the backend, allowing users to register and log in seamlessly.

![Main page](/2024/startup_studio/main_page.png)
![Login](/2024/startup_studio/login_page.png)
![Registration](/2024/startup_studio/registration_page.png)

### **Prototype Testing**:

You can take a look at our site yourself, but since we have everything running inside a virtual private environment, you'll need to follow a few simple steps to make it all work:

1) Install tailscale (you may need VPN or proxy to do it)
    
    For Linux **curl -fsSL https://tailscale.com/install.sh | sh**

    For Windows https://tailscale.com/download/windows

    For MacOS https://tailscale.com/download/mac

2) Connect to our VPN

    **tailscale up --auth-key tskey-auth-kZKWRrf2dD11CNTRL-LiVxGmRYbvF3krEfGPh8vFGUT45ELF5sa**

3) Go to our website

    http://babyhelm-front-svc.taila53571.ts.net/ 


### **Challenges & Solutions**

**Difficulties with metrics:**\
We use kube-system-metrics, of which we found only two versions. Each has its own disadvantages. One gives metrics for telemetry only, the other does not give detailed metrics for cpu usage and memory of pods. In the end we chose the second version, but we had to figure out how to convert the metrics that are available to us to the ones we need. To solve the problem we used PromQL.


**Dashboards customization:**\
There are no open-source dashboard solutions for Prometheus in Grafana. Having no example of dashboard configuration with prometheus, we had to manually investigate all possible metrics and how they will be displayed.

### **Plans for next weeks**

Looking ahead, our focus for next week includes:

- Creating a user account page for managing personal information and account settings.
- Developing an application deployment page for inputting Docker image details and project configurations.
- Continuing to build out the cluster management service with a focus on namespace control and resource allocation logic.
- Completing the email confirmation feature to enhance authentication security.