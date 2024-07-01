---
title: "Week #2"
---

# Hardware Team Report

## Tech Stack Selection

Maintainability and reliability are the most critical aspects for the
project's architecture. The customers of the project are demanding the
product that could be easily adapted to their requirements. Thus, to lay
the foundation for the project architecture we chose the modern and
stable framework, which perfectly suits industrial requirements.

-   ROS2 Humble, code written on C++/Python

> ROS2 is a preferable choice for industrial projects, a modern standard
> stack. We decided to use C++ to make it possible in the future to
> obfuscate the source code, before sending it to the customer, so the
> customer can use the code, but not steal it.

-   CAD (Solidworks, Siemens NX)

> Usage of the CAD model is convenient and important because it allows
> for precise planning, visualization, and testing of the robot\'s
> design before physical construction. This ensures proper fit and
> function of components, reduces errors, saves time and costs, and
> enables easy modifications and optimizations.

-   EasyEDA

> Usage of the EasyEDA is suitable because it simplifies the design,
> simulation, and manufacturing of electronic circuits by providing an
> integrated platform for creating different circuit schematics, while
> enabling easy and rapid prototyping.

-   Lidar sensors

> Usage of the Lidar sensors is crucial in our project, the movement of
> the robot in the environment is possible due to a created map of the
> terrain, which can be obtained with Lidar.

-   Camera sensors

-   Interfaces (CAN bus, RS485, USB, UART)

## Architecture Design

### Component Breakdown: 

-   Main controller

-   Motors driver

-   Motors

-   Batteries

-   Sensors(Lidar, Camera, IMU, UltraSonic,etc.[)]{.mark}

-   Chassis

### Data Management:

All parts of our system communicate through hardware interfaces. Visual
information from camera and Lidar sensors will be buffared for seamless
data transmission and processing. Drivers' current state will be stored
inside internal registers and would be easily obtained and overwritten
in case needed.

### User Interface (UI) Design:

Our project will have simple UI design due to the nature of our product.
On the top of the robot the big red button will be installed, allowing
it to make the emergency stop (as a last resort in emergency cases).
Also there will be a power button and LCD display, which would indicate
the battery charge status.

### Integration and APIs:

We use the ROS API. Here's the
[**[table]**](https://docs.google.com/spreadsheets/d/12NhludETQ2IaE7fxu59oZJm4TciK32dUEuHmFc2o4K0/edit?gid=0#gid=0)
of which API every sensors use, all of them are tested and implemented:

### Scalability and Performance:

Our project is designed to be a multi-functional platform. After working
on a basic model we can expand the robot to the client's wish so it fits
the environment. The usage of the CAN bus allows us to expand the amount
and variation of sensors & actuators without drastic changes in the
hardware solution.

### Security and Privacy:

PLC - controller ensures the safety of the robot from physical damages
caused by bumping into different parts of the environment. The durable
body will keep the insides safe. In the final product the impact of the
Software part on the Hardware should be encrypted to prevent hacking
attacks.

### Error Handling and Resilience:

All the information from every sensor will be logged. If an incident
occurs, the robot will initiate an emergency stop, all motors will be
automatically turned off and the log of the error will be sent to the
user.

### Deployment and DevOps:

For now we control the version of the ROS2 packages written by ourselves
through GitHub. In the future we will implement a script which allows us
to integrate our code with parts created by the Software team into a
Docker container and deploy it on the computer installed on the mobile
platform.

## Week 2 questionnaire: 

### Tech Stack Resources:

-   Automated Guided Vehicle Systems (2023, 2nd edition)

-   Mastering ROS for Robotics Programming (3rd edition)

-   ROS BASICS IN 5 DAYS - Entirely Practical Robot Operating System
    Training

-   Robot Building For Dummies

### Mentorship Support: 

Our mentor, Ruslan Damindarov, is integral to the AGR project. As our
hardware consultant, he provides essential expertise and ensures that
our team functions smoothly and efficiently. His contributions in the
project are highly valued.

### Exploring Alternative Resources:

-   [[https://index.ros.org/]](https://index.ros.org/) - ros
    packages index

-   [[https://www.slamtec.ai/wp-content/uploads/2023/11/SLAMTEC_rplidar_datasheet_C1_v1.0_en.pdf]](https://www.slamtec.ai/wp-content/uploads/2023/11/SLAMTEC_rplidar_datasheet_C1_v1.0_en.pdf) -
    Lidars datasheet

-   IMU (gyroscope/acceleration sensor) datasheet

-   Programmable Logic Controller hardware and programming manuals

-   Driver and motors datasheets

-   RealSense camera datasheets

-   Jetson Nano computer datasheet

-   [[https://www.roboteq.com/component/content/article/2-uncategorised/502-robonidec-agv2020-instructions]](https://www.roboteq.com/component/content/article/2-uncategorised/502-robonidec-agv2020-instructions) -
    example of platform geometry and implementation

### Identifying Knowledge Gaps: 

Even if our team does a great job distributing the workflow evenly and
fairly among every member, based on their knowledge and skills, there
exists obvious knowledge gaps in the group. One of them is the
Programmable Logic Controller workflow. Correct battery management and
battery management systems became another problem, which required
additional studying. The gaps in groups' knowledge are being resolved by
deep learning from different reliable sources and getting help from
peers and our mentor.

### Engaging with the Tech Community: 

As mentioned in the report for week 1, this project is inspired by
Robotics lab employees. Consequently, the Robotics lab provides us with
needed equipment and a place to hold meetings. Moreover, we also
discussed possibilities to use projects created by other Robotics lab
employees in our project (for example, we asked the team developing the
Follow-me mobile platform to test our SLAM on their robot).

### Learning Objectives: 

Since everyone is responsible for their own component, everybody already
has knowledge of their part or learned important information. That means
from a long term perspective we will get a learning objective while
working and testing in case if something out of hand happens, or we face
any problems, or we find a new unexpected task to solve. However, our
knowledge gaps are obviously our first priorities in learning objectives
for now.

### Sharing Knowledge with Peers: 

During the week we organized meetings and one of them was dedicated to
dividing tasks between everyone, so people can get the task they are the
most knowledgeable of or can handle. Moreover, all team members
communicated via Telegram to get information without having to wait for
meetings.

### Leveraging AI:

We used AI to help write the code for the ROS when unsolved problems
appeared, help identify and fix errors in other fields. However, for
collecting info about Hardware parts we used official documents because
we cannot trust AI with such delicate configurations and expensive
components.

## Tech Stack and Team Allocation

| Team member   | Task/Responsibilities   |
|------------|------------------------|
| Ahmed Abid (Lead) | Is responsible on overall chassis design and 3d cam performance |
| Mikhail Terentev | Technical assistant and responsible on IMU |
| Timur Islamov | Is responsible on batteries and their maintenance |
| Pavel Kuklin | Is responsible on schematics, motors and their drivers and also responsible on Lidar |
| Elina Murtazina | Technical reporter and responsible on camera and wifi module|
| Mohamad Nour Shahin | Is responsible on ultrasonic sensors |
| Andrey Yanov | Is responsible on Nvidia jetson |

Also except the responsibilities listed in the table everyone does CAD
models for their assigned part if it is not available on the Internet.

## Weekly Progress Report

We've met our expectations and goals for this week almost fully. But there
was some complications:

-   WiFi receiver is able to be connected to the Linux systems, however,
    it's a very complicated system to make it work at that stage of
    development. The question about implementation of the WiFi router in
    the build occurred. The idea will be discussed with Ruslan
    Damindarov, as he's the customer and the mentor of the project.

-   Creation of the CAD models takes more time than expected. CAD is the
    main goal in the WorkFlow for now since the work of the other teams
    is dependent on the development of the exact model.

-   HC-SR04 Ultrasonic sensors don't give strict values, need to find the way to fix this error.

-   Some small questions are on the way to be finalized with the customer.

Here's the diagram for 24v schematics: 
![24vScheme](/2024/HardwareOverlord100/24vScheme.jpg)
