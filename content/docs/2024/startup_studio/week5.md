---
title: "Week #5"
---

# **Week #5**

This week we completed the project page and resolved user authorization issues. On the backend, we improved project and application CRUD operations with better error handling. We also decided to revert to Prometheus for monitoring due to CAdvisor configuration challenges. Despite facing VM disconnection issues, we managed to overcome them and stay on track.

## **Frontend Development**
We finished the project page with applications and collaborators listing. Also resolved an issue where the frontend could not identify an authorized user. This fix is currently under testing.

![Project page](/2024/startup_studio/project_page.png)

## **Backend Development**

**Improved project CRUD operations.**\
When creating a project, all namespaces are added to the list, and it is checked that there is no name collision. If there is a collision, a 409 status code is returned. When receiving a project, a 404 status code is returned if it does not exist. Similarly, when trying to delete a non-existent project, a 404 status code is returned. If a project still has applications, a 400 status code is returned with a message indicating that the project still has applications. No longer return a 500 status code to the user.

**Improved application CRUD operations.**\
When creating an application, it is checked that there is no name collision, and if there is, a 409 status code is returned. When receiving a non-existent app, a 404 status code is returned, and the same applies to deletion. When interacting with a non-existent project specified in the handle path, a 404 status code is returned, ensuring that the project and application exist.

### **Monitoring System**:

We decided not to use CAdvisor due to issues with custom CRI and missing labels in Prometheus metrics. After considering the limitations and challenges with the embedded docker-shim in Kubelet, we decided to revert to using Prometheus and will display the resources provided by it. So we were in the process of restoring the previous monitoring settings.

## **Product Feedback**

**Beginner Usability:**\ 
Feedback indicated that beginners might find it difficult to understand how our product works. To address this, we decided to create a small documentation page where users can learn how to use our product, understand its functionality, and its purpose.

**Feature Requests:**\
Some users suggested adding more features, such as alerts on the application page or notifications sent via a Telegram bot. While we decided not to implement these features for the MVP, but we recognize their potential for future development.


## **Challenges & Solutions**

**VM disconnection:**\
We use cloud.ru to create VMs for our project. For some reason, there was an issue with our bonus points used for these VMs, which caused the VMs to be stopped. This resulted in significant downtime and lost productivity. To resolve this, we contacted cloud.ru support and had to wait two days for them to fix the issue and restore our VMs.


**CAdvisor configuration:**\
Decided not to use CAdvisor due to issues with custom CRI and missing labels in Prometheus metrics. The removal of the embedded docker-shim from Kubelet caused the kubelet's embedded CAdvisor metrics to break slightly. For custom containerd setups, adding --kubelet-extra-flags="--containerd=<path/to/containerd.sock>" into the k0s worker startup configures the kubelet embedded CAdvisor to gather metrics directly from containerd, thus obtaining the expected labels. However, this does not work when using Docker via cri-dockerd shim, and there are currently no easy workarounds for this. Future refactoring of kubelet to get container metrics from the CRI interface rather than directly from the runtime is being worked on as specified in KEP-2371. Until then, the only option is to run a standalone CAdvisor. So we decided not to use it.

## **Plans for next weeks**

- Add documentation page and application page.
- Continue working with role-base authentification.
- Integrate monitoring in application info (make dynamic links for users).
- Test our product to resolve any unknown issues.