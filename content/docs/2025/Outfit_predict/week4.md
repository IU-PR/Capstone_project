# **Week №4 Report: Outfit Predict**

**Deployed product available at: [http://outfitpredict.ru/](http://outfitpredict.ru/)**

## **CI/CD** 

## *Description of CI/CD setup, tools used, and any challenges faced.*

Created CI using python libraries for linting and refactoring code. Used styling formatters as Black, isort, prettier to reformat code. Linters: Flake8. Type checker MyPy. Security for checking api key leaks: gitleaks. Repo hygiene check-yaml, for tab checking also reformat for readable type. Git workflow for checking and fixing commit names: commitizen.

### Links to CI/CD configuration files

[*Link to CI*](https://github.com/IU-Capstone-Project-2025/Outfit_predict/blob/main/.github/workflows/ci.yml)

[*Link to pre commit which is checked during CI*](https://github.com/IU-Capstone-Project-2025/Outfit_predict/blob/main/.pre-commit-config.yaml)

## **Deployment** 

### Staging

### *Details about the deployment process, environment setup for staging environment*

*Created .env file which controls docker compose variables like postgresql username and password. Deployed using git, ssh tool to connect into VDS. Create a developing guide to use the correct git workflow in our code database. [Link](https://github.com/IU-Capstone-Project-2025/Outfit_predict/blob/main/dev.md)*

*Also we added the authorization part in our backend code. [link](https://github.com/IU-Capstone-Project-2025/Outfit_predict/pull/9)*

### Production

*If you focus on bonus points, describe the production deployment process, environment setup for production environment, public domain name and VDS setup* *ATTENTION: You can put this section in ANY future report (weeks 4,5,6)*

*First we needed to buy a virtual dedicated server and then set it up. Installing tools, such as docker compose, engine. I turned off logging using password due security reasons. Because of that I (Remal) added logging using RSA keys because they are a lot better. Turn off root user . Added port forwarding like nginx. Also we bought a domain for our site [outfitpredict.ru](http://outfitpredict.ru). To add them and get access we modified cloudflare DNS server to make the domain working and address it to our server. Then I configured .env variables to secure access to our databases such as postgresql, minio.*

*Script to configure nginx for port forwarding [link](https://github.com/IU-Capstone-Project-2025/Outfit_predict/blob/main/devops/setup-nginx.sh).*

*Then I cloned our project to server, configured docker compose to take environment variables to create all docker containers which includes backend part, frontend, minio and postgresql.* 

*Also we configured DDoS protection using cloudflare which will proxy every attack on the other server within securing our server from high risk attacks.*

*Overall:*

*The server is up and already serving the site by this link. Take into attention that the site is served by this link [http://outfitpredict.ru](http://outfitpredict.ru) not https because there is some problem with certificates to make connection secure to use https protocol. In future I (Remal) will try to get one of the public and free certificates to make this.*

## **Testing and QA** 

Backend

*Unit tests cover all critical backend logic, including CRUD operations, models, and integrations with external services. Tests use mocking for async database sessions, machine learning models, and storage backends to ensure fast, isolated, and reliable results. Both normal and edge cases are tested.*

Frontend:

*Key UI components and business logic are unit tested using React Testing Library to ensure correct rendering and user interactions.*

Integration:

*API endpoints are tested to verify correct request/response handling and error management, ensuring smooth interaction between frontend and backend.*

### Evidence of test execution

[*Link on the screenshot with running tests*](https://drive.google.com/file/d/1wdgIjXBpT-snXCKDmMnfdcYaCPHxYXYh/view?usp=sharing)

[*Link on the screenshot with results of tests*](https://drive.google.com/file/d/1AftmSAlT-iLZqbKPd5l7o6PYi-wh-Sod/view?usp=sharing)

[*Link to the commit*](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/f5032ab65aa878522a7749cc0fbf213aa29f1619)

## **Vibe Check** 

Team health check: Our team is currently working on several projects, one of which is the Capstone Project. The team together worked on different hackathons and other projects. We are effectively communicating using different channels: regular offline meetings, Telegram groups, and etc. Each team member feels confident and heard. The process for maintaining this is described later.

Progress, roadblocks and team dynamics: We effectively distributed the roles across team members, according to their preferred position. We have passed through the MVP and implemented the main functionality of our application. Now we are working together on adding extra functions and improving user experience. Moreover, our team members progress in the topic they have chosen. For example, DevOps and Backend developers learn more about CI/CD and product deployment. ML developers explore new models and architectures: YOLO, DINO, CLIP, and many others.  Front-end developer explore new frameworks. Product Designer explores different ways of finding similar products, explores new frameworks, such as MoSCoW, SWOT analysis. Customer Developer gains experience in conducting effective interviews. Project Manager learns new ways of organizing teams, gains experience in directing the team to the right goal. 

How do we ensure everyone feels heard: We conduct regular meetings, in which each team member describes his ideas and work. Project Manager ensures that each team member gained attention to his work and was properly acknowledged. In case of conflicts, we utilize majority voting. In case of equal votes, we utilize [random.org](http://random.org) for the final choice.

# **Weekly commitments** 

## **Individual contribution of each participant** 

*Bulat Sharipov: Distributed tasks among team members. Conducted team meetings and  ensured everyone is feeling heard. Wrote this report*

*Danil Fathutdinov: Experimented with different ML solutions. Discovered new models and parameters. Found best search optimization*

*Dinar Yakupov: Iterated on frontend development. Refined designs and created new prototypes. Created frontend pages for authorization and tweaks to UI wardrobe.* 

*Remal Gareev: Main worker of this week: Created CI/CD, Integration tests, deployed the project, created migrations.*

*Victor Mazanov: Conducted Customer Development ([link](https://www.notion.so/CustDev-for-Week-4-21d5a218c5d5807da8a2d1e3306cf45c))*

*Artyom Grishin: Iterated on competitors application analysis ([link](https://www.notion.so/New-features-based-on-competitors-21ea795c445f80af83e3e19cb14f0feb?source=copy_link)), iterated on cust-dev to create new features([link](https://www.notion.so/Features-and-insights-from-cust-dev-analysis-224a795c445f80ee9a35eb8a0d601c40?source=copy_link)), designed new features, contributed to writing integration and unit tests([link](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/f5032ab65aa878522a7749cc0fbf213aa29f1619)).*

## **Plan for Next Week** 

- Developing possibility to choose only a subset of clothes from the wardrobe to make outfit predictions.  
- Possibility to filter outfit searches by gender (i.e. showing clothes for girls only).  
- Possibility to filter outfit based on styles (i.e. casual, official).  
- Possibility to filter outfit based on dominated color on the outfit (i.e. yellow outfits).  
- Possibility to download outfit images.  
- Iterating on new ideas and features for the application   
- Add folder distribution mechanism: creating custom folders and propagating with outfits. Build endpoints and frontend pages.  
- Possibility to download outfit images.  
- Customer development.

## **Confirmation of the code’s operability** 

We confirm that the code in the main branch:

*  In working condition.  
*  Run via docker-compose (or another alternative described in the `README.md`).

