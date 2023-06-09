# **CockTail**

Hi! We are team CockTail and our project is an AI which generates a cocktail based on customer's preference! Here we will publish our weekly reports with tasks we've completed during the last sprint and our goals for the next one.

# **Week 1**

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member | Telegram ID | Email Address |
| --- | --- | --- |
| Leonid Zelenskiy | RamPrin | l.zelenskiy@innopolis.university  |
| Polina Bazhenova | poleeknow | p.bazhenova@innopolis.university |
| Ksenia Shchekina | KseniaSchekina | k.shchekina@innopolis.university  |
| Arina Yartseva | YarikaAA | a.yartseva@innopolis.university  |
| Irina Shchetinina | sch_irina73 | i.shchetinina@innopolis.university  |
| Alexander Agafonov | seoful | a.agafonov@innopolis.university  |

### **Value Proposition**

- **The problem:**
    
    Regular bar visitors often face a problem with the lack of variety of the cocktails offered by the bar list. Furthermore, a lot of bartenders, especially beginners, have difficulties with selecting ingredients for cocktails based on the customers' preferences. At the initial stage of the career, it is hard for them to remember every pair of well combined ingredients, and after a certain stage, their job for them becomes a routine and there is no place for creativity in it. Therefore, the bar list contains just few typical cocktails, and bartenders offer them to customers without taking into account their preferences. Thus, the choice of a cocktail falls entirely on an inexperienced client and the average bartender cannot help him/her.
    
- **Solution Description:**
    
    Our project will help bars varify their range of cocktails. We will create a website, the main idea of which is to complete the chain of the most suitable ingredients for the given component based on the already existing cocktail compositions from the dataset.
    
- **Benefits to Users:**
    
    Our project will help with the selection of the best ingredients for cocktails, and in addition further expand their diversity. Thus, the quality of the bar service will reach a new level.
    
- **Differentiation:**
    
    Among the popular applications there is VIVINO. One of its functions is to select the appropriate wine for the user at his/her request. However, this function is not the main one, so it does not work perfectly. In addition, this application theats exclusively to wines. We suggest an idea that will be used by bars for increasing offered assortiment.
    
- **User Impact:**
    
    The customers of such product will be bar as a company and the users will be its staff. It simplifies the work of the bartenders. As well as a qualitative increase of the assortiment will lead to an increase in profits and popularity of the institution.
    
- **User Testimonials or Use Cases:**
    - One of our early adopters, a bartender named John, shared his experience: "This tool has been a game-changer for me. I've been able to create new and exciting cocktails that I would have never thought of on my own. It's also been a hit with the customers. They love being able to try new cocktails that are tailored to their tastes."
    - In another instance, a bar owner, Lisa, reported a significant increase in customer satisfaction and repeat business after implementing our software. She said, "Our customers love the personalized experience and the variety of cocktails we now offer. It's been a great way to differentiate our bar from others in the area."
    
    These testimonials highlight the value and benefits of our software project, demonstrating its potential to enhance the bar experience for both bartenders and customers.
    
## **Lean Startup Questionnaire**

1. What problem or need does your software project address?
    
    *Problem of choosing the cocktail ingredients*
    
2. Who are your target users or customers?
    
    *Customer of our product is bar, but direct users will be bartenders*
    
3. How will you validate and test your assumptions about the project?
    
    *We ask our users to estimate the result (cocktail)* 
    
4. What metrics will you use to measure the success of your project?
    
    *Client satisfaction, time of performance* 
    
5. How do you plan to iterate and pivot if necessary based on user feedback?
    
    *The high-rated combinations will be included to list of possible cocktails and will take account and suggested to other users*

## **Leveraging AI, Open-Source, and Experts**

- AI (Artificial Intelligence):
    
    *To do this task we will use NLP model for working with text. Also the dataset  of cocktails recipes that we have do not contain any information about the cocktail flavor.  For that purpose we will use OpenAI Chat-GPT source.*
    
- Open-Source:
    
    *For this moment we found several public datasets in Hugging Face. We will combine them to one and delete unnecessary information. For the backend part we choose Django library, for the frontend part Flatter, and for the model architecture Keras library.*
    
- Experts in relevant domains:
    
    *We decided to interview the employees of bar 108 as experts in this field.*
    
## **Inviting Other Students**

*We decided to create the [questionary](https://docs.google.com/forms/d/e/1FAIpQLSfcoTU38QmN0moZWnntJ6nfX4XqCXoBfU2Ch17iDytjc9r2tw/viewform?usp=sf_link) about personal experiences in selecting cocktails.*

## **Defining the Vision for Your Project**
- **Overview:**
    
    Our project will direct to the domain of bar companies. Our product will produce the cocktail composition from ingredients. It will help bartenders with making cocktail for client preferences and also will solve problem of poor bar list by providing new cocktail recipes. The bar service quality will increase due to this, hence the bar business will go up.
    
- **Schematic Drawing:**
    
    {{<mermaid>}}
    
    graph TB
      U["User"] -- "Chooses Ingredients" --> M["Website/Model"]
      M -- "Selects Best Combinations" --> D["Database"]
      D -- "Checks for Complete Cocktail" --> M
      M -- "Offers Ready-Made Cocktail" --> U
      M -- "Store high-rated combination" --> D
      U -- "Rates the Combination" --> M
      linkStyle 0 stroke:#2ecd71,stroke-width:2px;
      linkStyle 1 stroke:#2ecd71,stroke-width:2px;
      linkStyle 2 stroke:#2ecd71,stroke-width:2px;
      linkStyle 3 stroke:#2ecd71,stroke-width:2px;
      linkStyle 4 stroke:#2ecd71,stroke-width:2px;
      linkStyle 5 stroke:#2ecd71,stroke-width:2px;
    
    {{</mermaid>}}
    
- **Tech Stack:**
    
    For frontend: Flutter framework
    
    For backend: Python, Django framewok
    
    For model: Keras library
    
- **Anticipating Future Problems:**
    
    Probably, during the process we can face challenges with databases combination. The learning of model also can be time consuming. To mitigate this problem we can use GPU and faster algorithms
    
- **Elaborate Explanations:**
    
    In out project we wil use NLP model to transform text data to the vectors. 
    
    Nowadays, there are no popular analogues of such idea that used in bar industry.
