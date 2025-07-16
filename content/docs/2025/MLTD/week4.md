# Week #4

## Testing and QA
The tests created for the frontend and backend involve checking for any missing folders, liniting the code, and running the code in development mode to see if it runs after a successful build.
However, we plan on making more tests for the CI pipelines such as API endpoint testing to make sure that the endpoints are working properly.

### Test Execution
[Python CI Pipeline Results](https://github.com/IU-Capstone-Project-2025/MLTD/actions/runs/16017212438)
[Node.js CI Pipeline Results](https://github.com/IU-Capstone-Project-2025/MLTD/actions/runs/16017212442)

## CI/CD
### Decription:
The CI pipelines were set up using GitHub Actions that will check the codebase for any problems for every new commit or pull request made to the repository.
This allows us to find any hidden problems that could have gone unseen during development and ensure that we have working code.

### Tool(s) used:
- GitHub Actions
- Bash scripting

### Challenges faced:
While setting up the pipelines I (Paramon) had troubles setting up the pipelines because I do not have much experience setting up CI/CD pipelines.
Another challenge I (Paramon) faced was deciding on what tests to write, as I also do not write tests that often.
However, I overcame both of those challeneges by looking at old group projects with CI/CD pipelines configured, searching online for documenation and examples.

### CI pipeline configurations:
  - [Python CI Pipeline](https://github.com/IU-Capstone-Project-2025/MLTD/blob/main/.github/workflows/python-ci.yml)
  - [Nodejs CI Pipeline](https://github.com/IU-Capstone-Project-2025/MLTD/blob/main/.github/workflows/node.js.yml)

### Deployment
#### Staging
For staging, we either run the project locally on our machines with node.js, python, and the project dependencies installed locally on our machines.
However, Paramon can run the project using docker compose on his linux server because he has issues using Docker on windows. Plus, by running the project on different platforms we can potentialy find issues on any platform and fix them.

## Vibe Check

### Team Health check
- Paramon: "I am doing ok, but it is kind of hard to get some things done on time each week since we only have two people in our team. Overall, the project is not as hard as I initally thought it would be and I am impressed how far we have gone in the first four weeks."
- Bulat: "I feel tired since I had other projects and we only have two people in our MLTD team. Not everything can be completed on time, but I think it will be easier starting next week, since some courses will already be over."

### Progress:
So far from three weeks of work we have a:
- Backend API that can recieve log files from users, which is sent to the machine learning model for threat detection, and it will give users the probability of a threat.
- Machine learning model that can detect threats and can be trained on preprocessed data.
- Frontend that users can use to find threats in their system or network infratructure as an alternative to using scripts to upload the log files directly to the API.

Overall we are impressed and satisfied with the progress we made in the first four weeks of development despite only having two people on our team.

### Challenges we faced:
1. The main challenge we faced is having only two people in our team, because we each have more work to do due to how small the team is.
2. As previously mentioned above, another challenege we faced was distributing project roles since it is only the two of us and neither of us are good at frontend development.

## Weekly commitments

Paramon:
- [Revamped the frontend UI](https://github.com/IU-Capstone-Project-2025/MLTD/commit/86ca789cb8076a4a1d91826a634d56db52e3e613) using shad-cn, which our TA suggested in a previous meeting.
- Created [tests](https://github.com/IU-Capstone-Project-2025/MLTD/commit/a5571c70dea95cf55aa594e0e1539dee58b082e6) for the frontend and backend.
- Created CI pipelines (see section CI/CD) for the frontend and backend.

Bulat:
- Created [parser for BGL log files](https://github.com/IU-Capstone-Project-2025/MLTD/commit/eb1c83527dd6acde6181298c0b95713614477282)
- Preprocessed data and trained the Bert model
## Plans for next week

## Confirmation of code operability
We confirm that the code in the main branch:
- Is in working condition.
- Can run via docker compose and other alternatives mentioned in README.md.
  
