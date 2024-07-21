---
title: "Week #1"
---

# Week #1

## **Presentation**:

{{< embed-pdf url="/2024/SoftOverlord100/presentation.pdf" >}}

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Ekaterina Mozhegova (Lead)     | @fire0Foxy | e.mozhegova@innopolis.university |
| Iurii Podkorytov            | @yurapodk | i.podkorytov@innopolis.university |
| Mukhammadrizo Maribjonov            | @rizo_net | m.maribjonov@innopolis.university |
| Yehia Sobeh           | @Yehia_Sobeh | y.sobeh@innopolis.university |
| Ali Hamdan            | @mralihamdan | al.hamdan@innopolis.university |
| Anastasiia Shvets | @Anaf_karf | a.shvets@innopolis.university |
| Saveliy Khlebnov | @SaveliyH | s.khlebnov@innopolis.university |

### **Value Proposition**

- Identify the Problem:

In the modern times, manual labor is being replaced by robots in different spheres of life, one of them being transportation of materials. Since human’s speed and carrying capacity is limited, transportation of materials manually is time-consuming. However, with robots, human labor is no longer needed in this field. Nowadays, industry is rapidly developing and incorporating robotized solutions, so the expansion of the mobile platform market is relevant. Unfortunately, the existing solutions are either unavailable in Russia, or are still in development. Moreover, such robotic solutions are usually catered for certain companies, not for the general market. 

- Solution Description:

We will build a mobile platform to optimize productivity in logistics and manufacturing operations. Our solution will be cheap and easily adaptable for the Russian market. Moreover, our aim is to create a general-purpose model with the potential of further integration into specific areas. 

- Benefits to Users:

Our solution will be cheaper than the most existing ones. Moreover, we aim to design a robot which can be adapted to any area of industry, rather than creating one for a certain company. Also, we will try to create a robot which can be easily maintained and repaired.


- Differentiation:

Similar projects are being developed in Russia, China and Europe, so we will compare our solution to the existing ones from these regions. 

The main benefit of our solution is its universality: it can be used in different environments. Most of the solutions existing in Russia are created for certain companies and with certain functionality in mind. We, on the other hand, will try to create a general-purpose mobile platform, which can be easily integrated into any desired location. 
Another benefit is maintainability and security, compared to Chinese solutions. Most of the Chinese solutions cannot be easily altered and repaired on site, and have to be sent to the manufacturer. Our solution should be more flexible and require little to no guidance from actual developers. Moreover, Chinese solutions cannot be controlled from the local servers, further increasing their dependency from the manufacturer, and decreasing security and, consequently, the number of potential customers. Furthermore, the language barrier makes communication hard, making the necessity of long-term support even more troublesome.

Moreover, our solution is more reliable compared to European ones. Most of the European solutions are not accessible in Russia, and the ones which are may easily lose support, since European companies may refuse service to Russian companies with little to no notice, making use of cloud services risky. 


- User Impact:

The main benefit our solution will bring to users is automatization of certain areas of production, where human labor is not the most effective solution, so precision-requiring tasks can be prioritized instead.

- User Testimonials or Use Cases:

The most obvious use case is when some warehouse worker needs to transport a box from one part of the warehouse to another. With our solution, he should just have to input where he wants the mobile platform to go, and the box will be transported.

Another possible use case is when such a box needs to be transported from point A to point B every day at a certain time. In that case, the worker should have to input the path only once, and then only put the box on top of the robot every time.


## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address? 
   
Our project addresses the problem of automatization of transportation in industry. Currently manual labor is required in many warehouses in Russia, since existing solutions are only in development, or require substantial investments.

2. Who are your target users or customers?

We target both industrial companies, such as Magnit Market (Kazan Express), which need automatized solutions for big warehouses, and personal users, who may want to make certain parts of their lives, such as, for example, carrying documents around offices, easier.

3. How will you validate and test your assumptions about the project?

We target both industrial companies, such as Magnit Market (Kazan Express), that need automatized solutions for big warehouses, and personal users, who may want to make certain parts of their lives, such as, for example, carrying documents around offices, easier.

We have already contacted potential customers from Magnit Market (Kazan Express) and Gazprom, and they were interested in such a product.

We will get the main feedback from our Experts (see Experts section), and we will alter our project accordingly. 

4. What metrics will you use to measure the success of your project?

We can use the following metrics for our project:

- Accuracy and error rates
- Frequency of external manipulation needed
- Improvement in time and cost efficiency

5. How do you plan to iterate and pivot if necessary based on user feedback?

We plan to give users a way to provide consistent feedback at every stage of integrating and using the solution, to see which parts of the project need improvement. We aim to remain open to changes and alterations based on the feedback, since the main point of our project is to be flexible and adaptable for any environment or circumstance.

## **Leveraging AI, Open-Source, and Experts**

### Leveraging AI

We will attempt to incorporate AI into different parts of our project. For example, AI can be used in Simultaneous Localization And Mapping (SLAM) to build maps of the environment and locate the mobile platform within it. Moreover, most Path Planning algorithms incorporate AI for optimization in some shape or form, the simplest example being A* algorithm, that can be considered AI. For now, we are exploring different approaches to using AI. 

### Open-Source

Our solution may require insights from similar projects. Moreover, since our project is done separately by four different groups (see more in Defining the Vision of Your Project - Overview), we may have to test the Backend part on already existing simulations. For example, we found the [AgileX](https://github.com/PurplePegasuss/agilex_scout_mini) project on GitHub, and plan to use it as an inspiration and test for our project. However, since we use a different technological stack, we will build the solution ourselves.

### Experts

This project is heavily inspired by senior Robotics lab employees, specifically Ivan Domrachev and Ruslan Damindarov. Specifically for the Software part of the project, Ivan Domrachev will guide us. The experts provide us with a general view of the project architecture that can be adapted for industrial requirements. We consult with them about technical stack and they provide us with feedback about our implementation of the main modules of the project. In the long-term perspective, the experts will also help us to find potential customers and establish communication with them.

## **Defining the Vision for Your Project**

### **Overview:**

The main goal of our project is to create a mobile platform and user-friendly software to control it. This project is aimed to solve the problem of material transportation in enclosed spaces, since now mainly humans are engaged in this sphere. Our project will provide a cheap roboticized solution, so that human workers can solve more important tasks.
Our project will be divided into 4 parts, constructed by different teams.

- Frontend part (1st year students) - the UI used to manipulate the robot
- Software part (2nd year students) - the code which will perform kinematic computations, SLAM and path planning
- Simulation part (1st year students) - the emulation of mobile platform on the computer with API identical to actual mobile platform
- Hardware part (2nd year students) - the actual real-life mobile platform with stable API

Our team will specify the Software part of the project, specifically the Backend. We will create the Backend compatible with Hardware/Simulation and Frontend parts of the project, so that they will not have to worry how exactly the algorithms are implemented on our part. Our part of the project will consist of the following parts:

- Simultaneous Localization and Mapping - algorithm to build a map of the environment with the obstacles around and understand where the mobile platform is located within this environment based on the data from the mobile platform. SLAM should support two modes: 
    1. Localization + Mapping, when Map is build 
    2. Only Localization, when Map is taken from memory or Database
- Path Planning - algorithm to build a path from the current location of the mobile platform to the desired one based on the given map and current position and velocity. Ideally, functionality to add custom obstacles, not detectable by platform itself, should also be added. 
- Controller - robotic software to control the mobile platform in a way to ensure it follows the desired direction based on the path created by the path planner, based on the API provided by Hardware and Simulation teams. The Controller should not care if the mobile platform is real-life or simulated.
- Sensors Fusion - the robotic software able to get information from different sensors of mobile platform and transform it into the approximate position, velocity and acceleration of the platform
- Database (Optional) - the database where maps and possible paths can be stored to not build them every time
- Behavior Tree (Optional) - the software which manages the behavior of the system, for example, specifies state transitions.


### **Schematic Drawings:**

![Schema](/2024/SoftOverlord100/backend_schema.png)

### **Tech Stack:**

- ROS2 Humble based on C++
  
  ROS2 is a preferable choice for industrial project, a modern standard stack.

- Docker
  
  Docker will make it easier to run the software on any platform. It allows to change hardware without having to redesign architecture

- SLAM tools
- Path Planning tools

## **Weekly Progress**

### **Objective**

The objective of the first week was to establish a team for the project and choose the project idea which will be both complex enough and reasonable to expect an MVP after only 6 weeks. We also had to create the GitHub repository for both the project itself and reports. This week is really important for the overall project since we have to understand what we actually want to do and how our view of the project can be brought to life.

### **Results and Challenges**

We have successfully found the full team and divided the responsibility for the project within our team. We divided the team in a way that at least one Robotics student works on the component which requires understanding of fundamental concepts. We have come up with the following tasks distribution:

- SLAM: Iurii Podkorytov, Ali Hamdan
- Path planning: Ekaterina Mozhegova, Yehia Sobeh
- Controller: Mukhammadrizo Maribjonov, Saveliy Khlebnov
- Report: Anastasiia Shvets

This way the Robotics students (Iurii, Ekaterina, Mukhammadrizo) can help with some complex Robotics concepts.

Some of the students already started getting acquainted with required tools and setting the needed software.

### **Conclusion and Next Steps**

We successfully established the team and workflow for the following project. For the next week, we plan to start working on the project and define actual algorithms and APIs which will be used for every part of the project.