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
	We have created ![a simple UI sketch](https://www.figma.com/file/fECQWJjZB6fJCJnE5aKjCo/ai-roadmap.com-(Copy)?type=design&node-id=1403-2224) in Figma on how it will look like

4. Integration and APIs:
   	* We are going to intergrate with OpenAI API for determination of job-related information.

6. Scalability and Performance:
	* In order to make future changes more simple, we decided to use Airflow, since there it is simple to add new tasks in a graph of processes.
	* We have booked a server in university: 8 GB RAM, 6 CPU cores; we believe it will be enough for our purposes

7. Security and Privacy:

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
