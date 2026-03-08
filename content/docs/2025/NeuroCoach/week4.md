---
title: "Week #4"
---

# **Week #4**

## Testing and QA

Overall Testing Approach
The NeuroCoach project implements a multi-layered testing strategy with comprehensive coverage across different application tiers and platforms.

Types of Tests Implemented
1. Unit Tests
Location: Individual *_test.go files alongside source code

Coverage Areas:
Services Layer (ai_test.go): AI service functionality, rating calculations, error handling
Handlers Layer (handlers_test.go): HTTP request/response handling, JSON serialization
Repository Layer (mongodb_test.go): Database operations, rating algorithms, consecutive days calculation
Models Layer (models_test.go): Data validation, score calculations, level progression logic
Utilities (crypto_test.go, jwt_test.go): Password hashing, JWT token generation/validation

2. Integration Tests
File: test_integration.go
Purpose: End-to-end API endpoint testing with mock dependencies
Features: Full HTTP request/response cycle testing, router integration

3. Benchmark Tests
Location: Within integration test file
Focus: Performance testing of critical algorithms (rating calculations, consecutive days logic)

4. Widget Tests (Flutter)
File: widget_test.dart
Purpose: UI component testing for Android app
Type: Basic smoke tests for widget interactions

Key Testing Features
Mock Implementation Strategy
Dependency Injection: Uses mock repositories and services
Interface-based Mocking: Clean separation between real and test implementations
Isolated Testing: Each test runs independently without external dependencies

Test Data Management
Structured Test Cases: Table-driven tests with multiple scenarios
Realistic Mock Data: Representative user ratings, workout data, and progress metrics
Edge Case Coverage: Zero values, boundary conditions, error scenarios

Automated Testing Pipeline
GitHub Actions: Automated CI/CD with test execution on push/PR
Multi-Database Support: Both PostgreSQL and MongoDB test environments
Coverage Reporting: HTML coverage reports generated automatically
Linting Integration: Code quality checks alongside tests

Testing Commands (Makefile)
make test              # All tests
make test-unit         # Unit tests only
make test-integration  # Integration tests
make test-coverage     # Tests with coverage report
make benchmark         # Performance benchmarks

Coverage Areas
Business Logic Testing
✅ User rating calculations (total workouts + consecutive days)
✅ Fitness level progression (Beginner → Intermediate → Advanced → Expert)
✅ Workout completion tracking
✅ Score calculation algorithms

Security Testing
✅ Password hashing/verification (bcrypt)
✅ JWT token generation/validation
✅ Token expiration handling
✅ Authentication flow testing

Data Layer Testing
✅ MongoDB operations (chat, workouts, progress)
✅ PostgreSQL operations (users, profiles)
✅ Data validation and constraints
✅ Error handling for database failures

API Testing
✅ HTTP handlers (register, login, rating endpoints)
✅ Request/response serialization
✅ Error response formatting
✅ Content-type validation

Testing Best Practices Implemented
Test Isolation: Each test is independent and doesn't affect others
Mock Dependencies: External services are mocked for reliable testing
Comprehensive Coverage: Critical business logic has high test coverage
Performance Testing: Benchmarks for algorithm-heavy operations
Automated Execution: CI/CD pipeline ensures tests run on every change
Documentation: Detailed testing guide with setup instructions

This testing strategy ensures high code quality, reliable functionality, and maintainable codebase across the entire NeuroCoach fitness application ecosystem.


### Evidence of test execution

https://docs.google.com/document/d/1ubudEJ3XETuGQ_XgsiREbY_UXPo9h-D3RlaWEiOa3o0/edit?usp=sharing

## CI/CD

CI/CD setup uses github actions. All workflows are being ran on ubuntu-latest github owned machine. Testing uses actions/setup-go@v4 and Makefile with all test running setup there.  Android app tests are made with subosito/flutter-action@v2, which setups flutter environment, and runs test with flutter test. Deployment uses SSH with webfactory/ssh-agent@v0.8.0, to connect to external server and run the project there via docker-compose. Challenges were faced with finding the right tools for executing tests and deployement on github machines, along with several typos/not up to date code issues.

### Links to CI/CD configuration files

https://github.com/IU-Capstone-Project-2025/NeuroCoach/tree/main/.github/workflows

## Deployment

### Staging

Deployment process runs with deploy.yml. It establishes an SSH connection with the external server, pulls from the main branch removes previously ran containers and rebuilds the project with docker-compose up --build -d.

### Production

The same goes for production. For purposes of hosting the app, the personal domain of one our team members was used (blazz1t.online)[http://blazz1t.online]. The DNS is made through Cloudflare, pointing exactly to target IP address The VDS is being ran as a Debian 12 virtual machine, which is ran under a publicly accessible personal server. Port forwarding was setup, forwarding incoming requests on port 80 from router, to port 8080 on the server. Nginx was setup on the server to figure out where to route the requests, depending on the subdomain. Server on its part forwards request to port 80 of the VM. 

SSH for the VM is setup the same way, to route requests from 22 to 2222 to 22 on the VM.

## Vibe Check

https://docs.google.com/document/d/1Sv4AI0s1hPF7FW-7umFmY2T143zwF_y18Bz-kVZv4r8/edit?usp=sharing

The session included all core team members: Maxim (QA & Backend), Danil (Designer), Klim (DevOps & Mobile Developer), Said (Frontend Developer), and Mark (Product Manager). The purpose of the Vibe Check was to reflect on team dynamics, identify potential bottlenecks, surface concerns early, and reinforce transparency and mutual support across the team.

Overall, the team is in excellent condition across most categories. Morale is high, with strong motivation and alignment on the product vision. Technical progress is outstanding, with all systems—backend, frontend, mobile, QA, and design—performing smoothly and efficiently. Communication is effective, especially through asynchronous updates, and coordination between design, development, and QA is well established. Design and UX are consistently strong, with timely delivery and precise implementation of assets. The backend architecture remains stable and adaptable to ongoing product changes. Product clarity is clear, and team culture is healthy, with no interpersonal issues reported.

However, two areas of concern were identified related to workload balance. Maria, who holds multiple roles including code review, technical evaluation, product ideation, and backend development, is experiencing overload. This creates a risk of burnout if not addressed through delegation or task redistribution. Similarly, Klim is handling both DevOps and mobile development simultaneously, which is currently manageable but unsustainable under increased pressure.

Each team member shared their reflections. Maria acknowledged the stability of the backend and effective cross-functional communication but expressed the need for task delegation to avoid burnout. Klim noted the success of the CI/CD pipeline and reliable deployment processes but pointed out the strain from handling dual responsibilities. Other team members—Maxim, Danil, Said, and Mark—reported smooth operations, manageable workloads, and good collaboration across disciplines.

In response to the feedback, several action items were agreed upon. Maria and Mark will reassess and rebalance technical leadership responsibilities before the next sprint. Klim and Mark will reevaluate the distribution of mobile and infrastructure tasks and reprioritize accordingly within the week. The entire team committed to proactively raising signs of overload or delays as they arise. Additionally, Mark will explore implementing a feature intake process or delegating some of Maria’s ideation responsibilities to other product managers or designers by mid-next sprint.

The team's overall mood was assessed on a scale from 1 (exhausted) to 5 (energized), with an average score of 4.3. Most members reported feeling energized and satisfied with the current pace and quality of work. While Maria and Klim feel some pressure due to their heavy workloads, both remain positive and engaged.

Moving forward, the team plans to support overloaded roles through rebalancing efforts and scope adjustments where necessary. Maintaining the current collaborative rhythm and open communication remains a priority. Small wins will be recognized regularly to sustain high morale and motivation.

# Weekly commitments

## Individual contribution of each participant

Mariia Nikolashina
Mariia organized synchronization meetings for backend, frontend, and mobile developers to ensure alignment. She coordinated with DevOps for accurate backend deployment. She proposed and detailed feature requests, conducted a vibe check, summarized team feedback, and suggested actionable improvements to enhance team dynamics. 

Vibe check: 
https://docs.google.com/document/d/1Sv4AI0s1hPF7FW-7umFmY2T143zwF_y18Bz-kVZv4r8/edit?usp=sharing

Feature requests included:  
- Scheduling specific training dates instead of generic planning.  
- Tracking workout statuses (done or expired) to manage user ratings.  
- Adapting workout plans based on weekly free time, extending across the user-defined goal timeframe.  

Mariia researched product challenges and target conditions, identifying potential growth obstacles and proposing preventive strategies to align the product with market needs and user expectations.

https://docs.google.com/document/d/1RfCdJfGrddlYxjBPtzC23AqPnK6HQcNbdZ4AlYob6rU/edit?usp=sharing

Mariia implemented the following features:  
- Generated comprehensive training plans for the entire user-defined timeframe, beyond weekly samples.  
- Dynamically adapted plans based on users’ weekly availability.  
- Scheduled specific dates for each workout.  
- Periodically updated workout statuses to reflect completion or expiration.  
- Integrated motivational message generation for user notifications.

PR - https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/24


Mark Petrov
Mark provided strategic project leadership, organizing and coordinating team work. He conducted a series of working meetings to discuss current tasks and development prospects. Mark devoted significant attention to market analysis and developing product promotion strategies. He revised the project's financial model considering various development scenarios and adjusted monetization approaches. The user interviews and usability tests he conducted helped identify important areas for improvement.
- https://docs.google.com/document/d/1Am0bbRsuRcGNvMzT-dQJ5CeYz4ur_zHst950EyRWsfg/edit?usp=sharing
- https://docs.google.com/document/d/1lErJMtMSMlS1pkcJhLP9JPIpVMMytAa8TuCMh0F4wUQ/edit?usp=sharing

Maxim Oleynik
Maxim focused on two fundamental aspects of project development. As part of functionality development, he created a sophisticated system for evaluating user activity that analyzes multiple training process parameters. This system doesn't just track exercise completion, but forms a comprehensive understanding of each user's progress. In parallel, Maxim built a multi-level quality control system including various types of automated testing. He thoroughly worked through processes for testing critical system components, paying special attention to security and system stability. Additionally, he prepared comprehensive documentation describing quality standards and best practices for the project.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/26/
- https://docs.google.com/document/d/1lErJMtMSMlS1pkcJhLP9JPIpVMMytAa8TuCMh0F4wUQ/edit?usp=sharing

Danil Fishchenko
Danil dedicated the week to deep refinement of the product's visual language. He explored various approaches to visualizing user progress, testing and improving concepts. The result was a cohesive visualization system where the training process takes tangible form. He paid special attention to creating an exercise library, ensuring illustration consistency and informativeness. Numerous interface improvements made by Danil significantly enhanced usability across all device types.
- https://www.figma.com/design/ggsx8HjvuNhfUltSbONPfu/Untitled?node-id=0-1&t=CN432rmJ0ESmdEj7-1

Klimentii Chistyakov
Klimentii executed the crucial transition of the project from development to production environment. His work included selecting optimal infrastructure, configuring secure connections, and ensuring uninterrupted service operation. To automate processes, he developed a system that significantly simplifies product updates and operational monitoring. For the mobile version, Klimentii solved several complex technical problems related to data synchronization and app performance under various conditions.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/25
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/23


Saidaziz Kadirov
Saidaziz worked on creating interactive data visualization elements and optimizing interface performance. He developed a visualization system that allows users to easily track their progress. His work particularly focused on performance and adaptability, achieving smooth interface operation in various conditions. Saidaziz also did extensive work to ensure consistent appearance and behavior across different platforms.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/commit/1d73b21675db18d853a7afb4ca81856f1bc8d3bb

## Plan for Next Week

- Enhance AI personalization by refining workout difficulty adjustments and improving conversational responses 
- Optimize user interface elements, particularly the AI chat visibility and workout variety options
- Implement offline functionality and performance improvements for mobile users
- Finalize visual design elements for the progress tracking system
- Prepare infrastructure for upcoming beta testing phase

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).