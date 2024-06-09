---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member           | Telegram ID  | Email Address                     |
| --------------------- | ------------ | --------------------------------- |
| Artur Lukianov (Lead) | @magnummalum | a.lukianov@innopolis.university   |
| Alexander Efremov     | @paqpaqpaq   | a.efremov@innopolis.university    |
| Vadim Yarullin        | @inf1rmittyy | v.yarullin@innopolis.university   |
| Andrew Boronin        | @anboronin   | a.boronin@innopolis.university    |
| Alexander Tomashov    | @sad_pixels  | a.tomashov@innopolis.university   |
| Nika Ckekhonina       | @xochusleep  | n.ckekhonina@innopolis.university |
| Viktoria Patrina      | @vika_7321   | v.patrina@innopolis.university    |

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

Our framework aims to be closer to buisness and provide transparent and smooth experience not only for red teamers, but also for engagement customers. Another difference is the agent model we use - we try to cover as much MITRE TTPs as possible, even if they overlap in some cases.

- User Impact:

With this C2 framework, profiessionals can make the Red Team engagemtns more transparent and robust. The customers of Adversary emulations will have control over engagement restrictions and will be informed about actions on objectives. The automation workflow and single database will raise the quality of Red Team engagements and speed up the process, saving time on routine operations.

- User Testimonials or Use Cases:

Use cases:

- External adversary emulation
- Internal adversary emulation
- Penetration testing
- Cybersecurity training

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address?

Our software project addresses the need for a robust and versatile command-and-control (C2) framework tailored for red team operations. It tackles the challenges of managing complex attack simulations and security assessments efficiently. By providing a multi-language, flexible, and scalable solution, it helps red teams conduct realistic adversary emulations, identify security gaps, and enhance the overall cybersecurity posture of organizations.

2. Who are your target users or customers?

Our target users are cybersecurity professionals engaged in red team operations, including penetration testers, security consultants, and threat hunters. Additionally, it is useful for organizations aiming to evaluate their security defenses, identify vulnerabilities, and improve their resilience against cyber threats. Security researchers and developers looking for a versatile C2 framework for testing and educational purposes are also among our target customers.

3. How will you validate and test your assumptions about the project?

We will validate and test our assumptions through a combination of beta testing, user feedback, and controlled testing environments. By conducting beta tests with cybersecurity professionals, we can gather insights into the framework's performance and usability. We will also collect feedback through surveys and direct interactions with users. Additionally, deploying the framework in controlled lab environments will help us assess its effectiveness in simulated scenarios.

4. What metrics will you use to measure the success of your project?

We will measure the success of our project based on the following metrics:

- User Adoption: Tracking the number of organizations and professionals using our framework.
- User Satisfaction: Collecting feedback and conducting surveys to assess user satisfaction and identify areas for improvement.
- Engagement Effectiveness: Evaluating the framework's performance in real-world red team engagements through success rates and the identification of security gaps.
- Scalability and Flexibility: Assessing the ease of deployment, integration with various environments, and the framework's ability to handle complex scenarios.

5. How do you plan to iterate and pivot if necessary based on user feedback?

We plan to iterate and pivot based on user feedback by continuously collecting and analyzing feedback from beta testers and users. Regular updates and enhancements will be made to address identified issues and incorporate new features. We will also maintain an open line of communication with our user base through forums, support channels, and user groups to ensure we are responsive to their needs. Data analysis from engagement scenarios will help us refine our framework, ensuring it remains relevant and effective in the evolving cybersecurity landscape.

For testing we will use the following resources:

- TryHackMe Networks
- Standoff365 Cyberrange
- Priviahub Cyberrange

## **Leveraging AI, Open-Source, and Experts**

Our team will levergage open-source projects like (sliver)[https://github.com/BishopFox/sliver], (merlin)[https://github.com/Ne0nd0g/merlin], (Empire)[https://github.com/BC-SECURITY/Empire] to measure the effectiveness against well-known frameworks.

We use AI for code checking and documentation, however all code is written by hand and based on best practices or white papers. Security frameworks must be secure and we could not yet trust AI to write secure code.

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
