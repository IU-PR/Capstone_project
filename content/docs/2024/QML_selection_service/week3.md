# Technical Infrastructure

This week, the primary focus was on ensuring that the technical infrastructure necessary for prototype development was fully operational. The shared development environment, including frameworks and platforms, was successfully set up. This involved accessing to QPU and Hybrid QPU servers to support the prototype. Training sessions were organized for all team members to efficiently utilize this infrastructure, ensuring a smooth development process.

## Backend Development

Backend functionalities implemented so far include:

- **Creation of Tables and Migration Files:** We have set up tables for managing user data and reports. Specifically, a user table and a report table have been developed.
- **Data Migration:** Ensuring seamless data migration between different database schemas was a challenge. This was addressed by thoroughly testing the migration scripts in a staging environment before deploying them to production, which helped maintain data integrity and minimize downtime.

## Frontend Development

Frontend components developed include:

- **UI Components:** Key user interface elements have been built, following the wireframes created earlier.
- **State Management:** Implemented state management to handle the dynamic nature of the application.
- **Firebase Authentication:** Set up authentication using Firebase to manage user logins securely.
- **Navigation:** Developed the navigation structure to ensure an intuitive and user-friendly interface.

Here are some screenshots of the UI elements (design options):
![UI Screenshots](/2024/QML_selection_service/design_options_main_page.png)

## Data Management

Data management capabilities set up include:

- **MySQL Database:** Implemented MySQL to manage the storage of reports and user information.
- **PDF Storage:** We are evaluating the best approach to store PDF files, considering either storing them directly within the database or serving them from a public file server. The challenge here is to determine the most efficient and secure method for PDF storage that balances performance and accessibility.

## Prototype Testing

Initial rounds of testing have been conducted, focusing on:

- **Device Compatibility:** Testing the frontend on different devices to ensure responsiveness and usability.
- **Feature Functionality:** Creating tests to verify the implemented features against defined user flows and scenarios.

Feedback from team members has been collected to identify and address usability issues or bugs. Refinements have been made based on this feedback to improve the user experience.

## Challenges and Solutions

- **Backend Data Migration:** Ensuring seamless data migration between different database schemas was a significant challenge. This was overcome by thorough testing in a staging environment before production deployment.
- **Quantum Annealing Performance:** Achieving fast solutions using the quantum annealer was challenging. We resolved this by employing different embedding methods, which proved successful.

## Next Steps

- **Expand Experiments:** Conduct more experiments on various benchmarking datasets to evaluate the performance of the feature selection using the CQM solver.
- **Web Application Development:** Continue with the web application development, focusing on features that highlight the differences between quantum machine learning (QML) selection and classical methods.
- **Enhance UI:** Further develop the user interface to improve user experience and functionality.
- **Optimize Data Management:** Finalize the approach for PDF storage, ensuring it is both efficient and secure.

## Conclusion

The goal for this week was to develop a functional prototype that demonstrates the core features and user experience of our project. Significant progress has been made in both backend and frontend development, data management, and initial testing. We will continue to build upon this foundation in the upcoming weeks, with a focus on expanding our experiments and enhancing the web application.
