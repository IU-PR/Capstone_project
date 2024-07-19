---
title: "Week #2"
---

# Week 2 Report: Alumni Portal


In today's report, we will cover three main topics:
1. Team Allocation
2. The tech stack chosen by our team.
3. The architecture of our project.
4. An overview of our progress and the future work for week 3.

## Team Allocation & Distribution of Responsibilities

| Full Name             | Tg alias       | Uni mail                        | Role                |
|-----------------------|----------------|---------------------------------|---------------------|
| Chulpan Valiullina    | @Chehmet       | c.valiullina@innopolis.university | ML engineer         |
| Nazgul Salikhova      | @kokosinka123  | n.salikhova@innopolis.university | ML engineer         |
| Liubov Smirnova       | @mangocandle   | l.smirnova@innopolis.university  | Frontend & Backend  |
| Anzhelika Akhmetova   | @angelika782345| a.akhmetova@innopolis.university | Frontend & Backend  |
| Olesia Grediushko     | @WellNotWell   | o.grediushko@innopolis.university | Frontend & Backend  |
| Galia Shabanova       | @g7l7a         | g.shabanova@innopolis.university | Frontend & Backend  |
| Anastasiia Ozerova    | @oneozerova    | a.ozerova@innopolis.university   | Product Manager & Report Writer |

## Tech Stack Selection

> As we presented our idea in last week's report, we will now talk in more detail about the tech stack for our project.
>
> Firstly, let's start with the framework for our website. Since my.university uses Django, we have chosen the same framework to facilitate better collaboration in the future. Therefore, for the backend, we chose Django and the Python as a programming language.
>
> For the frontend part, we use CSS and HTML for basic structure and styling.
>
> Now let's discuss the exciting part: the integrated AI part which will assist with user navigation. For this, we will use the following tools:
> - *Python*
> - *llama3 8B*
> - *Ollama*
> - *LangChain*
> - *Milvus database*
>
> Additionally, to manage information from our alumni and students, we will use a relational database. SQLite is well-suited for our main purposes and will be used for this project.

## Architecture Design

Data Management: relational database built-in Django project is used

User Interface (UI) Design: is created using Figma

Scalability and Performance: …

Security and Privacy: …

Error Handling and Resilience: …

Deployment and DevOps: …

### Django Project Structure

![project_structure](/2024/Alumni/project_structure.png)

- **alumni:** Contains all project settings and includes the market root page.
- **static:** Stores static files used in HTML pages, such as CSS, images, and JavaScript files.
- **templates:** Contains HTML pages and templates for the entire site.
- **db.sqlite3:** The SQLite database file used to store all project data.
- **manage.py:** A command-line utility for managing the Django project, including launching the project.

### Architecture Component Breakdown:

We will provide you with a schematic drawing of our website to give you a visual overview of its whole architecture.

![system_design](/2024/Alumni/system_design.jpg)

Now, let's discuss in more detail the user flow for each page on our website:

#### Application for a Pass Page
![pass_page](/2024/Alumni/pass_page.png)

#### Authorization and Profile Page
![auth_page](/2024/Alumni/auth_page.png)

#### Application for Mentoring Page
![ment_page](/2024/Alumni/ment_page.png)

#### Alumni Merch Page

The users can browse a list of available products, each with an image, name, and brief description. Clicking on a product takes the user to the product page where they can see detailed information including the product name, description, price, available sizes, several photos, and a "Buy" button.

When the user clicks the "Buy" button, they are redirected to the purchase page where they must enter their full name and select the product size if applicable. The purchase page also displays a summary of the selected product. Upon confirming the purchase, the user proceeds with payment via Tinkoff (not implemented in the MVP) and a message is sent to the admin about the new order. The delivery option in the MVP is limited to self-pickup.

## Our Progress

We have divided our responsibilities among team members, with each person handling both the backend and frontend for their assigned page. For this week, we completed the frontend for the following pages:

### Alumni Merch Page
![merch_page](/2024/Alumni/merch_page1.png)

### Authorization Page
![auth_screen](/2024/Alumni/auth_screen.png)

### Application for Mentoring Page Progress
![ment1_screen](/2024/Alumni/ment1_screen.png)
![ment2_screen](/2024/Alumni/ment2_screen.png)

### Card request page
![request_page](/2024/Alumni/request_page.jpg)

### AI Chat
![ai_chat](/2024/Alumni/ai_chat.jpg)

## Future Work

In the coming weeks, we will create the Alumni Event page and the Donation page. Additionally, during the third week, we plan to complete the backend development for the existing pages.
