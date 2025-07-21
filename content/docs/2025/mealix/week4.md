# Practicum Project Summer 2025 Report 4  
**Team mealix**  

---

## 1. Testing and QA  

To ensure the quality of the code, a comprehensive testing strategy was implemented, including:  
- **Unit tests** (covering individual modules and classes) using mock objects to isolate the code under test  
- **Integration tests** (checking the interaction of components) using test containers to raise dependencies  

The test infrastructure includes:  
- Docker test containers for deploying real services (databases, message brokers)  
- Mock frameworks for emulating external dependencies  
- Automated pipelines in CI for performing tests at each commit  

### Evidence of test execution  
Screenshots of tests: [link](https://drive.google.com/drive/folders/1bLe45qyquxreOjGaAtORP1FpTKihp6HY?usp=drive_link)


### CI/CD  
We have set up an automatic deployment via GitHub Actions. When pushing to the deploy branch, the script:  
1. Connects to the server via SSH  
2. Updates the code from the repository (does a git pull)  
3. Restarts containers via docker compose  

Encrypted SSH keys from GitHub Secrets are used for security.  
The process is fully automated - after the code is merged into the deploy branch, the application itself is updated on the server without manual intervention. The entire cycle takes several minutes.  

Configuration file: [.github/workflows/deploy.yml](https://github.com/IU-Capstone-Project-2025/mealix/blob/main/.github/workflows/deploy.yml)  

### Deployment  
At the moment, the staging environment has not yet been deployed - the server will be ready next week. As soon as it appears, we will:  
- Set up automatic deployment via GitHub Actions using the same principle as the main CI/CD pipeline  
- Use the deploy-staging branch for staging deployments  
- Create an isolated environment with a test database  
- Configure logging for debugging  
- Add automatic health checks after deployment  

Staging will be used to test new features before putting them into production.  

### Vibe Check  
The team is working smoothly, all the tasks for the week are completed on time. We discussed:  
- Current progress (CI/CD is configured, tests are written, code is stable)  
- The delay with staging server (not critical)  
- Ideas for improving the process (recorded in backlog)  

Team atmosphere is productive with good motivation. Any difficulties will be resolved promptly at daily stand-ups.  

---

## 2. Weekly commitments  

### Individual contributions  

**Alexander Kachmazov (ML):**  
- Wrote script to generate JSON file from AI data  
- Researched articles on menu generation with budget/energy constraints  
  - [Article 1](https://arxiv.org/abs/2502.20601v2)  
  - [Article 2](https://arxiv.org/abs/2501.04143)  
- [Code link](https://github.com/IU-Capstone-Project-2025/mealix/blob/llm_agent_code/ml/generate_menu_into_json.py)  

**Samat Iakupov (Frontend):**  
- Implemented work with pictures, find the image url by ingridient id in csv table.
- Styled interface
- Tried to deploy frontend on GitHub Pages, but no luck due to GitHub Pages doesnt support SPA (single page app).
- Explore platform for deploy of SPA "Vercel" and deploy our project frontend. Deploy domain: [mealix.vercel.app](https://mealix.vercel.app), but there is no connection with backend yet.
- [working branch](https://github.com/IU-Capstone-Project-2025/mealix/tree/frontend/frontend)  

**Dmitrii Antipov (Backend):**  
- Tested all services  
- Set up CI/CD  
- Wrote unit and integration tests  
- Next steps: Javadoc and business metrics  
- [pom.xml](https://github.com/IU-Capstone-Project-2025/mealix/blob/main/backend/pom.xml)  

**Danil Eramasov (ML):**  
- Improved product matching using vector representations and cosine similarity  
- [Code link](https://github.com/IU-Capstone-Project-2025/mealix/blob/llm_agent_code/ml/find_products_vectors.py)  

**Albert Shammasov (Data Analyst):**  
- Parsed ~1,900 recipes  
- Added URL parsing for product images  
- Created backups in CSV/JSON formats  
- [Commit link](https://github.com/IU-Capstone-Project-2025/mealix/commit/f777332cd6fdb8e807c018a3a46e433075c85c3e)  

---

## 3. Confirmation of the code's operability  

We confirm that the code in the main branch:  
- Is in working condition  
- Can be run via docker-compose (or alternative method described in README.md)  