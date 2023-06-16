---
weight: 1
bookFlatSection: true
title: "AI Career Guider"
---

# **Project: AI Career Guider**

# **Week 1**
# **Introduction**

{{< hint danger >}}

**Feedback**  
Write concise and well-written project description here. To enhance it further, we recommend incorporating additional details that provide an overview of your project. Consider including elements such as a project logo, a link to your project's webpage, or any other relevant visual materials that can help showcase your work effectively.  
As we plan to promote your work, it's crucial to ensure that this file serves as a compelling introduction that captures the attention of the potential reader. 
{{< /hint >}}

### Team members


|Team member|Telegram ID|Email Address|
| :- | :- | :- |
|Ilnar Khasanov (Lead)|ilnarkhasanov|i.khasanov@innopolis.university|
|Ruslan Kudinov|RuslanKudinov|r.kudinov@innopolis.university|
|Damir Afliatonov|Probirochniy|d.afliatonov@innopolis.university|
|Said Kamalov|SaidKbshsb|s.kamalov@innopolis.university|
|Arseni Rusin|Furry\_Lord|a.rusin@innopolis.university|
|Ivan Kornienko|VanyaKo\_Keyboardist|I.kornienko@innopolis.university|
|Sergey Milgram|MrFired|s.milgram@innopolis.university|
## Value Proposition 

### Identify the Problem 

Our application deals with the problem of profession orientation. Nowadays many people with different degrees of education face the following problem: it is hard to find a career path that suits your skills well among plenty of vacancies. Also, it is challenging to find a roadmap to develop in your field of study.

### Solution Description 

Our application provides solution by following functions:
- find a job title that suits you based on your skills and preferences
- create roadmap for found job
- find available vacancies

Uniqueness of this solution is that we provide these services just in one place.

### Benefits to Users

The main benefit is that users of our application don't need to search for all mentioned information across different sites (tests about professional orientation, roadmaps for your job, available vacancies). Consequently, it increases their productivity in terms of time saving.

### Differentiation 

The innovative feature and selling point of our application is AI integration:

- Finding a job with use of ChatGPT query.
- Creating a roadmap for a job with use of Neural Network or LLM.
- Searching for vacancies performed with use of Web Scraping.
### User Impact

In general, our application can shorten time from finding a suitable job and becoming specialist in it by creating an appropriate roadmap. 

### User Testimonials or Use Cases

In the [Based on the application of AI technology in resume analysis and job recommendation](https://sci-hub.ru/https://ieeexplore.ieee.org/abstract/document/9219491) article stated that it is possible to create competitive AI models searching by keywords for vacancy recommendation. Also, it describes the existence of future trends and opportunities for improving performance of such models.

Use Cases: Administrations of schools can integrate our service into lectures about career guidance. It can help graduates to understand better which subjects they need to pass and motivate them.
## Lean Startup Questionnaire 

1. What problem or need does your software project address?
- Our application deals with the problem of profession orientation, creating roadmaps for jobs and searching for vacancies

2. Who are your target users or customers?
- People who want to find their field of study or develop in an already found field, or who search for vacancies.
- Schools.

3. How will you validate and test your assumptions about the project?
  - We can test assumptions for our application by measurement of metrics introduced below. We can perform these evaluations in schools on professional orientation classes.
4. What metrics will you use to measure the success of your project?
  - Matching of found jobs/vacancies with user preferences.
  - Time spent by users on our site.
  - Decreased percent of school graduates who do not know what they want to do and what university/college they would like to enroll in.
6. How do you plan to iterate and pivot if necessary based on user feedback?
- We can change AI model for Web Scraping or even add more functional 
## Leveraging AI, Open-Source, and Experts

1. AI (Artificial Intelligence):
- ChatGPT for finding a job and creating a roadmap.
- Web Scraping for searching for vacancies
2. Open-Source:
- Search for existing solutions (for inspiration) in fields of AI application for finding vacancies.
3. Experts in relevant domains:
- You can see our team distribution in the “Tech Stack” subsection below.
## Inviting Other Students
We created our team based on every team member’s hard skills and stack. You can see our team distribution in the “Tech Stack” subsection below.

### Overview

The problem addressed by the application is the difficulty faced by people in finding a career path that matches their skills and preferences. The solution is to create an application that provides services such as finding a job, creating a roadmap for the job, and finding available vacancies. The application's uniqueness is that it provides all these services in one place. The benefits of the application are it saves time for users by providing all the information they need in one place. The application differentiates itself by integrating AI, which is used for finding a job and creating a roadmap, as well as web scraping for searching for vacancies. The application can help users save time by shortening the time it takes to find a suitable job and become a specialist in that field.

### Schematic Drawings
![](/AICareerGuider/architecture.png)


### Tech Stack

|Team member|Tech stack|
| :- | :- |
|Ilnar Khasanov (Lead)|Python: FastAPI, SQLAlchemy, alembic, Airflow; Databases: PostgreSQL; Docker|
|Ruslan Kudinov|Python: pandas, pytorch, scikit-learn, numpy|
|Damir Afliatonov|Python: FastAPI, SQLAlchemy, alembic, Airflow; Databases: PostgreSQL; Docker|
|Said Kamalov|python, pandas, scikit-learn, numpy, pytorch, MySQL, postgreSQL; Docker|
|Arseni Rusin|React|
|Ivan Kornienko|Python: pandas, pytorch, scikit-learn, numpy; Databases: PostgreSQL; Docker|
|Sergey Milgram|Python; GitLab CI/CD; Docker; Kubernetes|
### Anticipating Future Problems
- High-load of our service.
- Technical complexities related to integration of AI.

### Elaborate Explanations
- Front-end and back-end parts will work with each other using Rest API. Also we have introduced a “Query Interface” component that will remove a dependency of the front-end from the backend.
- All our ML-related parts will be processed in Airflow in order to pipeline them.
- We are also going to collect data and store it into the database in order to create a statistics dashboard in Grafana and make some decisions based on it. 

{{< hint danger >}}

**Feedback**  
It is an interesting project! Great job on identifying the problem that candidates face in job determination. Career paths can be complicated and I think it is important that your team tries to make it as straightforward as possible. Your app can greatly benefit career development by allowing users to see realistic track that is required for a given profession.

To further enhance your project, consider expanding on the specific features and functionalities that will be offered to users. Will the AI simulate career paths? Will your app include only IT professionals or some other professions too?

Overall, I think you have a great team and a very nice project. Try to scale it down to some core features and develop a detailed execution plan (as it currently stated it can be too big for 6 remaining weeks){{< /hint >}}

# **Week 2**

## Tech Stack Selection
1. Programming languages:

  	* Python for ML and back-end part
	* JavaScript for front-end part
	* SQL for databases

2. Frameworks:

	* React for front-end part
	* FastAPI for building API's with Python
	* Airflow for monitoring workflows
	* Scrapy for Web Scraping

3. Technologies:

	* Web Scraping for vacancies searching
	* OpenAI for interaction with ChatGPT queries
	* PostgreSQL for databases
	* Docker


## Architecture Design
1. Component Breakdown:

	![](https://github.com/IU-PR/Capstone_project/blob/AICareerGuide/static/AICareerGuide/architecture.png)

	* Front-end and back-end are "agreeing" on an interface of REST API messages and work with each other using that.
	* Backend trigger Airflow Directed Acyclic Graph in order to start processing the query of the user.
	* In the Airflow DAG we are going to determine:

		* Job title
		* Roadmap for that
		* Vacancies on the given job title
	
 	* Also in the Airflow DAG we are going to have a task for collecting the data; based on it we will create an internal or external statistics

2. Data Management:
	As we said, we are going to manage all our data in the Airflow DAG

3. User Interface (UI) Design:
	We have created [a simple UI sketch](https://www.figma.com/file/fECQWJjZB6fJCJnE5aKjCo/ai-roadmap.com-(Copy)?type=design&node-id=1403-2224) in Figma on how it will look like

4. Integration and APIs:
   	* We are going to intergrate with OpenAI API for determination of job-related information.

6. Scalability and Performance:
	* In order to make future changes more simple, we decided to use Airflow, since there it is simple to add new tasks in a graph of processes.
	* We have booked a server in university: 8 GB RAM, 6 CPU cores; we believe it will be enough for our purposes

7. Security and Privacy:

	* The code of the app will be analyzed for potential security issues as a part of CI pipeline.
	* User can communicate with the app only through its web API. The internal parts of the app will be isolated in a different Docker containers.
	* The app will not store any user's personal information, only the anonymous API request data for statistics and future improvements.

8. Error Handling and Resilience:
   	* Errors will be logged in Airflow

10. Deployment and DevOps:
    * We will use GitLab as version control and for CI/CD. The app will be deployed as a Kubernetes cluster of Docker containers.

## Week 2 questionnaire
1. Tech Stack Resources:

	* We don't use any project-based books.

2. Mentorship Support:

	* We don't have any mentor.

3. Exploring Alternative Resources:

	We checked different solutions with simular functionality:
	
	* [AI Roadmap Generator](https://ai-roadmap.com/) for creating career path roadmap
	* Professional orientation tests ([this](https://www.careerexplorer.com/career-test/) and [this](https://www.123test.com/career-test/)) for exploring possible questions to apply based on their results OpenAI query.

4. Identifying Knowledge Gaps:

	* Our team have knowlegde gaps in prompt engineering with usage of OpenAI API, Scrapy. So, we will deal with it by self-learning.

5. Engaging with the Tech Community:

	* We search for information on forums dedicated for specifics topics to get rid of knowledge gaps (for example, formatting of responses from ChatGPT)

6. Learning Objectives:

	* We set up following tasks in Trello for current week:

		* Create repository.
		* Create prototype of UX/UI design.
		* Create pipeline in Airflow.
		* Learn OpenAI API.
		* Collect questions for professional orientation test

7. Sharing Knowledge with Peers:

	* We have Tech Lead in each team (Frond-end, Back-end, ML) who is responsible for sharing knowlegde.

8. We used ChatGPT to expedite the process of acquiring knowledge.
## Tech Stack and Team Allocation 
Again, distribution of our responsibilities is:
|Team member|Tech stack|
| :- | :- |
|Ilnar Khasanov (Lead)|Python: FastAPI, SQLAlchemy, alembic, Airflow; Databases: PostgreSQL; Docker|
|Ruslan Kudinov|Python: pandas, pytorch, scikit-learn, numpy|
|Damir Afliatonov|Python: FastAPI, SQLAlchemy, alembic, Airflow; Databases: PostgreSQL; Docker|
|Said Kamalov|python, pandas, scikit-learn, numpy, pytorch, MySQL, postgreSQL; Docker|
|Sergey Milgram|Python; GitLab CI/CD; Docker; Kubernetes|
|Arseni Rusin|React, JS|
|Ivan Kornienko|Python: pandas, pytorch, scikit-learn; Databases: PostgreSQL; Docker|

We ensure that each team member was effectively assigned to appropriate tasks and responsibilities within the project by assigning tasks and their status in Trello and providing regular meetings dedicated to each team member's progress.
