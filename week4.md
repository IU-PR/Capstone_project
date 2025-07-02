# **Week #4** 

## Testing and QA

*Server-side logic now has 7 unit tests covering core request/response handlers and edge-case packet validation. Tests run automatically in the CI workflow on every push and PR to **dev**; the job fails the build if any test breaks. Average code coverage is moderate (exact % not yet exported).*

### Evidence of test execution

![Api image 1](https://github.com/r3based/capstone_images/blob/main/server.jpg?raw=true)

![Api image 1](https://github.com/r3based/capstone_images/blob/main/CICD.png?raw=true)

## CI/CD

*GitHub Actions workflows build, test and publish Docker images to GHCR.*

* **prod-server-deploy.yml** and **stage-server-deploy.yml** run on **main** and **dev** respectively.  
* Secrets are stored in GitHub Secrets; no credentials are committed.  
* Pipeline steps: run tests ➜ build image ➜ push to GHCR ➜ pull & restart container on target server.  
* Stage (port 8050) and Prod (port 9050) deploy jobs are isolated.  
* Hardening, container health-checks, and secret management implemented in commit `f0a1945e…`.  

### Links to CI/CD configuration files

* <https://github.com/IU-Capstone-Project-2025/DeathRoom/blob/main/.github/workflows/prod-server-deply.yml>  
* <https://github.com/IU-Capstone-Project-2025/DeathRoom/blob/main/.github/workflows/stage-server-deploy.yml>

## Deployment

### Staging

*Automatically built from **dev** and deployed via Docker Compose to 77.233.222.200:8050.*

### Production

*Built from **main** and deployed via Docker Compose to 77.233.222.200:9050 on a hardened VPS.*

## Vibe Check

*Team morale is high. No blockers were reported, collaboration is smooth, and everyone feels heard.*

# Weekly commitments

## Individual contribution of each participant

*All participants: attended calls, decision discussions, retrospectives, and performed code reviews.*

- **Slava Molchanov** — Implemented server-side booking handling  
  <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/593ab12db963c26c9698074edb3cbb4f318f1362>  
  Fixed client–server communication  
  <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/d840f5bb31ec0d8adc3ca83f6ec427472b0169ec>

- **Rodion Krainov** — Authored this report.

- **Ilyas Khatipov** — Implemented jump-pad mechanics  
  <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/b4f5c7a930d9c9c774215a5bceae3024fac74024>

- **Igor Kuzmenkov** — Re-wrote and optimised workflows, Docker & compose; provisioned and hardened new server; configured secrets; set up image publishing; separated stage/prod; fixed server tests  
  <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/f0a1945edd62696cb435651a27d65d59987cbfec>  
  Container registry: <https://github.com/IU-Capstone-Project-2025/DeathRoom/pkgs/container/deathroom%2Fserver>

- **Vsevolod Nazmudinov** — Linked backend to client, fixed libraries and package issues  
  <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/ce67a473bb344529652175d64514321c38c7f605>  
  <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/17bddfabe955d99bfa8006708894d7a6af31cbd5>  
  <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/d8589d0a885bb519e386456caa7339d6dfaead30>

- **Almas Bagishaev** — Improved game menu; created weapon-spawner object  
  <https://github.com/IU-Capstone-Project-2025/DeathRoom/commit/1d072710dcc3bb96671000367983513f7141cc16>

- **Gleb Lobov** — Updated design document sections on weapons and power-ups  
  <https://docs.google.com/document/d/1kdaqDS6iQa7g32GWyoYNd155X4573cyyWMIlz3Tq7Ys/edit?tab=t.0>

## Plan for Next Week

*Feedback, Iteration & Polishing — gather user feedback, iterate on the MVP, and improve overall project quality.*

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the README.md).
