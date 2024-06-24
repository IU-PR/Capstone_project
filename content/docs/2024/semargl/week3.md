---
title: "Week #3"
---

# **Week #3**

## Introduction
This report outlines the progress made in Week 3 of the Semargl C2 development project. The focus this week was on setting up the technical infrastructure, backend development, frontend development, data management, and initial prototype testing.

## Prototype Features
In our prototype, we have implemented the following features:

### Backend Development
- Developed the initial version of the backend server in Golang.
- Implemented gRPC communication for efficient server-client interactions.
- Set up Docker and Ansible for easy deployment and scalability.

### Agents
- Created agents in C and PowerShell, with a focus on C.
- Enabled basic command execution and communication with the server.

## User Interface
### UI/UX prototyping
- Developed initial design using the Figma.
### Frontend Development
- Developed initial UI components using the GO/Walls framework.

We considered two variants of UI, and conducted a poll among Information Security Specialists to choose the better one.

![User Interface Screenshot 1](/2024/semargl/ui1.png)
*User Interface Screenshot 1*

![User Interface Screenshot 2](/2024/semargl/ui2.png)
*User Interface Screenshot 2*

## Challenges and Solutions
### Challenge: Setting up a shared development environment and ensuring team members are proficient in using it.
- Solution: Organized learning sessions and created detailed documentation for the setup process.

### Challenge: Integrating gRPC communication in the backend.
- Solution: Utilized Golang's native gRPC library and followed best practices for implementation.

### Challenge: Finding ways to improve C2 agents.
- Solution: Making continuous research on popular and new techniques/features of C2 servers (for example, sliver).

## Next Steps
Our next steps are:
- Backend: Improve the implementation of core backend functionalities and enhance server-client communication protocols.
- Frontend: Refine the user interface, add more interactive elements, and improve user experience based on initial feedback.
- Prototype Testing: Continue with comprehensive testing and bug fixing. Collect and incorporate feedback from team members and early users.
- Post exploitation Add injection techniques like Reflective DLL hijacking.