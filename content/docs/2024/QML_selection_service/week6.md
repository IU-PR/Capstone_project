---
title: "Week6"
---

# **QML selection service presentation**

{{< embed-pdf url="/2024/QML_selection_service/Quantum-Annealing-For-Feature-Selection.pdf" >}}

## Weekly Progress Report

### Achievements
During this week, our team made significant progress in developing a FastAPI application designed to serve as a container for our quantum machine learning (QML) service. The key milestones we accomplished include:

1. **FastAPI Application Development:**
   - **Framework Selection:** We selected FastAPI due to its high performance, ease of use, and modern features that align well with our project's requirements.
   - **Service Integration:** Successfully integrated the QML service into the FastAPI application, ensuring that the service can be accessed and utilized efficiently.

2. **Library Importation:**
   - **Essential Libraries:** Imported all necessary libraries required for the QML service, ensuring that the application has the tools needed to perform quantum machine learning tasks.
   - **Dependency Management:** Managed dependencies meticulously to prevent conflicts and ensure compatibility across different environments.

3. **Containerization with Docker:**
   - **Docker Implementation:** Dockerized the FastAPI application, creating a portable and self-sufficient container that can run consistently across various computing environments.
   - **Portability and Scalability:** Ensured that the application is easily deployable and scalable, facilitating smooth transitions between development, testing, and production stages.

### Challenges & Solutions
Our team faced several challenges during this development phase, particularly with the installation of machine learning libraries and quantum annealing tools, as well as configuring the D-Wave systems. Here is a detailed breakdown of the challenges and our solutions:

1. **Challenge:** Installing Machine Learning Libraries and Quantum Annealing Tools
   - **Complexity:** The installation process for various machine learning libraries and quantum annealing tools required careful handling due to compatibility issues and specific configuration needs.
   - **Solution:** We addressed this by:
     - **Library Tracking:** Keeping a detailed log of every library used in the code and ensuring they were listed in the `requirements.txt` file. This practice ensured that all dependencies are documented and can be installed reliably.
     - **Dependency Documentation:** Regularly updating and maintaining the `requirements.txt` file to reflect any changes or additions to the libraries used.

2. **Challenge:** Configuring D-Wave Systems
   - **Complexity:** Configuring the D-Wave quantum annealer required a deep understanding of its documentation and settings.
   - **Solution:** 
     - **Documentation Review:** We thoroughly reviewed the D-Wave configuration documentation to understand the requirements and best practices for setup.
     - **Configuration Testing:** Conducted multiple tests to validate the configuration, ensuring that the quantum annealing tools are properly integrated and functional.

### Conclusions & Next Steps
We are pleased to report that we are nearing the completion of our project. The following outlines our conclusions and the next steps to be taken:

1. **Conclusions:**
   - **Progress:** Significant progress has been made in both the development and containerization of the FastAPI application. The integration of the QML service and the successful handling of dependencies and configuration challenges have set a solid foundation for the project's completion.
   - **Team Effort:** The collaboration and dedication of the team have been instrumental in overcoming the challenges encountered, showcasing our ability to work cohesively towards our goals.

2. **Next Steps:**
   - **Finalization:** Focus on finalizing the application, ensuring all components are fully operational and optimized.
   - **Thorough Testing:** Conduct comprehensive testing to identify and resolve any remaining issues. This includes functional testing, performance testing, and stress testing to ensure the application can handle real-world usage scenarios.
   - **Documentation:** Prepare detailed documentation covering all aspects of the application, including installation, configuration, usage instructions, and troubleshooting guides. This will facilitate future maintenance and updates.
   - **Deployment Preparation:** Plan and execute the deployment of the application, ensuring a smooth transition from the development environment to the production environment.
