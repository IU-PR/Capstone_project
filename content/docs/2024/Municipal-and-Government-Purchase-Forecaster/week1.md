# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Team Member (Lead) 1     |  Ogurchik_VOO |    e.erokhin    |
| Team Member 2            | daniilzimin4  |     d.zimin     |
| Team Member 3            |    dewroman   |    r.pakhomov   |
| Team Member 4            | urlittlesister|il.krasheninnikov|
| Team Member 5            |   dema_koder  |     d.zverev    |
| (Optional) Team Member 6 |    tanellD    |    d.davydov    |
| (Optional) Team Member 7 | gotterkiller  |   n.shaydullin  |

### **Value Proposition**

- Identify the Problem:

    The manual process of tracking inventory, analyzing demand, and planning procurement in government agencies is time-consuming, inefficient, and prone to errors.

- Solution Description:

    An AI-powered chatbot integrated with a data visualization tool that allows users to view warehouse inventory, visualize data through diagrams/graphs, forecast procurement needs, and generate purchase requests in JSON format.

- Benefits to Users:

    Streamlined inventory management, automated demand forecasting, and simplified procurement processes. Users can quickly access accurate inventory data, visualize trends, and generate precise procurement plans.

- Differentiation:

    Our solution leverages AI to categorize procurement data, predict consumption levels, and automate request generation, providing a more efficient and error-free approach compared to manual methods.

- User Impact:

    Users will save time, reduce manual workload, and improve accuracy in procurement planning. This leads to more efficient resource management and better allocation of budgetary funds.

- User Testimonials or Use Cases:

    A government agency's procurement team needs to generate procurement requests for cleaning supplies based on forecasted consumption.

    Steps:

    1. A team member logs into the chatbot via the Telegram application.
    
    2. They request the forecasted consumption of cleaning supplies for the next quarter.
    
    3. The chatbot categorizes the cleaning supplies as a regular procurement item and predicts the consumption levels.

    4. The team member requests a JSON file with the recommended quantities of cleaning supplies for the next quarter.

    5. The chatbot generates and sends the JSON file, ready for submission to the procurement department.

    Outcome:
    
    The procurement team efficiently generates accurate procurement requests, ensuring that the agency maintains an adequate supply of cleaning materials without overstocking. This automation saves time and reduces the manual workload.

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address? 
   
   The project addresses the inefficiencies and inaccuracies in manual inventory tracking and procurement planning in government agencies.

2. Who are your target users or customers?

   Our target users are the executive authorities of Moscow and their subordinate state institutions.

3. How will you validate and test your assumptions about the project?

   We will validate our assumptions through pilot programs with select government agencies, gathering feedback and refining the system based on real-world use and user input.

4. What metrics will you use to measure the success of your project?

   Key metrics include reduction in time spent on inventory management, accuracy of demand forecasts, user satisfaction ratings, and the number of successfully automated procurement requests.

5. How do you plan to iterate and pivot if necessary based on user feedback?

   We will use an iterative development approach, incorporating user feedback into regular updates and enhancements. If significant issues are identified, we will pivot our strategy to better meet user needs, focusing on the most critical pain points.

## **Leveraging AI, Open-Source, and Experts**

Our team leverages advanced AI algorithms to categorize and forecast procurement needs, utilizes open-source data visualization libraries to create user-friendly interfaces, and collaborates with procurement experts to ensure our solution meets the specific requirements of government agencies.

## **Defining the Vision for Your Project**

- Overview: The project aims to create an AI-powered procurement assistant for government agencies in Moscow, automating inventory management, demand forecasting, and procurement request generation to improve efficiency and accuracy.

- Schematic Drawings: The system includes a web/desktop chatbot interface accessible via applications like Telegram, where users can log in, request inventory data, receive visual forecasts, and generate JSON procurement requests for integration with external systems.
![UML Sequence Diagram](/2024/Municipal-and-Government-Purchase-Forecaster/UML.png)

- Tech Stack:
    
    java spring
    python: pandas, sklearn
    telegram api
    docker
    mongodb
