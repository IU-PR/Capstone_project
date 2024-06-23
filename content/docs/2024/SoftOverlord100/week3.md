---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

### **Technical Infrastructure**:

We share our development process via Github. We have a docker container and plan to create a launch file, which will further combine all the components together. All components are developed in the submodules of the main repository, and the development takes place in additional branches.

The structure of the project is the following (dashed lines represent the components that are not mandatory):

![Schema](/2024/SoftOverlord100/backend_schema2.png)

### **Backend Development**:

We have successfully implemented the core components of the project: SLAM, Path Planner and Controller. Now they work on the mock data, since the Hardware team has not finished assembling the actual mobile platform yet. 

Each of the components has following functionalities:

  - ***SLAM***: simultaneously build the map and localize the robot on this map
  - ***Path Planner***: build a point-to-point the trajectory
  - ***Controller***: manipulate the hardware/simulation to gain the desired velocity
      We have also partially connected our part of the project with Frontend via ros bridge. Now the map, created by SLAM, can be displayed in a webpage. 

We have also partially connected our part of the project with Frontend via ros bridge. Now the map, created by SLAM, can be displayed in a webpage. 


### **Frontend Development**:

We focus mainly on the backend, which is a vast area that contains plenty of tasks. Consequently, our project does not have a permanent clear UI. However, we are producing an intermediate layer of data for visualization, which will be later designed in a more presentable for a user way on the web application. 

As already mentioned, a map, created by SLAM, can be visualized, both in a web page and using rviz.

![Map](/2024/SoftOverlord100/slam_map.jpg)


### **Data Management**:

We have successfully created a database, using MongoDB. The following information is stored in the database:
- the map, constructed by the SLAM algorithm;
- segments, which represent obstacles, “virtual walls”.  

### **Prototype Testing**:

Unit tests were conducted on each of the core components (SLAM, Path Planner, Controller) to ensure they work properly individually, before combining them together.

## **Weekly Progress Report**:

### Goals for the week

1) Develop the path planner module with nav2;
2) Set up rosbridge and test ros2djs for displaying the slam map;
3) Create the database;
4) Write a launch file for SLAM.

### **Challenges & Solutions**

The main problem, which we faced this week, concerned the ros-frontend communication. We successfully installed rosbridge; however the connection was not good (fast) enough. Also, we faced difficulties with displaying the map, but later we fixed them by rewriting the code and everything works as intended. 

### **Conclusions & Next Steps**

We have finished implementing SLAM, path planner, and controller. These modules successfully work for the mock data (since the hardware team is still working on the physical components, so we can not set up the communication with the robot yet). 

The SLAM map is passed to the frontend via websockets. This map will allow the users to see the environment surrounding the robot. Also, the map will display the robot’s position and obstacles in this environment. The visualization can still be improved, and we will investigate other ways to implement it.

We have the following plan for the next week:

1) Create an API that will deliver the data stored in the DB to the frontend and pass the data from frontend to backend.

2) Connect all the modules with each other and conduct integration tests.

3) &ast; If we are successful with the previous steps, we will start developing new modules, namely Sensors fusion and Behavior Tree. Sensors Fusion module might provide us with more accurate data about the robot’s position, while Behavior Tree will implement a high-level logic interface by distributing the commands to the subsequent modules. 

