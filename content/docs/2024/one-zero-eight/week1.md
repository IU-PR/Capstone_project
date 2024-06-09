---
title: "Week #1"
---

# Week #1 report

## Team Formation and Project Proposal

### Team Members

| Team Member          | Telegram ID                                    | Email Address                       |
|----------------------|------------------------------------------------|-------------------------------------|
| Ruslan Belkov (Lead) | [@dantetemplar](https://t.me/dantetemplar)     | r.belkov@innopolis.university       |
| Artem Bulgakov       | [@ArtemSBulgakov](https://t.me/ArtemSBulgakov) | art.bulgakov@innopolis.university   |
| Anatoly Soldatov     | [@podyapolskiyaa](https://t.me/podyapolskiyaa) | a.soldatov@innopolis.university     |
| Alyona Artemeva      | [@Art_libra](https://t.me/Art_libra)           | a.artemeva@innopolis.university     |
| Eldar Mametov        | [@eldarlek](https://t.me/eldarlek)             | e.mametov@innopolis.university      |
| Nikita Sannikov      | [@raydenoir](https://t.me/raydenoir)           | n.sannikov@innopolis.university     |
| Amir Gubaidullin     | [@mng_cry](https://t.me/mng_cry)               | am.gubaidullin@innopolis.university |

### Value Proposition

- **Identify the Problem:**
  University students often face significant difficulties in finding the necessary information. Disparate information
  sources, complex search systems, and the lack of a centralized access point make the process of information retrieval
  lengthy, labor-intensive, and frustrating. Frequently, students abandon their search without finding the needed
  information.
- **Solution Description:**
  A centralized portal providing students and university staff with access to a wide range of information in one
  convenient location. This solution addresses data fragmentation, simplifies information search, and enhances learning
  efficiency.

  For Innopolis University, the following information sources may be consolidated:

  **University:**

    - Lecture materials
    - University documents
    - Eduwiki
    - Campus life
    - University events (Opportunities channel)
    - Dormitory documents
    - Professors and courses
    - Room booking information (Outlook)
    - Sports sections (descriptions, channels, events)

  **City:**

    - List of residents
    - City organizations
- **Benefits to Users:**
    - Access to the necessary information when needed.
    - Quick and efficient information retrieval.
    - A user-friendly interface providing information in one place.
- **Differentiation:**
  Our competitors include Moodle and Eduwiki (as information sources) and search engines like Yandex.

  Advantage: Fine-tuning the solution for Innopolis University (or other organizations).

- **User Impact:**
  Increased productivity and learning efficiency through easy access to required information.
- **User Testimonials or Use Cases:**
    - **Academic Support:** Student Ivan uses the platform to quickly find lecture materials and prepare for exams,
      significantly saving time.
    - **Event Organization:** Student Anna easily finds information about upcoming seminars and workshops, aiding her
      participation in additional educational activities.
    - **Dormitory Life:** Student Maxim accesses all necessary documents and instructions for dormitory living through
      the platform, eliminating the need for administrative visits.
    - **Sports Sections:** Student Olga finds training schedules and events for sports sections, helping her balance
      studies and physical activity.
    - **City Information:** International student John uses the platform to find information about city institutions and
      services, aiding his adaptation to the new environment.
    - **Room Booking:** Student Artem uses the platform to book rooms for study sessions and project meetings,
      simplifying the organization of academic activities.

## Lean Questionnaire

1. **What problem or need does your software project address?**
   The need for a unified resource for searching information related to life and activities in the city of Innopolis.
   Students and university staff face challenges in effectively finding information within the university, including:
    - Lecture materials
    - University documents
    - Campus events
    - Living information
    - Sports events
    - City resources
    - Information about professors and courses
    - Room booking information
2. **Who are your target users or customers?**
    - **Primary Customers:** Innopolis University or other organizations.
    - **Primary Users:** Students of Innopolis University (or employees of organizations).
    - **Secondary Users:** Professors, administrative staff, and technical writers.
3. **How will you validate and test your assumptions about the project?**
    - **User Interviews:** Conduct interviews with students, professors, and administration to understand their specific
      needs and problems.
    - **Surveys:** Distribute surveys to collect quantitative data on information access and usage patterns.
4. **What metrics will you use to measure the success of your project?Engagement Metrics:**
    - Number of active users
    - Frequency of platform usage
    - Time spent on the platform
    - Average session duration
    - Number of completed searches
    - User feedback on the platform

   **Performance Metrics:**

    - Accuracy and efficiency of search results
    - Performance of AI models
5. **How do you plan to iterate and pivot if necessary based on user feedback?**
    - **User Feedback Loop:** Implement a user feedback system with a feedback form on the site, as well as like and
      dislike buttons to rate the AI responses.

## Leveraging AI, Open-Source, and Experts

- **AI:**
    - Implement AI models at the core of our search and response generation systems.
    - Use ChatGPT and Gemini for ideation and report generation.
    - Employ AI tools like Copilot for efficient coding practices.
- **Open Source:**
    - Utilize permissively licensed open-source libraries to enhance our development process.
    - Research and integrate publicly available solutions to inspire and improve our project.
- **Experts:**
    - Engage with domain experts such as Alexey Potemkin and Albert Nasybullin to guide our project's development and
      ensure alignment with industry standards and best practices.

By thoroughly defining the vision for our project and leveraging modern technologies and expert guidance, we aim to
create a robust, user-friendly platform that significantly enhances the information retrieval experience for the
Innopolis community.

## Overview

The primary objective of our project, InNoHassle, is to develop a centralized portal that aggregates various services
within the Innopolis ecosystem, providing a seamless user experience for students and staff. The key motivation behind
this project is to address the frequent challenges students face in finding relevant information efficiently. Our
solution aims to streamline access to diverse resources such as lecture materials, university documents, event
schedules, and more, by integrating them into a single, user-friendly interface.

The main functionalities of our project include:

- **Search Portal:** A dedicated webpage featuring an intuitive search form that allows users to query various
  information systems, such as Moodle, for relevant academic materials and resources.
    - A clean and intuitive user interface for the search form.
    - Users can input queries to search across various integrated systems such as Moodle.
    - The search results will include a brief overview of the topic, relevant information snippets, and corresponding
      references.
- **Response Generation:** Using a Retrieval-Augmented Generation (RAG)-based approach to provide concise summaries and
  references for the searched topics.
    - Utilize a RAG-based approach to generate comprehensive and relevant responses.
    - The system will fetch information from indexed data sources and provide summaries enhanced by AI models.
- **Feedback Mechanism:** Implementing features for users to provide feedback on the relevance and accuracy of the
  search results through likes and dislikes.
    - Incorporate like and dislike buttons for users to rate the relevance and accuracy of the provided search results.
    - Collect user feedback to continuously improve the AI models and search algorithms.
- **Enhanced Parsers:** Improving existing parsers to efficiently gather and index information from multiple sources.
    - Develop and refine parsers to aggregate data from various sources efficiently.
    - Ensure that all collected data is properly indexed with appropriate tags, categories, and metadata.
- **Data Integration:** Negotiating access to essential data sources such as Moodle, and systematically indexing data
  entities with tags, categories, sources, and relationships.
    - Collaborate with key stakeholders, including Alexey Potemkin, to negotiate access to crucial data sources like
      Moodle.
    - Implement a robust indexing system to organize and relate data entities, facilitating efficient search operations.

**Search Pipeline Diagram:**

![https://myscale.com/blog/assets/img/rag-step3.da1abea3.png](https://myscale.com/blog/assets/img/rag-step3.da1abea3.png)

![https://myscale.com/blog/assets/img/rag-step2.ae451d6f.png](https://myscale.com/blog/assets/img/rag-step2.ae451d6f.png)

**Existing Architecture of InNoHassle Events service:**

![Untitled](/2024/one-zero-eight/f9128990-bc98-4863-98cb-f170aa0022bb.png)

![Untitled](/2024/one-zero-eight/a24e4efc-4318-45d1-9762-349b207f9e5c.png)

## Tech Stack

To ensure scalability, performance, and ease of development, we have carefully selected the following technologies,
frameworks, and programming languages for our project:

**Backend:**

- **Python:** For its simplicity and extensive libraries for data processing and machine learning.
- **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard
  Python type hints.
- **Langchain, Ollama:** To implement the Retrieval-Augmented Generation (RAG) pipeline for generating search results.
- **MongoDB:** As our database solutions to efficiently store and manage data from various data sources (schema-less)
- **Qdrant:** Vector database to store embedded information for content-meaningful search.

**Frontend:**

- **TypeScript:** A strongly typed programming language that builds on JavaScript, providing better tooling at any
  scale.
- **React, Next.js:** For building dynamic and high-performance user interfaces and server-side rendering capabilities.
- **TailwindCSS:** A utility-first CSS framework for rapid UI development with consistent and responsive design.
