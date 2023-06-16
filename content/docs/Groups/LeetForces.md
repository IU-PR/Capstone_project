# **LeetForces**

Hi! We a group called "LeetForces" and we do the `LeetForces` project.

# **Weekly reports**

{{< expand "Week 1 report" >}}

## **Team Formation and Project Proposal**


### **Team Members**

| Team Member            | Telegram ID   | Email Address       |
|------------------------|---------------|---------------------|
| Anton Nekhaev          | @anekhaev | a.nekhaev@innopolis.university     |
| Alexander Buchnev      | @pwn0id | a.buchnev@innopolis.university     |
| Vladislav Danshov      | @vladislav_danshov | v.danshov@innopolis.university     |
| Elina Akimchenkova     | @akmchnkv     | e.akimchenkova@innopolis.university     |
| Vladimir Surikov       | @MasterLogick | v.surikov@innopolis.university    |
| Georgiy Sapronov       | @qexik | g.sapronov@innopolis.university     |

### **Value Proposition**

- **Problem**: During the first-year of study at Innopolis University we (as students) faced a problem with the local code submission system called "codetest". 
    It had some fatal flaws in its implementation regarding the security aspects, as well as stability, so we decided to give our version of codetest a try.
- **Solution**: As a solution, we propose a microservice architecture system which is oriented for easier scalability, management and security. 
    The architecture consists of  several independent microservices.
- **Benefits to Users**: Our system is beneficial to future Innopolis University students and professors in the sense that the proposed system is secure (as far as 
    we are informed about existing software flaws), reliable, easy to maintain and use, scalable, and provides neat UX/UI.
- **Differentiation**: The system we develop offers Innopolis University a more secure and convenient way to check and generate assignments for students. 
    It ensures security by addressing known software vulnerabilities and offers reliability, easy maintenance and usability, scalability, and a user-friendly interface for a seamless experience.
- **User impact**: Our software project at Innopolis University has a significant impact on users, educational society, and the industry. It improves workflows 
    by offering a scalable and secure microservice architecture system for assignment submission and grading. Users are empowered with a reliable and user-friendly interface, allowing them to focus on their tasks with confidence.
- **Use cases**:
    - Assignment Submissions
    - Plagiarism Detection
    - Grading and Evaluation
    - Academic Progress Tracking

## **Lean Startup Questionnaire**
1. **What problem or need does your software project address?**
Our software project addresses the need for a secure and stable code submission system, addressing flaws in the existing
"codetest" system at Innopolis University.

2. **Who are your target users or customers?**
Our target users are the students and professors at Innopolis University who require a reliable and user-friendly 
platform for assignment submission, grading, and feedback.

3. **How will you validate and test your assumptions about the project?**
We will validate our assumptions through user interviews and usability testing gathering feedback from students and 
professors to analyze their experiences and suggestions.

4. **What metrics will you use to measure the success of your project?**
We will measure success through metrics such as user satisfaction, adoption rate, security incidents, system stability, 
assignment turnaround time, and improvements in assignment quality based on professor feedback.

5. **How do you plan to iterate and pivot if necessary based on user feedback?**
We will gather user feedback through direct communication, identifying areas for improvement and prioritizing them for 
subsequent iterations. We are open to pivoting our approach based on user feedback, ensuring the system meets the needs 
and preferences of our users.

## **Leveraging AI, Open-Source, and Experts**

1. **AI (Artificial Intelligence)**:  We will leverage AI technology to improve the code submission system through 
plagiarism detection enhancing efficiency and accuracy for students and professors.

2. **Open-Source**: By utilizing open-source libraries, frameworks, and tools, we can expedite development, reduce 
costs, and tap into the collective knowledge and contributions of the open-source community, allowing us to focus on 
customization and integration for our specific project needs.

3. **Experts in Relevant Domains**: Our team will ask for help from experts in relevant domains to achieve the best possible 
solution.

## **Defining the Vision for Your Project**
1. Summary: Our project addresses the need for a secure and reliable code submission system at Innopolis University. It 
    offers a streamlined workflow, improved security, and enhanced user experience, benefiting students and 
    professors by simplifying assignment submission and grading processes. The project fosters a culture of excellence 
    and innovation within the university community.
2. Schematic drawing:
```
                                   +-----------------+
                                   |                 |
                                   |   Database      |
                                   |  (PostgreSQL)   |
                                   |                 |
                                   +--------+--------+
                                            |
                                            |
                                            |
          +-----------------+      +--------+--------+      +-----------------+
          |                 |      |                 |      |                 |
          |                 |      |                 |      |                 |
          |  Orchestrator   +------+     Backend     +------+    Frontend     |
          |                 |      |                 |      |                 |
          |                 |      |                 |      |                 |
          +--------+--------+      +-----------------+      +-----------------+
                   |
       +-----------+-----------+
       |                       |
+------+-------+       +-------+------+
|              |       |              |
| Test runner  |       | Test         |
|              |       |  generator   |
|              |       |              |
+--------------+       +--------------+
```

As depicted above, the project consists of several modules:
- Frontend - the service which provides interaction with the user
- Backend - the service which handles requests from bot and forwards them according to their destination
- Orchestrator - the service which manages test generation and user submission execution and checking
3. **Tech stack**: Docker, docker-compose, GitHub actions CI/CD, Prometheus, Grafana, postgreSQL, Flutter, Python, 
XMLRPC.

4. **Anticipating Future Problems**:
Potential challenges during project development and deployment include technical complexities, resource limitations, 
time constraints, and dependencies on external systems. To mitigate these risks, we will plan meticulously, maintain 
open communication within the team, leverage scalable cloud services and prioritize essential functionalities.

5. **Elaborate explanations**:
- Our project utilizes a microservice architecture, enabling scalability, management, and security. Independent 
    microservices handle user authentication, assignment submission, plagiarism detection, and communication via well-defined 
    APIs.
 
- One of the critical components is the plagiarism detection algorithm, employing advanced code analysis techniques and similarity 
    algorithms to identify instances of plagiarism accurately.

- The user interface (UI) and user experience (UX) design focus on simplicity, responsiveness, and clear navigation, 
    ensuring an intuitive and visually appealing interface for assignment submission, feedback review, and grade tracking.

- We integrate AI algorithms for automated code analysis and grading, leveraging machine learning techniques to save time 
    for professors and ensure consistent evaluations.

- Our solution differentiates itself by offering a comprehensive and secure platform tailored specifically for Innopolis 
    University, providing reliability, efficiency, and a user-friendly experience for code submission and grading while 
    maintaining high standards of security and usability.

{{< /expand >}}

{{< hint danger >}}
**Feedback**  



**Value Proposition**

Good explanation. But in the use cases you have to elaborate more. You need to give details cases how your app will be used and by whom?

**Lean startup question**

Good

**AI**

Good! But how will you do the plagiarism detection. What will you use 

**Vision Of The Project**

Very good

**Overall**

The report is great, short but to the point.  

5/5

_Feedback by Moofiy_
{{< /hint >}}