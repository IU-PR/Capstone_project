---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

### **Feedback collection plan**

Our plan for collecting feedback is the following: 
- Show our current implementation to the person providing feedback 
- Let them test it in predefined environment
- Ask them to perform the following:
    - Make platform build the map of its surroundings
    - Ask the platform to get to a certain point
    - Switch to manual mode and try controlling the platform
- Get feedback on the following:
    - Simplicity of usage
    - Accuracy of platform movements (did it reach the desired destination, did the robot movements reflect what the user told them to do in the manual mode)
    - Accuracy of the map building (is the map built by the platform similar to the environment surrounding it)
  
We mainly focus our attention on students, implementing other parts of the project (Frontend, Hardware, Simulation) while getting feedback, as well as on mentors. However, we also asked some non-robotics related students to test our application to understand what people, who are less exposed to Robotics, may struggle with. Especially, it concerns frontend use cases, which have impact on our API implementation.

Unfortunately, algorithmic ways of feedback collection do not suit our project, since our current version of the product is not quite user-friendly and accessible to anyone, since
1) Our project is only a part of the broader one. Consequently, other parts of the project have to be implemented in order to test everything altogether. (For now, functionality, which is not implemented by other teams yet, is replaced by dummy data)
2) To fully test all the components of our software, users need to clone the repository and run it in a docker container, which is not the most convenient and easy way for users (though, the most convenient and easy way for us &#x1F643;).

Consequently, we are focusing on one-to-one feedback sessions.


### **Conducted user surveys or feedback sessions**
Every Tuesday we organize a feedback session with our mentor, Ivan Domrachev. During these sessions, we show our progress and current state of the project. 

During this week we also held additional feedback sessions with other respondents, to get more insights on what can be improved in the project. We have documented the feedback to better understand what can be improved.



### **Analyzing feedback, identifying and prioritizing issues**

After analyzing the feedback, we have identified the following issues:
1) The autonomous mode is not quite user-friendly for now, since users need to run several launch files separately. To make the launch of the program more convenient and fast, we are working on combining all the components together into a single service, which can be launched via a single command. 

2) The manual mode is quite complicated for a common user. With the current version of frontend, users need to enter the velocity data in the format, which is not very intuitive: 
   
`[linear.x, linear.y, linear.z, angular.x, angular.y, angular.z]`. 

On the web page it looks like this:

![Schema](/2024/SoftOverlord100/test_frontend.jpg)

One way to simplify the interaction for the user is to implement a controllable joystick, which will transform the direction pointed by the user into the required format itself.

## **Roadmap**:

After the end of the Capstone Project course, we will continue working on our product. We plan to divide the development into two tracks:
1) Improvement of the current backend (plan to finish before September)
- Improve Frontend-Backend communication
- Develop logs filtering, so that the user will be able to see error logs when emergencies happen to the robot
- Refine the method for map rendering with the virtual walls
- Implement Behavior Tree - a more advanced way to switch between different scenarios
- Implement Sensors Fusion module for a more accurate position estimation for the platform
  
2) Add new features connected with multiple robots co-operations (plan to finish before November)

## **Weekly Progress Report**:

The goals for this week were:
1) Fix navigation module
2) Add virtual walls
3) Start creating documentation for the project

### **Challenges & Solutions**

We have encountered the problem with Path Planner on the Simulation module. 
The current location of lidars created complexity in handling the data. We need to find a way to merge data from several lidars to a single topic and implement it. 

Frontend-to-Backend communication via websockets turned out to be challenging. We need to add new interfaces to ensure the safe messages transfer from Frontend to Backend. 

The polygon rendering is also a complicated task. For now, we simplified it to the task of rendering the non-detailed maps via points. 

### **Conclusions & Next Steps**

We need to refine some technical details, then connect all the parts of the project together, and make launching the project more user-friendly.
Thus, before the final presentation, we plan to:
1) Merge the lidars into a single topic
2) Connect all parts of the project together
3) Develop documentation for the project
