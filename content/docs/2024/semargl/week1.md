---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Artur Lukianov (Lead)     | @magnummalum | a.lukianov@innopolis.university |
| Team Member 2            | [Telegram ID] | [Email address] |
| Team Member 3            | [Telegram ID] | [Email address] |
| Team Member 4            | [Telegram ID] | [Email address] |
| Team Member 5            | [Telegram ID] | [Email address] |
| (Optional) Team Member 6 | [Telegram ID] | [Email address] |
| (Optional) Team Member 7 | [Telegram ID] | [Email address] |

### **Value Proposition**

- Identify the Problem:

While Information Security becomes more widespread, conducting full adversary emulation poses a significant challenge to professionals.

The industry has several tools what aim to provide penetration testers with needed environment, however the environment is closed and not trusted.

Also, the existing frameworks lacks techniques used by cyber-criminals, so cannot efficiently test Security Operation Centers.

- Solution Description:

We aim to provide a versatile and powerful command-and-control (C2) framework, which will support not only modules for actual red team operation, but also for planning and reporting. The framework should be transparent and allow customer of the red team operation to view all actions performed on infrastructure.

The framework should allow to choose TTPs to restrict or permit actions on customer network according to Red Team operation plan.

- Benefits to Users:

Open and transparent red teaming framework will make the process of Red Teaming more suitable for buisness goals, allowing to focus not on vulnerabilities or metrics, but on actual security and unacceptable events.

For Red Teamers and Penetration Testers this framework will provide a collaboration, collection and automation environment which can quickly adopt to chosen environments. The open code of framework makes the operation more secure, ensuring that no client data will be leaked outside.

- Differentiation:
...

- User Impact:
...

- User Testimonials or Use Cases:
Use cases:
 - External adversary emulation
 - Internal adversary emulation
 - Penetration testing
 - Cybersecurity training

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address? 
   
   ...

2. Who are your target users or customers?

   ...

3. How will you validate and test your assumptions about the project?

   ...

4. What metrics will you use to measure the success of your project?

   ...

5. How do you plan to iterate and pivot if necessary based on user feedback?

   ...

## **Leveraging AI, Open-Source, and Experts**

Our team...

## **Defining the Vision for Your Project**

- Overview: We aim to create a versatile and powerful command-and-control (C2) framework tailored for red team operations. The framework is targeting not only security professionals, but also tries to be closer to buisness customers.

- Schematic Drawings: 
{{<mermaid>}}
graph TD;
    Client1[Client] -->|gRPC| Server[Semargl C2 Server]
    Client2[Client] -->|gRPC| Server
    Redirector1 -->|TCP| Server
    Redirector2 -->|TCP| Server
    Agent1[Agent] -->|TCP| Redirector1[Redirector]
    Agent2[Agent] -->|HTTP| Redirector1[Redirector]
    Agent3[Agent] -->|DNS| Redirector2[Redirector]
    Agent4[Agent] -->|ICMP| Server
{{</mermaid>}}

- Tech Stack: 
   - Backend (server):
      - Golang
      - GRPC
   - Client:
      - Golang
      - GRPC
   - Agent:
      - C
      - WinAPI

