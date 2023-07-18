---
weight: 1
bookFlatSection: true
title: "AI Career Guide"
---

# **Project: AI Career Guide**

# **Week 1**
# **Introduction**

In an ocean of different paths, finding a career that suits *you* was never an easy task. Some people do not know were to start, while others question themselves about the choice after few steps.

![Logo](/AICareerGuide/AICareerGuide.pdf)

**AI Career Guide** is an [open-source](https://gitlab.com/ai-career-guide) online service that helps people find and follow their career path. By completing series of single choice questions about their preferences, a person receives *AI-generated job suggestions* that suit them. The Guide offers *roadmaps* for the suggested careers to make learning easier and *real vacancies* to motivate people.

You can check out the Guide at https://aicareerguide.ilnarkhasanov.com/ 

**Note:** only job suggestions in IT are available at the moment

Our final ![presentation](/AICareerGuide/presentation.pdf)!

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
![](/AICareerGuide/architecture.png)


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
	* Docker and Kubernetes for deployment and monitoring


## Architecture Design
1. Component Breakdown:

	![](/AICareerGuide/architecture.png)

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
   	* We are going to integrate with OpenAI API for determination of job-related information.

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

# **Week 3**

# Developing the first prototype, creating the priority list

## Technical Infrastructure: 
- We got the Ubuntu server from IU IT department and now we are setting up the CI/CD on it and preparing for the production. Also, we are working on domain for site for user access.
## Backend Development:
- We created a backend app that receives a data from the frontend and push it to the directed acyclic graph in the Airflow, waits for the result that should appear in RabbitMQ and returns it back to the frontend.
- Considering machine learning part, we have successfully integrated the career path suggestions feature into our backend. Our focus now shifts towards roadmap generation. We have defined a prompt structure for the OpenAI API and conducted preliminary experiments with few-shot prompting. The next step is to integrate this feature into our MVP.
The primary challenge lies in parsing the output from the GPT-model to a structured roadmap. This process necessitates a well-defined format for the roadmap. Our proposed solution is to acquire the roadmap as a string from the OpenAI API. This string will adhere to the structure of an enumerated list (i.e., 1, 1.1, 2, 2.1, 2.2, etc.).
- API response example:
  ![Components](/AICareerGuide/API.png)
## Frontend Development: 
- We created prototype using Figma. You can check it [here](https://www.figma.com/file/QDNRpes5bziKwAiKtTkM7Z/Untitled?type=design&mode=design&t=IO44qdhNKYF3DT6s-1).
- Here you can see the stucture of project in React:   
  ![Components](/AICareerGuide/components.png)
- Priority of functionality:
  1. Home page (_Home.js, Header.js components_).
  2. Questions pages (_Question.js_).
  3. Rendering results of user (_Result.js_).
  4. Applying design from Figma.
## Data Management:
We have a Airflow directed acyclic graph that it responsible for the data processing. At this particular moment our dag can receive the answers on the questions and return the job titles that correlates to the user's interests.
## Prototype Testing: 
- As you can see below, our Figma prototype is quite simple:
![Prototype](/AICareerGuide/prototype.png)
- It performs following flow:
  1. Renders main page and starts quiz after clicking "Start" button.
  2. Give a user opportunity to iterate back and forward among questions.
  3. After answering all questions, redirects user to page with rendered results.
# Progress report
## Prototype Features:
At this moment, following workflow has been implemented:
  1. Renders main page and starts quiz after clicking "Start" button.
  2. After this click, front-end part receives JSON with questions and renders them one by one.
  3. Then front-end part sends POST request with all answers choosen by user and receives results from Airflow pipiline in JSON format.
## User Interface: 
In detailes, there is such routing in prototype:
- On the main page, user can click button "Start" to move to questions:
  ![Main](/AICareerGuide/main.png) 
- User can iterate back, forward or finish answering questions depending on number of question. Also, all questions are multi-choice.
  
  ![FirstQuestion](/AICareerGuide/first_question.png)
  ![MiddleQuestion](/AICareerGuide/middle_question.png)
  ![LastQuestion](/AICareerGuide/last_question.png)
- The last page in prototype is thedown  page with user results: suitable vacancies and roadmap. Maybe, later we can make each "vacancy" component clickable and provide more information about vacancy after click.
  ![Result](/AICareerGuide/result.png)
## Challenges and Solutions:
- Public IP address for our server. The solution is VPN to the university network in order to make it accessible for the GitLab CI/CD.
- The API we're currently using is not capable to fetch key skills from each job offer. The solution is to use OpenAI technology which obtains job offer description as input and returns the array of key skills as output.
Next Steps - make app applicable for HeadHunter in order to get their API key.
- Domain for our service.
## Next Steps:
* Publish prototype in the Internet.
* Add new features as roadmaps and vacancies.

## Code Repository:
https://gitlab.com/ai-career-guide/backend/-/tree/develop?ref_type=heads

{{< hint danger >}}
**Feedback**  
I appreciate the transparency in sharing the progress of the project and the inclusion of the Week 2 questionnaire responses. It's good to see the allocation of team members and their responsibilities, ensuring efficient task distribution. The mentorship support may be lacking at the moment, but the team's proactive approach to learning and leveraging resources like ChatGPT is commendable.

The Architecture Design is clear and provides a good overview of how the different components interact with each other. I particularly like the use of Airflow for monitoring workflows and the integration with OpenAI for job-related information.

Consider visiting the MockMentor project page, I think you may want to collaborate and perhaps even join your projects in the future. Finally, I'm excited to see the development of the first prototype in Week 3. Keep up the great work, and I look forward to the continued success of our project. 
Overall, nice progress and thoughtful reports - 5/5 for both weeks.  
{{< /hint >}}

# **Week 4**

# External Feedback
For feedback, we asked people with different knowledge of IT. So, the results are:
- A person who does IT optionally:
> This test that is used to determine the path for IT career development is useful, since it pays attention to personal skills and interests.
I have passed it from my phone. The text was readable. However, it does not fill well to the boxes. There is still some work for improvement.
Anyway, I highly recommend this service for those who have not decided their IT career path.
- Software Development student from Kazan Federal University:
> In general, I like this service because it has suggested some ways I can develop myself in IT. I have really liked it. However, when I opened the website at the first time, I could not start the test.
_(Authors remark: we really had this problem; we have updated nginx's config, but did not reload its Docker container; already fixed)_.
Also, the website loads very slow (specifically at the start and while getting the results).
Moreover, I'd like the choice buttons to be bigger.
Anyway, I liked this service!
- A person who isn't related to IT:
> Overall, this site provides useful functionality and can be interesting for people involved in IT. By the way, I found some problems with the User Experience; for example, I can't move to the previous question if I haven't answered the current one.


# Testing
- Unit and integration testing:
  - We have introduced them in Docker. When we build a backend image, we always check the unit tests since they are checked very fast and isolately. We have also introduced integration tests, that we run in different Docker image, since they need some time to be processed.
- User Interface/User Experience testing:
  - We tested the front-end part (by ourselves and with the help of external feedback) and found several bugs in our prototype:
    - Mobile version of our application is not responsive.
    - User can't move back to the question until he selects an option. It is not very convenient for the user.
    - Favicon isn't displayed.
# Iteration
- Front-end part:
  - We added new functionality to our site:
    - Top 5 suitable job titles render on the _/results_ page:
![Results](/AICareerGuide/results_MVP.png)
  - We improved the User Experience:
    - User can't iterate forward or back until he selects an option. Also, if he moves to previous questions, he can see already selected answers:
![Iteration](/AICareerGuide/iteration.png)
- Back-end part:
  - Perform Unit and integration tests for the "Testing" section.
- ML part:
  - This week we solved the primary challenge that we defined the previous week: roadmap generation. We defined a prompt format as a numbered list with two levels of depth. It is important to notice, that we again used the few shots prompting technique to achieve a specific format of response. Also, we did research on function calling, a relatively new feature in the OpenAI API. Unfortunately, we did not have any idea how to apply this functionality to our project.
- DevOps part:
    - We deployed our site on the Vercel using domen http://aicareerguide.ilnarkhasanov.com
    - We have used Ilnar Khasanov's domain in order to deploy on public domain for free.
    - Our backend is running on test servers at Yandex.Cloud, also for free.
    - Backend is available at https://api.aicareerguide.ilnarkhasanov.com as well.
    - We have used Let's Encrypt in order to generate SSL-certificate for free.

{{< hint danger >}}
**Feedback**  
Alright, I like your tempo and fact that all parts are deployed and people already can see what is your project is about. Good job. There are still some work to do, so don't miss the chance to make it a complete project.
Overall, 5/5 for the week
{{< /hint >}}

# **Week 5**

## Feedback collection

To improve the user experience for our project, we have expanded feedback collection from the users. Previously, we had only been interviewing several people; now we moved on to surveying more people via [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdmqDHt9qyoFA3cVwxmDlTUeurGfMd53Cgub4Iq92cTTjC_XQ/viewform).

In the form, we focused on gathering opinions on job suggestions, information about technical issues and design enhancements.

## Gathered Feedback

We have gathered broad feedback, from bug reports to test result opinions to aesthetic suggestions. In summary, these are the important takes:

- Several major issues were found:
    - Questions 7 & 8 are duplicates;
    - There is no visual feedback for the user when they submit their form;
    - The service is poorly adapted for mobile browsing;
    - Sometimes the service returns some gibberish instead of job titles.
- Most people find the career path suggestions useful and/or insightful
- Minor issues that we marked as important:
    - Choice (radio) buttons should be bigger;
    - The service loads slowly when opened first time
    - Impossible to go back without answering the current question

## Implemented changes

Our team prioritized technical issues from the feedback, then we took into consideration design enhancements.

The following was implemented and changed:


- Adapted service for mobile browsing  
  ![Mobile main page](/AICareerGuide/main_mobile.png)
  ![Mobile question page](/AICareerGuide/question_mobile.png)
  ![Mobile result page](/AICareerGuide/results_mobile.png)
- Added loading animation for form submition  
  ![Loading](/AICareerGuide/animation.png)
- Fixed duplicate questions
- Fixed going back without answering the current question
- Added favicon


The updated version of the service is coming to production soon.

{{< hint danger >}}

I am pleased to see that project is rapidly taking shape! Also, great to see that you are making progress with the mobile. 
You guys have accomplished a lot! Thank you for the hard work and dedication.
5/5 for the week, and see you soon! Cheers, Rustam
{{< /hint >}}