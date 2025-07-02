---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

This week was dedicated to detailed elaboration and implementation of core functionalities necessary to reach our minimum viable product (MVP) state. The main efforts were concentrated on the backend server and simulation environment setup, with initial exploration and sketches of the agentic system architecture.

### Prioritized backlog

The prioritized backlog can be accessed through our project management tool (e.g., Kanban board). The tasks were clearly outlined, focusing on:
- Backend REST API development
- Simulation environment setup
- Integration methods for simulation and backend
- Initial architecture sketches for agentic system

## Project specific progress

### Simulation Environment (Ilvina)

This week, a basic setup for the drone simulation environment was established. The simulation includes preliminary landscape elements and a basic drone model with realistic physics. To simplify the integration and control by agentic models, wind and floating simulations were deliberately omitted for the initial MVP. A basic keyboard controller was implemented to test drone movements. 

Connection between Unity (simulation) and Python (server-side logic) was successfully established using WebSockets after evaluating other technologies like WebRTC and gRPC. Currently implemented APIs for drone control include:

1. Turn camera up/down
2. Set direction (reset direction to 0 degrees)
3. Turn by degrees (left/right)
4. Move to global coordinates (X, Y, Z)
5. Move by positional offset (X, Y, Z)

Additionally, functionality for image capturing from the drone simulation was implemented and prepared for testing.

### Backend Server (Ilvina Akhmetzianova)

The backend server was fully developed and deployed, providing a robust and flexible REST API. Inspired by the ELK stack approach, dynamic indexing of data structures was implemented, enabling schema definition and changes at runtime without altering server code. This approach ensures high flexibility to accommodate future, uncertain data requirements.

Key implemented features:
- Dynamic index creation and management through JSON schema
- Data validation against JSON schemas
- Docker Compose-based containerization for easy deployment and scalability
- Nginx reverse proxy integration

The codebase was pushed to Git, and a pull request was successfully created for review and integration into the main branch.

### Agentic System Sketch (Nikita Sergeev)

Initial sketches of the agentic system structure were prepared, providing a conceptual overview of how agentic AI systems will interact with backend services and simulation environments. The sketches are available at the shared drive and are open for feedback and further refinement.

### SLAM3R Experimental Analysis (Mahmoud Mousatat)

A comprehensive experimental evaluation of the SLAM3R system was performed, involving 60 experiments. Key insights were gained regarding optimal parameters and configuration for robust drone navigation and 3D reconstruction tasks. The full detailed report is available and includes data visualizations and recommended settings for optimal performance.

## Weekly commitments

### Individual contribution of each participant
- **Alexander Rozanov**: Developed and deployed backend server, implemented dynamic indexing inspired by ELK stack methodology, created and reviewed pull requests.
- **Ilvina Akhmetzianova**: Established simulation environment in Unity, implemented WebSocket communication between Unity and Python, developed drone control APIs and image capturing functionality.
- **Nikita Sergeev**: Prepared agentic system architecture sketches, identifying key integration points and initial system flow.
- **Mahmoud Mousatat**: Conducted detailed experimental analysis of SLAM3R system, documented results comprehensively with recommendations for system optimization.

## Plan for Next Week
- Complete integration testing of backend server and simulation environment.
- Finalize choice and implement robust API methods tailored specifically for agentic system requirements.
- Begin implementation of agentic system architecture based on initial sketches.
- Continue refinement of SLAM3R system parameters based on the conducted experiments.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (as described in the `README.md`).