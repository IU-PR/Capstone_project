---
weight: 3
bookFlatSection: true
title: "Week #3"
---

# **Week #3**


## **Developing the first prototype, creating the priority list**

You can check our progress on [FairLance github repo](https://github.com/AhmadAlhussin2/fairlance), and for the frontend part on [fairlance frontend](https://fairlance.netlify.app/).

<div style="text-align: center;">
  <img src="https://hackmd.io/_uploads/ryqd33sP2.png" alt="FairLance" width="600" height="300">
</div>

Throughout the week, significant advancements have been made in backend, frontend, and smart contract development. The following accomplishments are outlined in the report:

- Substantial progress has been made in implementing the backend.
- The user interface is nearly complete; a few additional pages need to be created and linked to the backend.
- The smart contract is almost finished; further discussions are required to determine additional features or the removal of unnecessary ones.
- We have implemented automated tests for our smart contract to ensure its functionality.


## **Progress report**:  

 - ### Prototype Features:
   We have implemented the following features/functionalities so far:
   
   - **Applications**: the API allows to create new applications, retrieve a list of applications for a particular project and application details, delete and update applications.
    - **Employments**: it provides functions such as creating a new employment record, list all of  employment records, getting a specific employment record, deleting and updating a record.
    -  **Projects**: users can create a new project, update a project, delete a project, get a range of projects based on indexes, get a specific project
    -  **Users**: it manages user-related functions such as signing up, signing in and etc.
    
    **Core interactions** that are essential to our project's goals are user registration/authentication, profile management, job posting, hiring a freelancer and payment processing(including crypto payments).
    
    **User flows:**
    
    - Freelancer registration and profile setup:
        1) User signs up on our platform
        2) User completes the profile by adding skills, cv/portfolio.
    - Client registration and job posting:
        1) User signs up on our platform
        2) User creates a project by providing details/requirements
        3) User posts the project
    - Freelancer job search and application process
        1) Freelancer signs in and searche for available projects
        2) Freelancer reads project details
        3) Freelancer submits proposal for selected projects
    - Client project hiring
        1) Client reviews proposals for their project
        2) Client selects a freelancer and starts a price negotiation process that includes asking and answering questions
        3) Client approves the deal, freelancer takes the project
    
    **Data Management**:
    
    - Users: the platform stores user data, credentials and profiles.
    - Applications: the platform stores application data such as project id and freelancer id.
    - Employments: the platform stores employment data such as application id and payment id.
    - Payments: the platform stores payment data such as payer and payee ids, amount and date.
    - Projects: the platform stores projects details(id, owner, title and etc).
    - Skills: the platform stores data about skills(required and available)
    - Messages: the platform stores message data such as id, sender and recevier ids, date and content of the message. 
    
    **Smart Contract**:
    
    - We have implemented the smart contract, created tests, which you can view in [contract branch](https://github.com/AhmadAlhussin2/fairlance/tree/contract) in our repository.
    - Moreover, the contract is deployed on Seploia test network, and can be viewed [here](https://sepolia.etherscan.io/address/0x57f34f39b4bb009e43b695d618d17a65c7b97a52#code).
    - Howver, the contract is not ready for production yet, since we need to create more tests and more features. We plan to deploy it on main net in the last steps only.
    
 - ### User Interface: 
 
    You can check our initial design on https://fairlance.netlify.app/, we have made significant progress in frontend development.

    **PLEASE NOTE**: this is only frontend demo, we have not linked our backend with the frontend yet, we plan to do it during the next week.

    Here you can find some explainations about the website:

    -  **Landing Page**: This webpage is designed for first-time users visiting our website. Here, users can explore recent post examples, view completed projects, and find a brief introduction to our website.

        In the initial view, users have the option to either post a job (by clicking on "Find a Freelancer") or search for a job using the search bar. Additionally, the navigation bar provides links to various pages, including login, signup, home, and job listings.

        ![](https://hackmd.io/_uploads/B1e_Yg8d2.png)

        Below, you will find a selection of recent job examples and completed projects.

        ![](https://hackmd.io/_uploads/Byyw9g8un.png)

        Finally, you reach the footer, where you can find the FAQ page, home, and some pages that are not ready yet.

        ![](https://hackmd.io/_uploads/HJsXieUd2.png)

    - **Finding jobs page**: Here, you will be directed to find a matching job. You can use filters based on categories, budget, time to finish the project, and minimum rating for employers. 

        Search bar to find a matching job, some projects

        ![](https://hackmd.io/_uploads/r1ly6e8_3.png)

        Some extra filters and more posts

        ![](https://hackmd.io/_uploads/rJDr6lIun.png)

    - **Signin, Signup pages**: Here, the user can enter his details to signin or signup.

        ![](https://hackmd.io/_uploads/ryVc6lUO2.png)

    - **FAQ page**: Here you can find some frequently asked questions.

        ![](https://hackmd.io/_uploads/S1JZk-Iuh.png)


 - ### Challenges and Solutions:
 
     - This week, we encountered some issues with a smart contract. As we explained in the previous reportes, the transaction process works according to the following: When a project owner hires a freelancer, the payment amount is transferred from the project owner's wallet to a smart contract, where it remains until the deadline for project completion.
     - We earn money by cutting a small ratio of the price from 5% to 10% depending on the total amount (we haven't firmly decided on that yet).
     - The issue we're facing is that every interaction with the smart contract incurs an unpredictable cost, sometimes resulting in high expenses. Additionally, as we store more information in the smart contract, such as deadlines, senders, receivers, and other relevant details, we require additional interactions, which further increases the associated costs.
     - If we store a large amount of information in the smart contract, the transaction costs may exceed the percentage we earn from the project price, resulting in financial losses, particularly in the initial stages of the website. 
     - In order to provide a solution, our decision was to design a minimalistic smart contract. This approach involves refraining from storing excessive project-related information in the contract, as we determined them to be unnecessary. Additionally, the contract will incorporate a whitelist functionality, enabling us to select the most stable and cost-effective stable coin (such as BUSD, USDT, etc.) for integration. All extra functionalities will be implemented in the backend.
   
- ## Next Steps:
  
  - Our very next step is going to be deploying the backend and connecting it to the frontend and make sure that they are integrated properly. This should probably be achieved before the end of this week.
  - Concurrently, the backend should also be connected to smart contract that's deployed on the test network.
  - Next, we are planning to add more features, such as:
      1- Payment System.
      2- Messaging system.
      3- Search functionality & filtering (we might apply ML if we have enough time).
  - As we are working without a designer, we are planning to reassess the design and solve the minor issues we are (and will be) encountering along the way.
  - Finally, the smart contract needs to be deployed on the main network.
      

---