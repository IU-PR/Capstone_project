## Implemented MVP features

- After further research, tools for real-time static analysis in JupyterHub environments have been updated and reconfigured
	- Previously used tools: ruff, pycodestyle, pyflakes
	- Currently used tools: ruff, Vulture, MyPy, Bandit
	- [Increment card](https://strategic-control.kaiten.ru/space/606257/boards/card/51182219) (includes user story, acceptance criteria, validation checklists, members responsible for delivery, execution timeline, etc.)
	- Corresponding PR / commit / merge / branch
- After further research, tools for deep static analysis in JupyterHub environments have been updated and reconfigured
	- Previously used tools: MyPy, pylint, dodgy, vulture, pydocstyle
	- Currently used tools: pylint, dslinter, MLScent (partial due to non-standardised output format)
	- [Increment card](https://strategic-control.kaiten.ru/space/606257/boards/card/51182344) (includes user story, acceptance criteria, validation checklists, members responsible for delivery, execution timeline, etc.)
	- Corresponding PR / commit / merge / branch
- Basic LLM feedback functionality was implemented during the first week
	- Provides feedback for the current code on request, basic at the moment
	- [Increment card](https://strategic-control.kaiten.ru/space/606257/boards/card/51182158) (includes user story, acceptance criteria, validation checklists, members responsible for delivery, execution timeline, etc.)
	- [Corresponding PR](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/1)
- Buttons for deep static analysis and LLM feedback on request
	- Replacement for magic commands introduced earlier
	- [Increment card](https://strategic-control.kaiten.ru/space/606257/boards/card/51359353) (includes user story, acceptance criteria, validation checklists, members responsible for delivery, execution timeline, etc.)
	- Corresponding PR
- Interactive LLM chat for the user with code selection capabilities
	- Suitable for asking general questions and question
	- [Increment card](https://strategic-control.kaiten.ru/space/606257/boards/card/51481962) (includes user story, acceptance criteria, validation checklists, members responsible for delivery, execution timeline, etc.)
	- [Corresponding PR](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/18)
- Security specifications in the current architecture have been updated after discovering an intersection between Conjur Open Source and HashiCorp Vault capabilities, as well as extra requirements for Keycloak deployment. See updated system design [here](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111).

> User journey and accompanying processes are described via [Process-Experience map](https://strategic-control.kaiten.ru/documents/d/3c16a965-34eb-40e9-ba0c-cc0d92e16c03)

## Demonstration of the working MVP

- Please see all demonstration materials [here](https://disk.yandex.ru/d/pH7TS9Ndu38nXg)

## ML

Currently we are using [Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) with constrained generation for feedback and custom langchain client for chat support.

## Internal demo

Our team conducts an internal demo several times every week following this procedure:
1. Whenever an increment is finalized by the developers, it is moved into "Deploying to Dev" stage of the [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards)
2. Then `dev` deployment is prepared by developers and validated by the team member responsible for the current increment
   ![image](https://github.com/user-attachments/assets/d7ec6479-774e-45f8-bd87-a9811542e284)
3. Afterwards, the increment is moved to "Deploying to Beta" stage of the [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards), where completion of another checklist is required. Two of its stages include requesting approval for further deployment, which is given after the internal demo if all the acceptance criteria and quality attributes are met as defined
    ![image](https://i.ibb.co/zTQwgMcH/Pasted-image-20250625202455.png)
4. After receiving approval from the team lead for beta deployment and updating `uat` deployment, the increment is considered done

> Internal demo mostly consists of validating the current `beta` deployment against the acceptance criteria and quality attributes of the increment.

#### Notable observations for this week's increments

- **Loading animation** for buttons is absent despite it being an acceptance criterion
	- Reason: technical difficulties
	- Decision: partially decline the increment and set it to "Reopened" status to finalize in the next sprint
- **Icons for buttons** do not match the ones specified in acceptance criteria
	- Reason: technical difficulties
	- Decision: partially decline the increment and set it to "Reopened" status to finalize in the next sprint
- Deep static analysis is triggered not only by the corresponding button, but also **by saving the file**
	- Reason: specifics of LSP server interaction with JupyterLab
	- Decision: accept the corresponding increment for now, since this issue will automatically disappear when JupyterLab UI will be replaced with a custom UI
- Interactive LLM chat requires **manual code selection** for context awareness, which is contradictory to one of the acceptance criteria
	- Reason: technical issues
	- Decision: decompose the current increment into "basic" chat, which is accepted, and "context-aware chat" which is rescheduled to the next sprint


# Weekly commitments

## Individual contribution of each participant

### Dmitriy Prokopyev

- Added new increments, existing ones advanced and validated, see [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) for details
- Advanced target [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111) security specifications compared to previous week
- Conducted Sprint Planning and other meetings required to orchestrate project development
- Decomposed the main hypothesis in [Hypotheses Map](https://strategic-control.kaiten.ru/documents/d/25edfaac-364b-49e3-8ce0-64a1d926eb4a), extrapolated it according to accumulated insights
- Fully remade [Process-Experience Map](https://strategic-control.kaiten.ru/documents/d/3c16a965-34eb-40e9-ba0c-cc0d92e16c03) based on new insights and feedback from methodology experts
- Established a new increment approval process to ensure that Definition of Done for each increment is always met exactly as defined

### Egor Torshin

- Implemented and deployed the syntactic feedback button
	- Integrated deep static analysis tools into the syntactic feedback microservice: dslint, mlscent, pylint
	- See [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/18/commits/a2e00ff8f026a134f1d93c1d215e19aade643b9c)
- Architecturally modified the system to enable semantic feedback triggering from within JupyterLab
- Rewritten README instructions to correctly match new deployment and usage specifics
	- See [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/18/commits/15c761fb523a583f86f244b4389f8a227f3d9d0f)
- Coordinated backend development, held responsibility for all backend increments

### Aziz Vundirov

- Implemented LSP caching to enable simultaneous provision of real-time and deep static analysis
	- See [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/13525792cd7b6778254abf846c66828495ef08cd)
- Updated the deployment of syntactic analysis microservice
	- See [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/8e23a45ed60f13930dc7c1309509857ad9fadd4a)
- Integrated Vulture and Bandit as plugins for pylsp
	- See [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/e493cf2ffb799544b6d86f0aad871d3c54e6e7c5)
- Debugged tons of intermediate technical issues

### Nikita Tiurkov

- Implemented advisor microservice which serves as a custom chat provider
- Implemented chat history storage via PostgreSQL
- Implemented chat history caching and retrieval via Redis

> See latest commits [here](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commits/dev/?author=KosmonikOS)

### Oleg Shchendrigin

- Implemented custom langchain client to communicate with advisor microservice
- Integrated the custom langchain client into JupyterAI extension to enable native-like chat
- Setup and debugged the deployment of advisor microservice and associated langchain client

> See latest commits [here](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commits/dev/?author=Quartz-Admirer)

### Marsel Fayzullin

- Contributed significantly to debugging intermediate deployment issues
- Implemented auto-healing to ensure that LLM service is permanently up and running

> See latest commits [here](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commits/dev/?author=saddogsec)

### Dmitriy Yashin

- Researched separation of security requirements into incremental changes that improve yet do not break the system
	- See file [here](https://strategic-control.kaiten.ru/documents/d/e5d1e2ec-e3a8-458e-8e7b-30638f44a63c)
- Defined implementation steps for new security increments, see them in [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards)
- Contributed to updating the security contour of current system design, see [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111)


## Progress Comparison to Previous Week Plans

- [x] Account for all the new insights by updating the Hypothesis Map
- [x] Account for strategy adjustments by updating the Process-Experience Map
- [ ] Finalize Story Implementation Map
- [x] Finalize target System Design
- [ ] Finalize Functional Requirements and Non-Functional Requirements documents
- [x] Migrate deep LLM-generated feedback and statis analysis feedback to corresponding buttons near each cell of the .ipynb notebook
- [x] Implement LLM-powered context aware chat for user clarifications on feedback (partial)
- [ ] Integrate multiple sessions support for every other implemented feature
- [ ] Integrate customized environments support (pre-installed packages, included datasets and template files for cases)

## Plan for Next Week

- [ ] Finalize Story Implementation Map
- [ ] Finalize Functional Requirements and Non-Functional Requirements documents
- [ ] Finalize the increments that have been declined or partially accepted
- [ ] Integrate multiple sessions support for every other implemented feature
- [ ] Integrate customized environments support (pre-installed packages, included datasets and template files for cases)
- [ ] Transfer localized semantic feedback into dynamically appearing code comments
- [ ] Setup CI/CD pipeline to enforce quality standards
- [ ] Implement integration tests and end-to-end tests for endpoints

> Separation into staging and production environments is already implemented

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x]  In working condition.
- [x]  Run via docker-compose as described in `README.md`
