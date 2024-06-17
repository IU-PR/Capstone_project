---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Ahmed Abid (Lead)     | @Ahmed_fluffy | a.abid@innopolis.university |
| Mikhail Terentev            | @MiTerentev | m.terentev@innopolis.university |
| Timur Islamov            | @it_is_ti | t.islamov@innopolis.university |
| Pavel Kuklin            | @guestKP | p.kuklin@innopolis.university |
| Elina Murtazina            | @NA_Nevermind | el.murtazina@innopolis.university |
| Mohamad Nour Shahin | @Mohamad_Nour0 | mo.shahin@innopolis.university |
| Andrey Yanov | @Anr_y_an | a.yanov@innopolis.university |

### **Value Proposition**

- **Identify the Problem:**

    In the modern times, manual labor is being replaced by robots in different spheres of life, one of them being transportation of materials. Since human’s speed and carrying capacity is limited, transportation of materials manually is time-consuming. However, with robots, human labor is no longer needed in this field. Nowadays, industry is rapidly developing and incorporating robotized solutions, so the expansion of the mobile platform market is relevant. Unfortunately, the existing solutions are either unavailable in Russia, or are still in development. Moreover, such robotic solutions are usually catered for certain companies, not for the general market. 

- **Solution Description:**

    We will build a mobile platform to optimize productivity in logistics and manufacturing operations. Our solution will be cheap and easily adaptable for the Russian market. Moreover, our aim is to create a general-purpose model with the potential of further integration into specific areas. 


- **Benefits to Users:**

    Our solution will be cheaper than the most existing ones. Moreover, we aim to design a robot which can be adapted to any area of industry, rather than creating one for a certain company. Also, we will try to create a robot which can be easily maintained and repaired.

- **Differentiation:**

    Similar projects are being developed in Russia, China and Europe, so we will compare our solution to the existing ones from these regions. 

- **User Impact:**

    The main benefit of our solution is its universality: it can be used in different environments. Most of the solutions existing in Russia are created for certain companies and with certain functionality in mind. We, on the other hand, will try to create a general-purpose mobile platform, which can be easily integrated into any desired location. 

    Another benefit is maintainability and security, compared to Chinese solutions. Most of the Chinese solutions cannot be easily altered and repaired on site, and have to be sent to the manufacturer. Our solution should be more flexible and require little to no guidance from actual developers. Moreover, Chinese solutions cannot be controlled from the local servers, further increasing their dependency from the manufacturer, and decreasing security and, consequently, the number of potential customers. Furthermore, the language barrier makes communication hard, making the necessity of long-term support even more troublesome.

    Moreover, our solution is more reliable compared to European ones. Most of the European solutions are not accessible in Russia, and the ones which are may easily lose support, since European companies may refuse service to Russian companies with little to no notice, making use of cloud services risky. 


- **User Testimonials or Use Cases:**

    The most obvious use case is when some warehouse worker needs to transport a box from one part of the warehouse to another. With our solution, he should just have to input where he wants the mobile platform to go, and the box will be transported.

    Another possible use case is when such a box needs to be transported from point A to point B every day at a certain time. In that case, the worker should have to input the path only once, and then only put the box on top of the robot every time.


## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. **What problem or need does your software project address?**
   
   Our project addresses the problem of automatization of transportation in industry. Currently manual labor is required in many warehouses in Russia, since existing solutions are only in development, or require substantial investments.

2. **Who are your target users or customers?**

   We target both industrial companies, such as Magnit Market (Kazan Express), that need automatized solutions for big warehouses, and personal users, who may want to make certain parts of their lives, such as, for example, carrying documents around offices, easier. We have already contacted potential customers from Magnit Market (Kazan Express) and Gazprom, and they were interested in such a product.

3. **How will you validate and test your assumptions about the project?**

   We will contact potential customers to see if they are satisfied with the proposed solution, or their vision is not fully reflected. We will use qualitative surveys for that purpose, since they provide a way to give open answers, which may highlight new insights for the project. We will also test our solution in a real-life setting, analyzing how well our solution performs in such an environment. 
   
   We will get the main feedback from our Experts (see Experts section), and we will alter our project accordingly 

4. **What metrics will you use to measure the success of your project?**

   We can use the following metrics for our project:
   - Accuracy and error rates
   - Frequency of external manipulation needed
   - Improvement in time and cost efficiency

5. **How do you plan to iterate and pivot if necessary based on user feedback?**

   We plan to give users a way to provide consistent feedback at every stage of integrating and using the solution, to see which parts of the project need improvement. We aim to remain open to changes and alterations based on the feedback, since the main point of our project is to be flexible and adaptable for any environment or circumstance.

## **Leveraging AI, Open-Source, and Experts**

 ### **AI**

Since we do the Hardware part of the project, Artificial Intelligence can be applied in a very few parts of  development. But we will attempt to use AI in terms of finding information about sensors, actuators, hardware interfaces, and datasheets to optimize our searches and get new ideas from AI sources.
### **Open-Source**
Our solution may require insights from similar projects. Moreover, since our project is done separately by four different groups (see more in Defining the Vision of Your Project - Overview), we may have to test the work of the hardware part separately, without software. We succeeded in finding parts of competitor’s model as CAD model, which will help us to build our project more sensibly. Also there exist videos about Hardware components of the similar projects, giving us an opportunity to calculate the most optimal solution.
### **Experts**
Our experts will provide us with a hardware part, including tools and equipment at the same time as advice, supervising and helping in problem solving. In the long-term perspective, the experts will also help us to find potential customers and establish communication with them.

Our experts:

- Ruslan Damindarov
- Ivan Domrachev
- Aleksei Maliukov

## **Defining the Vision for Your Project**

- **Overview:** 

    The main goal of our project is to create a mobile platform and user-friendly software to control it. This project is aimed to solve the problem of material transportation in enclosed spaces, since now mainly humans are engaged in this sphere. Our project will provide a cheap roboticized solution, so that human workers can solve more important tasks.
Our project will be divided into 4 parts, constructed by different teams.
Frontend part (1st year students) - the UI used to manipulate the robot
Software part (2nd year students) - the code which will perform kinematic computations, SLAM and path planning
Simulation part (1st year students) - the emulation of mobile platform on the computer with API identical to actual mobile platform
Hardware part (2nd year students) - the actual real-life mobile platform with stable API
Our team will provide the solution of the Hardware part specifically. This involves physical connection of all the components, creation of a CAD model of the platform, and finding or developing ROS packages for each sensor, each component. Each node will publish topics - the output data from each sensor. The task is to provide an intuitive low-level software, which can be further easily incorporated into the software development of the platform. 

- **Schematic Drawings:**

![Diagram](/2024/HardwareOverlord100/Diagram.png)

## **Weekly Progress**
### **Objective**
The objective of the first week was to establish a team for the project and choose the project idea which will be both complex enough and reasonable to expect an MVP after only 6 weeks. This week the task for the Hardware team was to study documentations and datasheets of sensors, motors and other parts of the future robot. We also had to create the GitHub repository for both the project itself and reports. This week is really important for the overall project since we have to understand what we actually want to do and how our view of the project can be brought to life.
### **Results and Challenges**
This week was successful in terms of the given task. Documentations for drivers, sensors and motors were studied fully, the performance of motors was checked and confirmed, same as for ultrasonic sensors, lidars, batteries and Jetson. 

We faced many challenges during this week:

1. While checking the WiFi receiver / transmitter it was confirmed we need our own WIFI router which will be able to distribute its own internet connection to connect our robot with it through WPS feature later.

2. While testing the motor driver we failed to find an appropriate ROS package, therefore we decided to write our own implementation for this project.

3. While testing lidars, we confirmed that there exists a ROS2 package developed by the manufacturer and we intend to use it.

4. We decided to use Can Bus to interconnect the parts of the system, however usage of the Can Bus with the Jetson requires us to perform more testing and research to increase our understanding and experience.

5. Precision of existing ultrasonic sensors is not satisfactory, so we need to adjust it or find a replacement

## **Conclusion and Next Steps**
We successfully established the team and workflow for the following project. For the next week, we plan to conduct a meeting with a customer, then we can start to design the layout of the chassis, relative position of all components. Parallel to that we will research the best way to organize the power distribution scheme of accumulators in our system. Also we need to do research for ROS packages for the rest of the devices we’re going to use and write our own implementation of which we could not find.

## **Existing solutions**

[MiR100](https://shop.hartfiel.com/products/MiR100%20Mobile%20Robot) - the solution is pricey and not accessible in Russia

[GOWE Intelligent Mobile AMR Robot](https://www.amazon.com/GOWE-Intelligent-Chassis-60kg-Agv/dp/B0CZK5HSTL/ref=sr_1_1?crid=1JSZRWUDZ7KN8&dib=eyJ2IjoiMSJ9.bKrUfqjWNTqSpHoMDVLAqy8TLPNaGrDZ6E83BrxZddXtcf8WHNC7-hLf78Y04d60aRbSP6esMpDTa48H66u0PTA7eLzcA8B_WWYT0BGuoEUGRllEDeg1wOo8yAqDNK3Eq-uaJrnw4SqbvNrs6SpM6Sak-O7GI-oH-63_IFuUGvA8flZPmfEbWUBPDlYDr-gKDFZRcsVlYKNX70utqDneJ74LETzFGDINq-StmUd_8mIFqr4e8NbmfZ18zqLvPBKJ1HsjmMO9XIGHhxZ-rQBYU7KxZXkiJqkG_nMPgNJRRUs.eKBgS2OraX2Jyu8AgtIQzZp-jfIJ02pM1iQ2Uk__2wA&dib_tag=se&keywords=robot+automatic+mobile+platform&qid=1717939378&sprefix=robot+automat+mobile+platform%2Caps%2C455&sr=8-1) - still pricey, cannot be delivered to Russia

[Robot created by Yandex](https://yandex.ru/project/rec-comms/robotics/index) - since it is created by Yandex company, it is not accessible by the global market