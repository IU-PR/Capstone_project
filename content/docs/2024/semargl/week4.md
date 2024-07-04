---
title: "Week # 4"
---

# Project Report for Week 4

## External Feedback

Emphasizing the importance of feedback cannot be overstated. This week, we focused on gathering external feedback for our project, Semargl C2. Given that it is early to target potential users directly, we sought feedback from our community, including fellow students and friends who could provide honest insights.

### Key Feedback Points:
1. Usability: Several users found the initial setup and configuration process straightforward.
2. Functionality: Users appreciated the multi-language agent support, noting that it allows for flexibility across different environments, but the agents are incomplete and are in different progress stage.
3. Documentation: While the installation instructions were clear, users suggested more detailed usage examples and troubleshooting tips. Also, there was questions about the details of conversation protocols between the agent and C2.
4. Interface: The UI/UX prototype was well-received, but some users suggested adding more intuitive navigation and real-time monitoring features.

This feedback has provided us with valuable insights to enhance the user experience and refine the functionalities of Semargl C2.

## Testing
Initial tests have helped identify some areas for improvement, including optimizing network communication and refining the error-handling mechanisms.

1. Basic Functionality Tests: Ensured that key features such as agent communication, command execution are working as expected.
2. Environment Compatibility: Conducted tests across different environments to verify the seamless integration and execution of Rust, C, and PowerShell agents.
3. Scalability Tests: Utilized Docker to deploy multiple instances of Semargl C2, testing the system's ability to handle a larger number of simultaneous connections.

### Challenges and solutions

### GUI Client

We implemeneted prototype of GUI client using Wails framework with Vue. Currently it is not fully functional, but allows to interact with server in basic way.

### Agent

Rust agent gained support for `download` and `upload` commands. C agent DLL module loading added, but is not currently fully tested.


## Current status and next steps

**Current Status:**

- Client UI/UX prototype with working communication
- Agents and server communications with basic commands

**Upcoming Tasks:**

- Implement database on server for storing hosts and credentials
- Improve module loading functionality
