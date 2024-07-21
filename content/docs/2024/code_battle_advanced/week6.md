---
title: "Week #6"
---

# **Week #6**

## **Presentation**:

To see the presentation that was created for this week, visit the static folder and look at w6presentation. 
To see the current state of the final presentation, go to [Google docs](https://docs.google.com/presentation/d/1UXhJAu-Q7oWhZ5ZF7qpS0KLGr2IJ6OhM6fKifUT5zjA/edit?usp=sharing).


## **Weekly Progress Report**:

Our team did:

- Ported the judgement procedure to a separate docker container for enhanced security.
- Ported all containers from Alpine to Debian Linux distributions because application written in Python work much better with Debian and may even cause the resulting image size to be less.
- Added contest management page.
- Misc fixes and features such as fixing not working links and adding file upload via drag and drop.
- Started and halfway finished reinforcing the project in terms of cybersecurity. 


### **Challenges & Solutions**

1. Despite our profound usage of dockers, creating another one was still tedious. Still, we persevered. 
2. The creation of a CI/CD pipeline is underway, but it requires a bit more time with parsing the html requests. 
3. It is very difficult to properly include a secure connection using HTTPS without paying anything. Ultimately, we decided to shelve that idea for now as there is no easy and free way to obtain a public IP address while the university has all routers inside of it behind a proxy. The website can, however, be accessed from inside the university.
4. It is very tedious to create secure sandboxes in Kubernetes on demand, since it requires accessing Kubernetes API from a container, making another bunch of config files and somehow relaying the data back to the original container. For this reason, we decided to just use another layer of docker containers inside the existing judgement container since it keeps the system nice and organised and is much easier to deal with.
 

### **Conclusions & Next Steps**

For the upcoming week we plan to finish the current work and test the project to present it. The current version of the presentation is barebones, so it will be a great focus of our work. Additionally, we need to figure out the plans for the deployment of our website, at least a temporary solution. On top of that there are still some vulnerability concerns, but they are on track to get fixed.

For the current state of the project, please refer to the [Github repository](https://github.com/IU-Capstone-Project-2024/code-battle-advanced). 


