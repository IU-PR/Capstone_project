## Detailed Requirements Elaboration

Please see detailed requirements (product backlog items) for the MVP in [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards).

> Note
> - [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) items in Sprint Queue or Ready To Implement stages have detailed Acceptance Criteria, since they have been prepared by team lead and QA engineer
> - [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) items in Backlog Queue are formulated, but do not have detailed Acceptance Criteria and Quality Attributes yet, since they have lower priority than others

### Prioritized backlog

Development methodology adopted by our team requires three distinct backlogs:
- [Requirements Engineering Backlog](https://strategic-control.kaiten.ru/space/606285/boards)
	- Transforms insights and ideas of team members into actionable increments (enriched user stories or intermediate action stories) using project strategy ([Hypotheses Map](https://strategic-control.kaiten.ru/documents/d/25edfaac-364b-49e3-8ce0-64a1d926eb4a)), enriched user flow ([Process-Experience Map](https://strategic-control.kaiten.ru/documents/d/3c16a965-34eb-40e9-ba0c-cc0d92e16c03)), implementation forms specification ([Story Implementation Map](https://strategic-control.kaiten.ru/documents/d/47197102-fb45-452e-94e6-ef2e0538ea75)), and target [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111)
- [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards)
	- Used for increments (small valuable additions to the product) flow, ensures full increment specification, automation of these specifications, and multi-stage deployment with intermediate validations reaching the end user
- [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards)
	- Used for technical tasks flow, ensuring testing and review of every task before committing it to any stable branch

## Project specific progress

### Product Management

- New increments added, existing ones advanced and validated, see [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) for details
- Target [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111) advanced significantly compared to previous week, security concerns handling included
- Specified and coordinated DevOps advancements, see [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards) for details
- Validated and approved[ increments transition](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/6) to production version
- Integrated security requirements into target [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111)

### Backend

> Realtime static analysis and deep static analysis on save using built-in LSP server and various static analysis tools with rendering native to JupyterLab are implemented

- See implemented backend tasks (they have "Backend" tag) in [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards)

### ML Engineering

> Separation of localized deep feedback as code warnings and non-localized feedback as markdown text is implemented

- See implemented ML tasks (they have "ML" tag) in [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards)

### DevOps Engineering

> A three-stage deployment system has been implemented and wrapped conveniently:
> - `dev` deployment for developers and intermediate testing
> - `beta` deployment for validating the value and match with acceptance criteria
> - `uat` deployment as a stable deployment for stakeholders
> Additionally, JupyterLab session credentials have been secured

- See implemented DevOps tasks (they have "DevOps" tag) in [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards)

### Security Engineering

- [Conjur Open Source integration research](https://strategic-control.kaiten.ru/documents/d/97661837-0255-46c6-b355-b48bfedf5ab4)
- [Keycloak integration research](https://strategic-control.kaiten.ru/documents/d/a0f1db88-f945-4337-a639-88c34340a5f1)
- Target [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111) updated with researched security tools

# Weekly commitments

## Individual contribution of each participant

### Dmitriy Prokopyev

- Added new increments, existing ones advanced and validated, see [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) for details
- Advanced target [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111) significantly compared to previous week, security concerns handling included
- Specified and coordinated DevOps advancements, see [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards) for details
- Validated and approved[ increments transition](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/6) to production version
- Integrated security requirements into target [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111)
- Conducted Sprint Planning and other meetings required to orchestrate project development

### Egor Torshin

- Prepared and completed various backend tasks, see [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards), user "Egor Torshin"
- Participated in system design, see [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111)
- Developed a [static analysis microservice](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/cf66374021163c24b7d58e8b1a28ef6c241f1127) (syntactic/deep)  
- Supervised [LSP deployment](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/5)  

### Aziz Vundirov

- Completed various backend tasks, see [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards), user "Aziz Vundirov"
- Reconfigured, implemented, and deployed the [LSP-service](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/524cfdf721d03ae6af0aa5b33e79c36963807fee) (+ deep analysis integration)  
- Configured and deployed [real-time validation](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/6) in JupyterLab
- Rewrote the [functionality of main LSP-server](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/compare/aziz_deploy_lsp) for supporting the real-time code-checking
- Connected the JupyterHub, LSP-server and Deep Static Analysis microservice

### Nikita Tiurkov

- Prepared and completed various ML tasks, see [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards), user "Nikita Tiurkov"
- Implemented warnings generation functionality, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/bbb416096778ac35b4ad5752f45e2a6f2fb17571)
- Implemented logging for semantic feedback microservice, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/5fe4bae2a029c3d2206c1ebdbb75f2c17aa50f4b)

### Oleg Shchendrigin

- Prepared and completed various ML tasks, see [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards), user "Oleg Shchendrigin"
- Prepared test cases for generated warnings, approved implementation, see [testing results document](https://strategic-control.kaiten.ru/documents/d/b7e4ff33-7e11-4b3b-b1cb-0cea32655983)

### Marsel Fayzullin

- Completed various DevOps tasks, see [Technical Backlog](https://strategic-control.kaiten.ru/space/606259/boards), user "Marsel Fayzullin"
- Added support for multiple working deployments at a time, see [corresponding commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/6f32e457c0b63dd7fae2c2ab240976e7b15c0d50)
- Moved credentials out of jupyterhub config, see [corresponding commit](Moved credentials out of jupyterhub config)

### Dmitriy Yashin

- [Conjur Open Source integration research](https://strategic-control.kaiten.ru/documents/d/97661837-0255-46c6-b355-b48bfedf5ab4)
- [Keycloak integration research](https://strategic-control.kaiten.ru/documents/d/a0f1db88-f945-4337-a639-88c34340a5f1)
- Target [Technical Architecture](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111) updated with researched security tools

## Plan for Next Week

- Account for all the new insights by updating the Hypothesis Map
- Account for strategy adjustments by updating the Process-Experience Map
- Finalize Story Implementation Map
- Finalize target System Design
- FInalize Functional Requiremets and Non-Functional Requirements documents
- Migrate deep LLM-generated feedback and statis analysis feedback to corresponding buttons near each cell of the .ipynb notebook
- Implement LLM-powered context aware chat for user clarifications on feedback
- Integrate multiple sessions support for every other implemented feature
- Integrate customized environments support (pre-installed packages, included datasets and template files for cases)

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x]  In working condition.
- [x]  Run via docker-compose (or another alternative described in the `README.md`).
