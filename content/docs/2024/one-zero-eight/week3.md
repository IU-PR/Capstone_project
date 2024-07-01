---
title: "Week #3"
---

# Week 3 - Developing the first prototype, creating the priority list

- **Technical Infrastructure**:

  We use GitHub Actions for CI pipelines such as formatting, linting, testing (if there are any tests). Before each
  commit the pre-commit hooks reformat changed files locally using tools such as ruff (for Python), prettier or eslint (
  for JavaScript). After pushing to the repository, automatic workflows check the whole repository to ensure that the
  changes can be integrated without any problems, ensuring code quality.

  Our team already has 3 servers for production and staging environments. During the week we set up a deployment of a
  new backend service to staging server. After each push to main branch, new Docker image will be built, pushed to
  staging, and reloaded. Now frontend team can use that deployment for integrating calls to API into frontend code.
  Also, frontend has such deployment pipeline too. We can test the whole service on staging URL now.

  Members of our team got unlimited access to 2 servers with Tesla V100 GPU. We will use them for experiments,
  benchmarking, inference of ML approaches and models. For production use we will create a daemon which receives tasks
  from our API, processes them, and pushes results back. Some such tasks include: recognising of image contents in PDF,
  generating summary of lectures, generating relevant response for user query using LLM.

- **Backend Development**:
    - **Database Migration:** Migrated from PostgreSQL to MongoDB, optimizing the database for current requirements.
    - **Student Authentication System:** Integrated a robust authentication system (InNoHassle-Accounts) to enhance
      security and manage user access.
    - **Endpoint Development:** Created essential endpoints and methods to facilitate interactions with other parts of
      the service.
    - **Data Integration:** Connected the backend to store data obtained from Moodle and Telegram chats, ensuring
      centralized data management.
    - **Metadata Search Implementation:** Implemented module metadata search through MongoDB indexing, leveraging
      frequency analysis, language syntax understanding, lemmatization, stemming, and stop words for accurate search
      results. Each result includes an anchor URL and a preview URL for temporary access.
    - **Continuous Deployment:** Set up automated deployments to the staging environment, allowing real-time testing and
      integration by the frontend team.
- **Frontend Development**:

  Our team has made significant progress on the frontend development. Here are the key achievements so far:

    - **Search Page Creation**: We have created the search page on the Innohassle platform, providing users with an
      intuitive interface to perform searches.
    - **Data Structure and Hooks**: We have defined the structure of the data stored on the backend and written hooks to
      facilitate server requests for fetching user query results.
    - **PDF Preview Display**: We have added an attractive display for PDF file previews attached to search results,
      enhancing the user experience.
    - **Source Switching**: Each search result can have multiple sources. We have implemented a feature to switch
      between these sources (their previews). If a preview is unavailable, a message indicating its unavailability is
      displayed.
    - **UI Improvements**: The website's interface has been made more pleasant and optimized, ensuring a better user
      experience and performance.

  These advancements in frontend development ensure that our platform is not only functional but also user-friendly and
  visually appealing.

- **Data Management**:
    - **MongoDB:** We managed to connect MongoDB database for storing metadata of available sources with corresponding
      models for moodle and telegram resources. The baseline indexes were set up on each resource type.
    - **MinIO:** The MinIO solution is used for storing large files of scrapped resources to be able to retrieve and
      provide resource for the user as quick as possible.
    - **FAISS:** We decided to use FAISS vector database for storing chunks of text embeddings rather than Qdrant
      because of higher efficiency and simplicity on our scale with potential possibility to grow up using gpu-leveraged
      approach.
- **Prototype Testing**:

  In our testing phase, we aimed to uncover any usability issues and bugs within the prototype. Specifically, we
  evaluated the effectiveness of the search interface we had developed. While no significant bugs were detected, our
  team members did offer valuable feedback on enhancing the overall user experience. A key focus of our attention was on
  optimizing website responsiveness, given that a majority of users are likely to access our product via their mobile
  phones.

  When designing a help tool for students, our team, being a part of the main target audience, prioritizes creating user
  scenarios that are intuitive and user-friendly. By considering the most convenient pathways for users, we strive to
  ensure that our product meets the needs and expectations of our audience effectively.

## **Weekly Progress Report**:

This week, we've accomplished a lot towards achieving our goals in implementing the prototype. The prototype is ready
and includes the following functionality:

**Integration with Moodle:**

Now it's possible to save data from Moodle, including courses, modules, and resources. This data is stored in MongoDB
for further use. If there are missing or updated files, the system identifies them so that the client can download the
necessary files, which are then stored in MinIO.

**Metadata Search and Indexing:**

Implemented module metadata search through MongoDB indexing. The search algorithm utilizes frequency analysis,
understanding of language syntax, lemmatization, stemming, and stop words to provide accurate results. The search
returns results with a relevance score. Each result includes:

- Anchor URL: Points to a specific Moodle module.
- Preview URL: Points to our API, which redirects to a temporary file URL valid for one day.

**Moodle Browser Extension:**

Developed an extension with auto-login functionality for Moodle and quick links to current courses, significantly
reducing navigation time within Moodle. The extension has been sent to Chrome Web Store and Mozilla Addons to make them
available through browser extension markets.

**Frontend Development:**

Created a search page that queries file metadata. Search results are sorted by relevance. Implemented previews for PDF
files and links to sources.

**Telegram Parser Bot:**

Developed a fully functional Telegram parser bot that collects data from Telegram channels and sends it to the server.

### **Challenges & Solutions**

It turned out that just a zip file is not suitable for delivering a browser extension, because... modern browsers will
limit it. The only solution here is to upload the extension to browser's extension store. To do this, we needed to
describe the purpose of the extension, what data it collects, attach screenshots and source code. Moreover, we had to
write a privacy policy for users. Mozilla Addons has already accepted our extension (the verification took three days),
but there are problems related to application permissions. We also filled out an form on Chrome Web Store, but there is
no response yet.

Minio storage requires a dedicated domain, so we filled out an application with the IT department to get it.

The servers with video cards had outdated packages, some of them were able to be updated, but the cuda libraries could
not be updated, so we had to limit the PyTorch version in our project.

### **Conclusions & Next Steps**

Finally, we were able to see and click on the results of our work. It's nice, we would like to keep the temp. We plan to
continue to have weekly synchronization meetings where we outline work for the next sprint.

We would like to rework the "Search" page to match the Google Search style, and move the existing template into a
separate "Ask" page because it suits LLM-generated answer more.

There are also plans to collect more data for our experiments in the field of AI, for this we will add a new remote (
Minio from backend part) to our DVC. We also need to speed up the PDF processing library, as it takes too much time.