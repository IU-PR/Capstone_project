---
weight: 1
bookFlatSection: true
title: "Week #1"
---

# Week #1
## Project: Vehicle tracking at maintenance service

### Team Formation and Project Proposal

#### Team members
| Team Member         | Telegram      | Email Address                     |
|---------------------|---------------|-----------------------------------|
| Darya Zhuravleva    | @zhur_a_vleva | d.zhuravleva@innopolis.university |
| Igor Abramov        | @IG_ragon     | ig.abramov@innopolis.university   |
| Mariya Sapukhina    | @sapushha     | m.sapukhina@innopolis.university  |
| Aleksandra Voronova | @Himera_05    | a.voronova@innopolis.university   |
| Viktoriya Kruk      | @cokosaa      | v.kruk@innopolis.university       |
| Lev Rekhlov         | @rekhlov      | l.rekhlov@innopolis.university    |

#### Value Proposition
**Problem:** checking the vehicle status and maintenance progress requires human supervision. It costs additional money and time. However, people tend to make mistakes or just be lazy.

**Solution:** proposed application, helps to automate the task previously assigned to human supervisor.

**Benefits:** our solution reduces risks of human errors, and is a one-time investment with low maintenance cost. Therefore, a company will eventually cover development costs and save money.

**User Impact:** reducing number of paid workers can increase company's income. Removing human factor from workflow results in automated detection of misbehavior of a workers and provides additional data that helps to analyze productivity of maintenance service.

**Use Cases:**
* program records date and time of vehicle arrival to the service
* program records data and time of vehicle leaving the service
* program records time a vehicle spends at the service
* program detects delay during work (i.e vehicle stays intact for too long)


### Lean Startup Questionnaire
1. What problem or need does your software project address?
2. Who are your target users or customers?
3. How will you validate and test your assumptions about the project?
4. What metrics will you use to measure the success of your project?
5. How do you plan to iterate and pivot if necessary based on user feedback?

Answers:
1. Our project automates the detection of vehicles arriving at, staying in, and leaving from the maintenance center;
2.  Our task holder is the company "Gazstroyprom" ("Газстройпром");
3.  We have a clear technical description for the application we need to build;
4.  Satisfaction of task holder:
5.  Throughout the process of building the application we will be in contact with the IT department of "Gazstroyprom" to validate all necessary steps and check with our and their vision regarding implementation. Our team will work on AGILE with scrum sprints.

### Leveraging AI, Open-Source, and Experts

#### Artificial intelligence
Artificial intelligence, especially LLMs like Chat-GPT can provide a quick start and help to sketch a general architecture of our application. Overall, our application relies on detection neural models and OCR technologies.

#### Open-Source
As we have a detection task, there is a high probability, that we will use great open-source pre-trained models like YOLO. Moreover, we are definitely will use open-source libraries and technologies such that PyTorch and Flutter Plugins.

#### Experts in relevant domains
Besides tech guys in "Gazstroyprom", our team members have useful connections with Innopolis University staff and SEZ residents. These people will consult us about the technical aspects of deploying neural models to production code as well as share best industrial practices.

### Defining the Vision for Your Project

#### Overview
Brief summary of the project:
The goal of the project is to develop and implement a system capable of determining the presence of vehicles in the area of technical inspection and repair (MRO) using state registration plates (GRZ). The system will be based on modern technologies of computer vision, license plate recognition and data analysis.

Problem:
One of the main problems faced by enterprises involved in MRO is the need to control and track the presence of vehicles in the work area. Lack of such controls can lead to unplanned delays, waiting times and reduced efficiency in the MRO process.

Solution:
The developed system will use CCTV cameras and computer vision algorithms to automatically recognize the GRZ of vehicles entering, staying and leaving the MRO area. Data on recognized license plates will be transferred to a central database for further processing.

Benefits and impact on users or stakeholders:

* Automation of the vehicle control process in the MRO area will reduce the likelihood of errors associated with manual data entry and simplify the procedure for tracking the presence of vehicles.
* The ability to quickly respond to changes in the composition of vehicles in the MRO area will allow the enterprise to effectively plan and organize work processes.
* Improved maintenance times by optimizing work schedules and eliminating unplanned delays.
* Improving the overall efficiency of the enterprise, increasing its competitiveness

#### Schematic Drawings

![](/WeWantMoney/Use-case_Cap.drawio.png)

#### Tech Stack
The preliminary tech stack for our project looks like this:
* Flutter developer
* Computer vision engineer (selecting and verifying model)
* Developer (internal logic of the application)
* Machine learning engineer (deployment and maintenance)
* Designer for desktop applications

#### Anticipating Future Problems
Technical challenges may arise in ensuring accurate license plate recognition and optimal performance of computer vision algorithms.
To address these challenges, we will conduct comprehensive testing, continuously train and update our algorithms, and collaborate closely with experts and technical support for effective troubleshooting and maintenance.

#### Elaborate Explanations
Explanations will be done through explaining application workflow:
* Application receives video in a form of a stream or file from stationary cameras at the maintenance service
* Video is handled by YOLO or other detection neural model
* Frame analysis in a time-series allows to identify action and actors (arrival, leaving, staying, work delay)
* Detected actions are filtered and recorded to database
* Recent events will be displayed
* Future database implications will be discussed with tech guys. Currently, idea is to notify responsible people about major issues (i.e delay). Also, it is possible to make automated reports at the end of a working day and at the end of month, or just send collected data to any BI system currently adopted by a company.

{{< hint danger >}}
**Feedback**  


**Value Proposition**

This is very short explanation of the value proposition. And it doesn’t reflect that you spent much time answering them.

What are you trying to solve exactly. In what system? Car maintenance  services? But how will you eliminate ham factor? The problem statement you have is weak. You must re do it

Use cases are wrong, the uses cases should reflect how your app will be used and by whom?

**Lean startup question**

This part also, very short, And it doesn’t reflect that you spent much time answering them.
And mostly wrong answers or incomplete. 

>Satisfaction of task holder 

How will you measure it. Beside is this the only metric you will use? Try google Metrics to mouser success in Products 

**AI** 

What detection neural models will you use? 
Which OCR technologies will you use?

**Vision Of The Project**
Good

**Overall**

The report is ok. it’s good in the technical side. But you need to spent more time thinking about the business and operational side. 
You should redo : Value proposition and lean startup question 

3/5


_Feedback by Moofiy_
{{< /hint >}}

