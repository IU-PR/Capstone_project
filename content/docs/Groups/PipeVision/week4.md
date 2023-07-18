---
weight: 1
bookFlatSection: true
title: "Week 4 report"
---

# **Week #4**

### **External Feedback**

We decided to organize user acceptance testing to make sure users are satisfied with our interface.
According to the UAT requirements, conduction criteria were described:

- the prototype has the first features set - the starting point for the UAT
- the interface is accepted by the client - the end point for the testing

We designed the acceptance tests and sent them to the client.
![User acceptance test](/PipeVision/user_testing.jpeg "User test").

Then, feedback was collected.

**Feedback:**

- meaning of all buttons is intuitively understandable
- all use actions can be done easily and fast
- no error message when login or password were typed incorrectly
- no strictly defined boundaries for file extensions
- only english language is available

Overall, the client is satisfied by our design except for small details. Also, the company underlines the importance of minimalistic interface because of possibility of further integration of it in more massive projects with some changes to features. All negative remarks were proiritiesed and included in current and following development iterations.

### **Testing**

As was stated before, we estimated the drawbacks in our design by UAT.

Additionally, our software developers undertook the responsibility of manual testing, followed by the rectification of any errors discovered. This process primarily involved sessions to validate the communication between the frontend and backend components of our system, ensuring accurate message passing. Our backend developers separately carried out tests to confirm effective interaction with the database and proper data representation.

During this process, any bugs found were meticulously logged, documented, and tracked using our task management system. Bugs were then prioritized based on their severity and potential impact on the software's functionality.

Our developers then tackled these bugs according to their prioritization, examining and rectifying each issue. All bug fixes were subsequently reviewed before being incorporated into the codebase to maintain code integrity and quality.

Post-fixing, the software underwent a round of retesting to ensure the identified bugs were successfully eliminated and that the fixes didn't inadvertently introduce new bugs — a process often termed as regression testing.

All stages of this process, along with the relevant details, were written down in task comments for future reference, learning, and improvement of the testing process. This step-by-step approach helped us enhance the quality of our software product and promote efficient error management.

We refined scope of our project and understood that we chose the right vector of project development. The feautures, which should be introduced in given 7 weeks, are agreed with the customer and introduced in the task management system. We are able to implement all required features in time. So, there is no necessity to narrow the scope of the project.

### **Iteration**

**Goals and Objectives:**

In response to client feedback, our main objectives for this iteration are to improve user experience and simplify backend operations. We aim to:

- Enhance the user interface, particularly the login form.
- Provide more detailed file extension information for file uploads.
- Redesign the database structure to improve readability and formality.
- Structure the project more efficiently for easier collaborative development.
- Begin utilizing university servers for deployment.

**Features to be Developed:**

1. **Error Message in Login Form**: Design and implement an error message system in the login form to guide users through successful login.

2. **File Description Enhancement**: Modify the file description section to include details about possible file extensions to assist users during file uploads.

3. **Database Redesign**: Formalize and enhance readability of our database and its models.

**Tasks:**

**UI/UX Design**: Redesign the login form to include error messages.
**Coding**: Implement the above design in our codebase.
This task is done, the result is shown below.

![Login page](/PipeVision/login_with_error.png "Login").

**Testing**: Test the new login form to ensure it works as expected.
**File Description Update**: Code the changes in the file description and conduct subsequent tests.
This task is also done, the result is shown below.

![Browse file](/PipeVision/browse_file.png "File browsing").

**Database Redesign**: Map out a more formal and readable database design, implement it, and test the new design.

![Database design](/PipeVision/db_schema_new.jpeg "Database schema").

**Integration**: Streamline integration of frontend and backend for more structured project management.

**Deployment**: Deploy the testing version of the project on our server temporarily, and begin preparations for university server usage.

**Assumptions/Dependencies**:

**Assumptions**: We are assuming that the new design and structure will improve the user experience and efficiency of development.

**Dependencies**: The deployment on the university server depends on their availability and setup.

**Timeline**:

This iteration is planned for a span of one week. The tasks will be distributed among the team members, ensuring parallel work streams to expedite the process.

{{< hint danger >}}
**Feedback**

**Overall**<br>
Report is good. But you need to take extra care for Testing and refining the iteration plan

**Grade: 4/5**

_Feedback by Moofiy_
{{< /hint >}}
