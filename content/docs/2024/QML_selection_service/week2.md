# Weekly Progress Report: Week 2 - Choosing the Tech Stack, Designing the Architecture

## Tech Stack Selection

- Explored quantum computing platforms, including D-Wave's Leap Cloud and NVIDIA's cuQuantum SDK.
- Selected D-Wave's Leap Cloud for quantum annealing due to its application in combinatorial optimization problems, crucial for business analytics.

## Architecture Design

This architecture integrates a Flutter web frontend with a Laravel backend for handling core business logic, authentication, and data management, along with FastAPI for machine learning and quantum computing functionalities.

### Component Breakdown

#### Flutter Web Frontend
- **Purpose:** Provides a responsive and interactive user interface for web users.
- **Technologies:** Dart, Flutter Web.
- **Key Responsibilities:**
  - Render UI components.
  - Handle user interactions.
  - Make API calls to the backend (Laravel) for data and authentication.
  - Display results from machine learning and quantum computations.

#### Laravel Backend
- **Purpose:** Manages business logic, data storage, and authentication.
- **Technologies:** PHP, Laravel Framework, MySQL/PostgreSQL (for database).
- **Key Responsibilities:**
  - Serve as an API provider for frontend requests.
  - Handle user authentication and authorization.
  - Manage and interact with the database.
  - Coordinate data requests and responses between the frontend and FastAPI services.

#### FastAPI Service
- **Purpose:** Provides endpoints for machine learning and quantum computing functionalities.
- **Technologies:** Python, FastAPI, various ML libraries (like TensorFlow, PyTorch), quantum computing libraries (like Qiskit).
- **Key Responsibilities:**
  - Expose RESTful APIs for machine learning models and quantum computations.
  - Perform intensive computations and return results.
  - Interact with the Laravel backend to fetch necessary data.

### Communication Flow

#### User Interaction
1. The user interacts with the Flutter web app.
2. The Flutter app sends API requests to the Laravel backend.

#### Laravel Backend
3. Laravel processes requests from the Flutter app.
4. For regular data and business logic processing, Laravel interacts with the database and sends responses back to Flutter.
5. For ML and quantum computation requests, Laravel forwards the requests to the FastAPI service.

#### FastAPI Service
6. FastAPI processes ML and quantum computation requests.
7. It performs the required computations using appropriate libraries.
8. FastAPI sends the computation results back to the Laravel backend.

#### Laravel Backend
9. Laravel receives results from FastAPI.
10. Laravel processes the results if needed and sends the final response back to the Flutter frontend.

#### User Interface Update
11. The Flutter app receives the response and updates the user interface accordingly.

### Detailed Component Interaction

#### User Authentication Flow
- **Frontend:** User submits login credentials.
- **Backend (Laravel):** Validates credentials, generates a token, and responds to the frontend.
- **Frontend:** Stores the token and uses it for authenticated API requests.

#### Data Request Flow
- **Frontend:** User requests data (e.g., list of items).
- **Backend (Laravel):** Fetches data from the database and responds to the frontend.

#### Machine Learning Request Flow
- **Frontend:** User initiates an ML request (e.g., image classification).
- **Backend (Laravel):** Receives the request and forwards it to FastAPI.
- **FastAPI:** Processes the request, performs ML computation, and sends results back to Laravel.
- **Backend (Laravel):** Processes results if necessary and responds to the frontend.
- **Frontend:** Displays the results to the user.

#### Quantum Computing Request Flow
- **Frontend:** User initiates a quantum computation request.
- **Backend (Laravel):** Forwards the request to FastAPI.
- **FastAPI:** Executes quantum computation, processes the results, and sends them back to Laravel.
- **Backend (Laravel):** Processes results if necessary and responds to the frontend.
- **Frontend:** Displays the results to the user.

### High-Level Diagram of the Architecture

    +-------------------+       +-------------------+       +------------------+
    |   Flutter Web     | <---> |     Laravel       | <---> |     FastAPI      |
    |     Frontend      |       |     Backend       |       |  (ML & Quantum)  |
    +-------------------+       +-------------------+       +------------------+
            ^                           ^                          ^
            |                           |                          |
            v                           v                          v
      +------------+             +-------------+             +-------------+
      |    User    |             |   Database  |             |   Compute   |
      |  Requests  |             | (MySQL/PG)  |             |  Libraries  |
      +------------+             +-------------+             +-------------+


## Considerations

### Security
- Use HTTPS for all communications between frontend, backend, and FastAPI.
- Implement robust authentication and authorization mechanisms in Laravel.
- Secure sensitive data in the database and during transit.

### Scalability
- Deploy each component (Flutter, Laravel, FastAPI) in a scalable manner using containers (Docker) and orchestration tools (Kubernetes).
- Use load balancers to distribute traffic efficiently.

### Performance
- Optimize database queries and use caching mechanisms in Laravel.
- Ensure FastAPI endpoints are optimized for performance-intensive tasks.
- Utilize asynchronous processing in FastAPI for handling long-running computations.

## Quantum Annealing and Leap Cloud Integration

### Quantum Annealing
- Leveraged D-Wave's quantum annealing technology for solving combinatorial optimization problems. Quantum annealers use quantum fluctuations to find the lowest energy state (optimal solution) of a given problem.

### Leap Cloud
- Utilized D-Wave's Leap Cloud platform, providing access to quantum annealers via cloud-based services. Leap Cloud offers tools like Ocean SDK for developing and deploying quantum applications, simplifying integration with existing workflows.

### Ocean SDK
- Integrated Ocean SDK for quantum programming, facilitating seamless development and execution of quantum annealing applications. Ocean provides a suite of tools and libraries for algorithm development, problem modeling, and result analysis on D-Wave quantum systems.

### Hybrid QPU and Direct QPU

#### Hybrid QPU
- Explored hybrid quantum processing units (QPU) combining classical and quantum processing capabilities. Hybrid QPUs offer flexibility in algorithm execution, leveraging classical computing for preprocessing and post-processing tasks while utilizing quantum resources for computational advantage.

#### Direct QPU
- Evaluated direct QPUs for pure quantum processing tasks, focusing on leveraging quantum entanglement and superposition for solving complex optimization problems. Direct QPUs offer potential speedups over classical counterparts in specific quantum algorithm applications.

## Week 2 Questionnaire

- **Tech Stack Resources:** Utilized D-Wave's Leap Cloud documentation for configuring quantum annealing parameters and understanding hardware constraints.
- **Mentorship Support:** Conducted independent research with guidance from online resources and community forums.
- **Exploring Alternative Resources:** Evaluated NVIDIA's cuQuantum SDK for potential integration with quantum-inspired machine learning models using TensorFlow Quantum.
- **Identifying Knowledge Gaps:** Identified the need for deeper understanding in quantum algorithm optimization specific to business analytics applications.
- **Engaging with the Tech Community:** Participated in webinars and discussions on LinkedIn Quantum to explore advancements in quantum computing applications.
- **Learning Objectives:** Planned to validate quantum annealing's efficiency gains in feature selection through comparative analysis of machine learning model performance.
- **Sharing Knowledge with Peers:** Intended to publish findings in IEEE Quantum, aiming to present at Qubits Quantum Computing Conference to disseminate project insights.

## Challenges & Solutions

- **Challenges:** Initial setup complexities with quantum annealer integration and API synchronization, particularly in managing quantum circuit execution times and qubit interactions.
- **Solutions:** Resolved integration issues by leveraging D-Wave's Leap Cloud SDK and adapting API endpoints for optimized data exchange and computational resource management.

## Conclusions & Next Steps

- **Conclusions:** Quantum annealers demonstrate potential efficiency improvements for feature selection, critical for optimizing machine learning model performance.
- **Next Steps:** Implement classical and quantum feature selection algorithms, conduct rigorous performance benchmarks, and refine integration for enhanced prediction accuracy and computational efficiency.

## Progress Review Session with TA

- Actively participated in progress review session, incorporating feedback on quantum computing methodologies and scalability considerations.
- Enhanced system architecture to support dynamic scaling of quantum annealing tasks and optimized resource allocation for improved performance.

## Communication & Presentation

- Structured report to articulate quantum computing concepts and project objectives effectively.
- Employed a clear and concise technical writing style suitable for peer-reviewed publications, complemented by illustrative data visualizations and comprehensive references.

## Team Members and Responsibilities

| Team Member             | Track        | Responsibilities                                                    |
|-------------------------|--------------|---------------------------------------------------------------------|
| Vladislav Pershko (Lead)| Design       | Overseeing project design, integrating components, managing team    |
| Sergey Dzyuba           | Fullstack    | Developing and maintaining backend and frontend integration         |
| Vlad Vechkanov          | Frontend     | Developing and maintaining the Flutter web frontend                 |
| Mikhail Voronin         | ML           | Implementing machine learning models and algorithms                 |
| Suleiman Karim Eddin    | Backend      | Developing and maintaining the Laravel backend                      |
| Hadi Salloum            | Quantum ML   | Implementing quantum computing algorithms and integration           |

## Weekly Progress Report

Our team worked on exploring quantum computing platforms and selecting the appropriate tech stack, resulting in choosing D-Wave's Leap Cloud for its capabilities in combinatorial optimization. We designed a system architecture integrating Flutter, Laravel, and FastAPI, detailing the interaction between these components.

## Challenges & Solutions

- **Challenges:** We faced difficulties in integrating quantum annealers and ensuring efficient API synchronization.
- **Solutions:** These issues were resolved using D-Wave's Leap Cloud SDK and optimizing API endpoints for better data exchange and resource management.

## Conclusions & Next Steps

- **Conclusions:** The integration of quantum annealers shows promise in improving feature selection efficiency, crucial for machine learning model optimization.
- **Next Steps:** We will implement both classical and quantum feature selection algorithms, benchmark their performance, and refine the integration to enhance accuracy and computational efficiency.