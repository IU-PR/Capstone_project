---
weight: 2
bookFlatSection: true
title: "Week #2"
---

# **Week #2**

# **Introduction**

**FairLance**: Introducing Fairlance, an innovative platform that aims to provide fair opportunities to freelancers worldwide. Leveraging decentralized technologies, our website will transcend geographical boundaries, empowering freelancers to expand their reach without worrying about excessive fees, unlike other conventional freelancing platforms

<div style="text-align: center;">
  <img src="https://hackmd.io/_uploads/ryqd33sP2.png" alt="FairLance" width="600" height="300">
</div>

The adoption of our new payment method brings a significant positive impact on users. It eliminates numerous limitations that currently exist in the industry, transforming the way freelancers and service providers operate. Unlike existing websites that impose restrictions based on specific locations and pay discrepancies based on nationalities, our platform fosters inclusivity and equal opportunities for all. Join us as we revolutionize the freelancing landscape, offering a borderless and equitable platform for talented individuals to thrive and get paid securely with cryptocurrencies.

By the end of the second week in this project, we have gained a clearer vision and deeper insights. The upcoming report will provide comprehensive technical details related to the project, offering valuable additional information.

For additional information, please reach out to me on Telegram at <a href="https://t.me/AhmadAlhusein">@AhmadAlhusein</a>. 

You can check our progress in the <a href="https://github.com/AhmadAlhussin2/fairlance">project repository</a>

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**


### **Tech Stack Selection**

Now, we have a more solid vision for our project, and we can identify the major parts in it and how are we going to set the tech stack.

Our team decided to split the teck stack to three major levels:

- #### Frontend

    The frontend part of the project is actually huge, and we have many pages to handle.

    - **React**: The main framework for our project. It is the most common framework and it is suitable for teamwork.

        We decided to adapt the following strucutre for our react project:
        
        ```
            /public
                /svg
                    icons
                index.html
            /src
                /assets
                    /imgages
                    /svg
                    /styles
                /components
                    [common-components].js
                /pages
                    /Home
                    /Login
                    /Signup
                App.js
                Index.js
            package.json
        ```

        Following this structure will greatly enhance teamwork for us. We have decided to allocate different team members to handle individual pages. Each team member will be responsible for adding their respective page to the designated folder, while leveraging the common components or creating new ones as necessary. This approach is designed to minimize conflicts within our remote repository, ensuring a smoother collaborative process for all involved.
    
    - **CSS Frameworks/SASS**: Currently, we are utilizing plain CSS. However, in the upcoming weeks, we plan to transition to SASS as we require consistent styling across all pages. Initially, we refrained from adopting SASS due to our limited familiarity with the framework.

    - **useMoralis**: a powerful React framework that will greatly assist us in interacting with our smart contract. This framework is specifically designed to enhance the user experience by allowing them to effortlessly link their preferred smart wallets, including popular options like Metamask, Coinbase, and Atomic Wallet. With useMoralis, we can easily handle payment requests sent to the backend.

- #### Backend

    - **Django**: We've chosen Django, the leading Python framework, for our backend development. Its popularity and team-friendly features make it an ideal choice. We've divided responsibilities within our backend team, assigning each member a specific feature.

    - **PostgreSQL**: PostgreSQL is vital for our project due to its extensive security features, which are crucial when dealing with real money. Additionally, its recent performance enhancements make it a fast and efficient choice for handling large amounts of data.

- #### Smart contract

    We decided to make it as a seperate level because of its extra difficulty

    - **Solidity**: the main language for creating smart contracts. Our smart contract will have the following main features:

        ```solidity
        function startEmployment(sender, reciever) payable {}
        function endEmploymentSuccessfully(sender, reciever) payable {}
        function solveConflict(employer, freelancer) onlyOwner {}
        ```

        - `startEmployment` function, a sender will start a new payment transaction to the reciever.
        - `endEmploymentSuccessfully` when an employer likes the job and complete the transaction.
        - `endEmployment` is only accessible to the admins to solve conflicts.

    - **RedHat/Brownie**: Two frameworks for interacting with the smart contract. We might consider only one of them in the future

### **Architecture Design**

Designing a robust and scalable architecture is crucial for the long-term success and maintainability of your software project. This week, focus on defining the architecture that will serve as the backbone of your application. Consider the following aspects:

1. **Component Breakdown**:

    As described in the teck stack we have three main components (frontend, backend, smart contract).

    A more detailed architecture:

    ![](https://hackmd.io/_uploads/H1-mUAKvh.png)

    - #### Frontend:

        We will mainly have the following pages:

        - **Landing Page**: the entry point for our platform. Here all unauthorized users will see some examples of projects and have the oppurtunity to sign up or sign in

        - **Sign up/Sign in**: The quthorization page where users will have the option to sign in/sign up.

        - **Profile page**: users can view their profile, 

        - **Browse jobs**: This page will be for authorized users. They can see all the related jobs and apply for the job.

        - **Post infromation page**: this page contains more details about the project, and freelancer can comment here (Apply for job).

        - **Create post page**: this page is for emplyers to post oppurtunities.

        - **Messaging page**: this page to agree on details between freelancer and employer.

    - #### Backend:

        We have many features for the backend

        - **Authorization mechanism**: We will have different kinds of privillages, like unauthorized, admin, and user.

        - **Messaging system**: One of the hardest parts in our projects. We need to set it to let the user communicate with the employer. Moreoevr, we will ban sending other contact methods to prevent users from leaving our platform.

        - **Posts management**: Including fetching, posting, and editing posts. 

        - **Applying for jobs**: Comments mechanism to apply for posted jobs.

        - **Uploading CV**: to let the freelancer showcase their experience.

    - #### Smart contract:

        The payment system in general

        - **Hiring**: keep the money in the smart contract as a garantee to pay the freelancer

        - **Release**: upon successful complete

        - **Conflict management**: only for owners to decide what to do in case of conflict.


2. **Data Management**: Determine how data will be stored, accessed, and manipulated within your application. Select appropriate databases or data storage solutions based on the project’s requirements.

    *We decided to use PostgeSQL relational database system to store our data for several reasons*
    
    - Security: PostgreSQL prioritizes security and provides robust mechanisms for user authentication, data encryption, and access control.
    - Reliability and Stability: PostgreSQL is known for its robustness and stability. It is widely used in production environments for both small and large-scale applications.
    - Scalability: PostgreSQL can handle large amounts of data and can scale effectively as our project grows.

    *During the last meeting, we decided and agreed on our database structure*
    
    ![](https://hackmd.io/_uploads/BJAxHAYv2.png)

    - Skills table: Only admins can add skills to this table. Freelancers and project owners choose from this table.
    
    - Project Publication: Clients, acting as project owners, have the ability to publish projects. They provide essential details such as the project's title, description, optional media attachments, deadline, and a set of required skills. All of the previous will be stored in projects table.
    
    - Freelancers: Each user who is a freelancers specifies his skill set.

    - Applications table: Freelancers on the platform can browse through the available projects and submit applications for those that align with their skillsets. 

    - Selection Process (Employment table): Project owners review the received applications and carefully choose the freelancers they wish to hire for their projects. The selection process involves assessing the freelancers' skills, experience, and overall suitability for the specific project requirements. Once a project owner selects a freelancer, both parties enter into negotiations to establish mutually agreed-upon terms, including the project price. They determine a reasonable price within the specified range. 

    - Smart Contract and Payments: Upon reaching an agreement, the project owner and the hired freelancer proceed with the contractual arrangements. The agreed-upon price is transferred to a smart contract, where it remains securely held until the specified project deadline. If the project is successfully completed within the given timeframe, the agreed-upon amount is then transferred to the freelancer's wallet as payment for their services.

    - Messages table: Stores messages between users on the website.
    
     *Using Django REST framework and PostgreSQL we can ensure secure access and manipulation of our data from the APIs side*
    


3. **User Interface (UI) Design** 

    For design we are getting inspiration from e-commercial websites, and some public designs on figma community.
    We have already developed the landing page for our website. 
    **For now, you can check our design [here](https://fairlance-frontend-vhph.vercel.app/).**
    
    But, note that this is the initial design, and it is not functioning. We decided that showing our current work is better than showing basic scetching.
    
    In the following section we will show you the general theme to our website. 
    
    - ***Landing page first view***: the user will be directed here once entered our website

       ![](https://hackmd.io/_uploads/ry2sNnovn.png)

    
    - ***Landing page recent posts***: here the user will check recenlty posted/delivered projects to motivate him to enter our platform

        ![](https://hackmd.io/_uploads/B1aCNhiD2.png)


    NOTE: those pictures are only to show our initial design, and not final for now.

4. **Integration and APIs**: 
    *As a result of the discussion during the last meeting, we are going to implement the following API's that will interact with the database*

    - APIs to login, logout, autheticate users to add projects to projects table.
    - API to get user's information by ID or username from users table.
    - API to retrieve project's information by ID.
    - API to retrieve application for a specific project.
    - API to retrieve relevant projects for a specific user.
    - API to hire a specific user on some project.
    - API to do crypto transactions.
    - API to send messages between users.
    
    *We will use Django REST framework to implement these API's because it provides a comprehensive set of tools and features specifically designed for building RESTful APIs, it offers functionalities such as serialization, authentication, permissions, and more, which significantly simplify API development.*
    

5. **Scalability and Performance**: 
    As our project is still in the early stages, it is a still a little vague whether will it be possible for us to have both horizontal and vertical scalabilities as the website experiences increased loads. However, from the current perspective it seems more suitable to focus on scaling up (vertical scalability). In this way during the future growth of our project, we are aiming to optimize the utilization of the available resources. In addition, the approach will be cost-effective for a small team like ours
    Performance: To maintain a good performance having increased loads, we are planning to keep optimizing the content, for the example images and assets to have faster page load times. We are also planning to focus on database optimization, where we're planning to implement indexing and query optimization to ensure fast database operations.

6. **Security and Privacy**: 

    Security is our top priority at FairLance, especially considering the sensitive nature of handling customers' funds. We take this responsibility seriously and are confident in our ability to ensure the highest level of security. With our website built on the Ethereum blockchain, we benefit from the inherent security measures provided by this decentralized network.

    Furthermore, by utilizing cryptocurrency as the primary payment method, we offer an added layer of privacy for our users. Transactions conducted through our platform ensure anonymity, as payment details cannot be traced or linked to individuals' identities.

    However, to address potential conflicts between users, we have implemented some centralized technologies that facilitate dispute resolution. In such cases, only authorized administrators will have access to the relevant information. They will follow predetermined rules and guidelines outlined in our terms and conditions to resolve any conflicts promptly and fairly. Rest assured that user privacy remains a paramount consideration in all our processes.

7. **Error Handling and Resilience**: 

    In our project, if an error occurs, the employer has the authority to halt the transaction until an administrator resolves the current issue. This functionality aims to minimize the costs associated with errors. Furthermore, we have future plans to enable this feature to be directly accessible through interactions with the smart contract. This means that even if our servers experience downtime, the employer will still be able to postpone the payment until the website is operational again and all issues have been resolved.

8. **Deployment and DevOps**: 

    
    We have established our GitHub repository, which you can access and review [here](https://github.com/AhmadAlhussin2/fairlance). To ensure code quality and collaboration, we have implemented protection rules for our main branch. Any changes or additions to the main branch will require thorough reviews through pull requests before merging.
    
    Additionally, each team member will be responsible for creating their own branch to work on and represent their new feature within the project.
    
    To maintain high standards of reliability and security, we will incorporate various testing procedures before merging pull requests. This includes utilizing code linters, conducting custom tests, and performing security tests. As we progress and prepare to host our website, we plan to automate these processes using GitHub Actions.
    
    It's important to note that our project is still in its early stages, and we remain open to adopting new technologies and approaches as we continue development.


## **Week 2 questionnaire:**  

1) Tech Stack Resources: Are you utilizing any **project-based books** that specifically cover your tech stack and help you build your project? If yes, please provide the names of these books (name at least 3). How do you anticipate utilizing these materials to enhance your knowledge and expertise in your tech stack?

    - **Answer**: Currently, We are not using any project-based books. However, We are heavily relying on the documentation and resources provided by the frameworks we are using.

2) Mentorship Support: Do you currently have a mentor actively involved in your project? If yes, kindly share the name of your mentor and explain how their guidance has positively influenced your project. If you don't have a mentor yet, have you considered seeking one? How do you believe having a mentor could contribute to the success of your project? Remember, having an experienced mentor that can guide you and your team is your responsibility.
     - **Answer**: Currently, our project does not have a mentor. We haven't considered having a mentor for the project as we are still in the early stage. However, we recognize the potential benefits of having a mentor, so we might consider seeking out a mentor in later stages or challenging points in the project. 

3) Exploring Alternative Resources: In addition to project-based books, what other resources have you explored to expand your understanding of your tech stack? This could include online courses, video tutorials, documentation, or any other sources that have been valuable in filling knowledge gaps. Please, name at least 3 resources
    - **Answer**: As we said in the first question, our main resources are the documentations provided by the frameworks like Django, Django REST and React documentations.In addition to documentation, we sometimes go for popular video tutorials. Also, we always try to analyze how other popular platforms handle features and functionalities related to our platform. By thoroughly studying these resources, we are gaining in-depth knowledge about the features, functionalities, and best practices of our tech stack. This approach allows us to utilize them effectively in our project development in order to achieve security, scalability and performance.

4) Identifying Knowledge Gaps: Are there any specific areas within your tech stack where you or your team feel there are knowledge gaps or expertise is lacking? If so, how do you plan to address these gaps and ensure a well-rounded understanding of your chosen technologies? Please name the tech stack division in your team and outline how are you planning to deal with **knowledge gaps**
     - **Answer**: As second-year students, our average experience drives us to seek more knowledge and conduct extensive research for developing a fully-featured website/project. During meetings, we create detailed plans for the upcoming week, identify knowledge gaps, and search for tutorials to address those gaps. Recently, we faced difficulty in selecting the appropriate authentication method that suits the interaction betweeen our frontend/backend frameworks. As none of us have experience in this area, we are researching to bridge this gap and ensure a suitable solution for both frontend/backend teams.
     - The tech stack dicision will be like following:

         **Frontend**
        
        Due to the diverse backgrounds of our frontend team members, each individual utilizes different frameworks and technologies. However, in order to enhance our teamwork efficiency, we have collectively chosen REACT as our primary framework.

        To bridge the knowledge gap and ensure everyone is well-versed in REACT, we have devised a plan for the first two weeks. Each team member will be assigned a specific page based on their expertise, allowing them to practice and familiarize themselves with the framework. This approach aims to strengthen our skills and create a cohesive understanding of REACT within the team.
        
        - ***Ahmad Alhussin***
          Create main landing page, browsing jobs page.
        - ***Ghadeer Akleh***
          Create profile information page
        - ***Hamada Salhab***
          Create sign in/sign up, and posts pages
        
        **Backend**

        The backend team also faces various knowledge gaps, and we have adopted a similar approach as the frontend team to address this issue. Each team member will be given the opportunity to practice and enhance their skills by focusing on specific features.

        In order to effectively utilize the first two weeks, we have divided the tasks as follows:
        
        - ***Vladislav Lopatovskii***
          Create the main hiring mechanism
        - ***Ahmad Sarhan***
          Design schemas, views and models for those scheams
        - ***Yazan Kbaili***
          Authentication mechanism
        
        **Smart contracts**
    
        We acknowledge that our team lacks experience in working with smart contracts. Nevertheless, since our smart contract implementation does not involve complex technologies, we have decided to assign this particular section to a team member who possesses background knowledge in solidity
        
        - ***Ahmad Alhussin***
        

     
5) Engaging with the Tech Community: Have you actively engaged with the broader tech community to seek guidance or learn from experienced professionals in your tech stack? This could involve participating in online forums and groups (telegram, discord or any other platform), attending local meetups (Kazan, Innopolis)? Do you have means to engage experts into critical tech stack problems through professional networks? 
    - **Answer**: At present, we heavily rely on online resources for our work. By utilizing renowned frameworks in our projects, we can conveniently discover solutions to any inquiries on platforms like [Stack Overflow](https://stackoverflow.com/). Take REACT as an example, with its public repository amassing over [200,0000](https://github.com/facebook/react) stars, it offers a wealth of valuable information covering various common issues.

6) Learning Objectives: What specific learning objectives have you set for yourself and your team in relation to your tech stack this week? How do you plan to achieve these objectives, and what strategies or resources will you employ to deepen your understanding?
    - **Answer**: Our objective for this week is developing a better understanding of security practices and vulnerabilities within our tech stack.We will review documentation, security guidelines, and best practices provided by the framework creators. Furthermore, we will explore security-related articles, blogs, and tutorials specific to our tech stack.

7) Sharing Knowledge with Peers: How have you been sharing your knowledge and expertise with your teammates? Have you organized any knowledge-sharing sessions or discussions to facilitate the exchange of insights and experiences related to your tech stack?
    - **Answer**: During our regular team meetings, we make sure to discuss any challenges or issues we have encountered. We also communicate any novel techniques or tools that we come across and think the group might find useful. We've also set up a Telegram group where we can communicate and schedule meetings if necessary. Although no formal knowledge-sharing meetings have been scheduled, we place a high value on teamwork and open communication to make sure that everyone is constantly learning new things.


8) How have you leveraged AI to compensate for any lacking expertise in your tech stack? Have you utilized AI-powered tools or platforms to expedite the process of acquiring knowledge and expertise in your tech stack?
    - **Answer**: We have not leveraged AI to compensate for any lacking expertise in our tech stack. For now, we are relaying on our team's expertise and experience to develop and maintain the platform. However, we are open to explore AI tools to improve our processes and enhance the user experience.


### **Tech Stack and Team Allocation**

As mentioned in earlier sections, our approach involves assigning each team member a specific page or feature to work on. Our team is divided into parts, and during our regular meetings, we assign responsibilities for each week based on project requirements and individual strengths.

This dynamic structure allows us to adapt to changes efficiently. For instance, if a team member has dedicated more time and effort to a particular feature, we will balance their workload by assigning them a relatively easier task in the following week. This approach ensures fairness and enables us to optimize productivity while maintaining flexibility within our team.

For the first two weeks we assigned the following responsiblities to our team:

| Team Member            | Main task   | Description                      |
|------------------------|---------------|------------------------------------|
| Ahmad Alhussin         | Main Page frontend/ project structure setting | Created the general theme for our website, creating finding job page, and set the project structure    |
| Ahmad Sarhan           | Create schemas  | Designed the schemas and started creating view and models for them      |
| Ghadeer Akleh          | Profile page  | Started creating the profile page where the freelancer upload their resume.       |
| Vladislav Lopatovskii  | Hiring mechanism      | Started with creating the hiring feature in FairLance (mainly collecting job inforamtion from employer) |
| Hamada Salhab          | Log In/Sign Up, Post pages  |  Started working on the log in and sign up pages. Later will develop editing posts page      |
| Yazan Kbaili           | Athentication       | Started creating authentication mechanism with Django      |

The genaral roles are divided like following (for the long term)

**Frontend**

- Ahmad Alhussin
- Ghadeer Akleh
- Hamada Salhab

**Backend**

- Vladislav Lopatovskii
- Ahmad Sarhan
- Yazan Kbaili

**Smart contract**

- Ahmad Alhussin

---
