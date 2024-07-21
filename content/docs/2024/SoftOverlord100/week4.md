---
title: "Week #4"
---

# **Week #4**

## **External feedback**

During this week, we have gathered feedback on our project. 

1) Firstly, our mentor, Ivan Domrachev, reviewed our code and proposed some fixes and solutions: 

    <ul> 
    <li> For now, the switching between modes is not perfect. Implementation of the Behavior Tree would improve it.</li>
    <li> The current position might not be calculated accurately. Sensors Fusion need to be implemented to estimate the odometry based on all hardware devices the platform has (including sonars, encoders, IMU). </li>
    </ul>


2) Secondly, we have contacted another Robotics lab employee, Ruslan Damindarov. He is more involved with the Hardware part, so his insights would help us avoid problems with Hardware in the future. He had the following propositions:

    <ul> 
    <li> The functionality to store maps in the frontend and create virtual walls is desired, so we have to save the references to the map and virtual walls.</li>
    <li>Error handling needs to be added for the manual mode.</li>
    </ul>


3) Thirdly, we have contacted the potential customer, MagnitMarket (previously KazanExpress), to see if they approve the current implementation. The customer requested a functionality to add common routes to the memory, so that they do not need to be recomputed.


After getting all the external feedback, we understood that, even though our project solves the basic task it was created to do, we need to improve some features. 

&rarr; We need to change temporary solutions, such as switcher between modes, to more reliable ones. We need to implement the Sensors Fusion module and a feature of creating virtual walls. &larr;


</ul>

## **Testing**

We have tested both separate components of the project, as well as the project altogether. 

The SLAM algorithm is able to build the map without problems when data from lidars is provided.

The Path Planner builds acceptable routes to given points.

As for the project as a whole, we have encountered the problem with obstacles. Since no obstacle handling is implemented for the manual mode yet. We are aware of this issue and are going to work on it during the further development. 
*Note that we are still working with Simulation, and not actual Hardware.*

You can see some demo launches of the mobile platform moving, governed by the controller, and the robot navigating through the maps with virtual walls (as well as some bugs with navigation involving virtual walls).

[Link to video launches](https://drive.google.com/drive/folders/1zSW9OxTZn6WhHShu85cDUQWcQ2UZTH5S?usp=sharing) (The quality leaves much to be desired, but in the actual simulation, the robot's movements look better.)

## **Iteration**

We have the following plan for the iteration:

1) **Planning**: Every Tuesday we meet with our mentor, Ivan Domrachev, to get tasks which we have to do during the week
2) **Executing**: During the week, we work on given tasks, and meet to discuss problems we face, if needed
3) **Reviewing**: On Sunday we hold a meeting to discuss which tasks were done and which still require attention.
4) **Repeating**: Based on what has done, and on the speed of development, we create new plan for the next week.

During the development, we have encountered bugs and errors connected with ROS, especially, running it in a docker container, however, it is a normal situation in Robotics. 

With the help from other team members and our mentor, we were able to overcome most of them, and will continue working to mitigate the influence of these problems.

We stick to the initial plan and endeavor to implement Sensors Fusion and Behavior Tree blocks, of course, after we refine the modules we tested.

We are also listening to feedback we get from TAs, our mentor and other students, to get another point of view, and try to improve the project based on it. With the help of all those people, we will be able to create a truly exceptional project. We conduct meetings with our mentor, Ivan Domrachev, weekly, to share our progress and get an understanding of what will be done next.

## **Weekly progress report**

### **Goals**
1) Construct a demo by combining SLAM, path planner, and controller modules together;
2) Gather feedback from experts and fellow students;
3) Connect to Simulation part of the project;
4) Fix pipeline in GitHub;
5) Fix CI/CD;
6) Set up the plugin for handling virtual walls.

### **Challenges and Solutions**

- Connection of all the modules was not smooth, but it is a common situation in Robotics. Anyway, we fixed the bugs and got the navigation stack working properly. 
  
- While testing on a simulation, we found a bug in the Controller and fixed it. 

### **Conclusions and Next Steps**

During the next sprint, we are going to refine the navigation stack, virtual walls avoidance feature. Also, we are planning to implement a Sensors Fusion module and set up communication with the frontend. 

