# **<p style="text-align: center">BookHive</p>**

## **Week 1 report**

This week, our main task was to form a balanced all-around team and choose the general theme and outline of our project. Creating a team was not hard, as we mostly already knew each other and our strengths. Below is the list of our members and the roles they can fill out during project development:

| Team Member            | Telegram ID   | Email Address       | Stack |
|------------------------|---------------|---------------------|-------|
| Anastasia Martynova (Lead)          | @zefirush | <a.martynova@innopolis.university>     | Design/Frontend |
| Maxim Piniagin     |     @Ozurexus | <m.piniagin@innopolis.university> | Frontend/Product Manager |
|Yegor Sokolov | @yeawouu | <ye.sokolov@innopolis.university> | Backend |
|Marat Medvedev | @DuckBlur | <m.medvedev@innopolis.university> | Backend/ML |
|Lev Gorbunkov  | @levgo1337 | <l.gorbunkov@innopolis.university> | Frontend/Backend |
|Bulat Kutlugallyamov | @bulatok4 | <b.kutlugallyamov@innopolis.university> | Backend |
|Roman Voronov | porludom | <ro.voronov@innopolis.university> | Backend/ML |

As you can see, we have an assortment of stack variations, and we believe that this will be an advantage during development.

While choosing the project idea, basically everyone had suggestions: we thought about making a site for prediction of currency exchange rate, considered making site+telegram bot for prediction of prices on online shops such as WildBerries. At some point, we even considered making a site for automatic note creation from the user uploaded mp3 file.
In the end, we settled on something that in our opinion has a higher chance of being a useful project: a book recommendation site (web/ML project). After finishing a book they really liked, many people have problems finding a similar one, and we aim to aid in that. Here is the brief rundown of the main features of this project:
The user enters a book they finished reading and whether they liked it or not. Based on that, our site proposes books that the user has not read and that might be interesting for them using Machine Learning Algorithm.
Each book will contain genre, abstract, and links to its page in several online bookshops: both in digital and on paper.
Moreover, we plan to have some open source books be available for download directly from our site. Also hope that if this project will work out to get rights to sell books there.
More features may be added further down the line, when it will be easier to assess how much time we have after implementing the main ones, among those we consider implementing book crossing, however we first will measure the need for it to decide whether it is worth implementing or not.

To summarize, the problem we are solving is the difficulty to find similar books. The target audience for our project is people who read books. To test our assumptions, we are planning to try this on ourselves and see whether proposed books will be a good fit for us. The metrics for our project will be the amount of site users and their satisfaction with the recommendations. It is currently hard to make plans how to iterate our project, as this will mostly depend on the feedback we will be getting.

The book recommendation algorithm will be AI-based, the GitHub repository will be most likely open, and since we have a Machine Learning algorithm we will have two dedicated ML developers in our team. We are confident that we can complete the project by ourselves without other teams’ help.

{{< hint danger >}}

**Feedback**  

Hi, I think this is a great project and idea! Since this course aims to finish the semester with an MVP - minimal viable product, consider scaling your project down to creating a web app that does core/main things. Outline main features of your project and focus on execution. I would also think about which particular parts you can strip down - for example, UI can be very simple (I am saying all this because we have only 7 weeks).  

One website that I actually use is called goodreads.com - it's a book recommendation platform which is also a social network of the sort. It helps people to form communities and discuss books. However, this platform mainly oriented towards English-speaking users. Perhaps, your team can take some good ideas/features and replicate them in your website. You can think about parsing their book scores as an initial data for the recommendation service.

Overall, I think this is a very good project idea, that now requires a well-planned execution. Therefore, plan for simplified version that showcases main features.

{{< /hint >}}

## **Week 2 report**

**Architecture Design**

1. Component Breakdown:
    * Create UI/UX for site
    * Create login/welcome page
    * Create recommendation page
    * Create account information page
    * Design databases for users and books
    * Create starting version of recommendation algorithm
    * Add links to online bookshop for the recommended books (this is not a high priority task, and generally we are not sure whether we can do it without using web scraping)
    * If we have enough time, create some book compilations based on genre

2. Data Management: We are planning to have a database for storing tables about books and users, they most likely will be PostgreSQL, MySQL or SQLite. We are not sure, as we have not decided where the database will be located.

3. User Interface Design: While most of the design is set in stone, it is still subject to some minor changes. Link to [Figma Model](<https://www.figma.com/file/re5Sxk8RQA22Xr90WxL3un/Untitled?type=design&node-id=0-1&t=5WoM93cL9oqVIEhN-0>)
Screenshots to show progress at the time of report submission:
![alt text](https://i.ibb.co/3kgLGwV/1.png)
![alt text](https://i.ibb.co/6B2fHwN/2.png)
![alt text](https://i.ibb.co/gD8jdk1/3.png)
![alt text](https://i.ibb.co/vv9hJF9/4.png)
![alt text](https://i.ibb.co/rcRh2zF/5.png)
![alt text](https://i.ibb.co/YPnDqpr/6.png)

4. Integration and APIs:  We are planning to utilize Google Books API to get important information about books: annotations, genres, etc. This data will be used for recommendation algorithm and will also be displayed together with book’s cover on the site

5. Scalability and Performance: Since we are still in brainstorming stage of our project, we can't really predict its performance, but we hope that the expected time of our site’s response time will be not higher than a couple of minutes  

6. Security and Privacy: Once we choose the database language, we will be able to provide more accurate information about what protection of database we will utilize to avoid malicious actions.

7. Error Handling and Resilience: The lowest bar for us will be that all occurring errors must be handled, or at least not interfere with the product use.

8. Deployment and DevOps:We are yet to decide where we will deploy our product, since there are currently few free deployment options.

**Week 2 questionnaire:**

1. Tech Stack Resources: Are you utilizing any project-based books that specifically cover your tech stack and help you build your project?
    * Answer: We do not have plans to use any books, as none of us have read books, which would be particularly helpful. And we most likely won't have enough time to read any book in full, since we have only 6 weeks remaining.

2. Mentorship Support: Do you currently have a mentor actively involved in your project?
    * Answer: Our team does not have a mentor, and we are not looking for one, as we are confident we will be able to deliver the MVP at the end by ourselves.

3. Exploring Alternative Resources: In addition to project-based books, what other resources have you explored to expand your understanding of your tech stack?
    * Answer: our ML developers use [Kaggle](<https://www.kaggle.com>) to learn more about it. One of the particularly useful [videos](<https://www.youtube.com/watch?v=x-alwfgQ-cY>) on our topic. Frontend developers read [React documentation](<https://react.dev>).

4. Identifying Knowledge Gaps: Are there any specific areas within your tech stack where you or your team feel there are knowledge gaps or expertise is lacking?
    * Answer: We might have some problems connecting ML to backend, as it is not something our ML developers have a lot of experience in. But our team should be able to find out how to do it using open source tutorials and documentations.

5. Engaging with the Tech Community: Have you actively engaged with the broader tech community to seek guidance or learn from experienced professionals in your tech stack?
    * Answer: One of our members attended Innopolis meetup regarding Data Science and Machine Learning recently and shared information he learned there with the rest of the team.

6. Learning Objectives: What specific learning objectives have you set for yourself and your team in relation to your tech stack this week?
    * Answer: All of us had an Introduction to Machine Learning course, where we performed most of the tasks by the steps given by instructors. However now the development process is basically unsupervised, and we want to test ourselves in fully organizing project workflow, while also picking up knowledge in related fields.

7. Sharing Knowledge with Peers: How have you been sharing your knowledge and expertise with your teammates?
    * Answer: We had a number of meetups/brainstorms to make sure that everyone had time to speak their mind, and we were all on the same page regarding the vision of our project.

8. How have you leveraged AI to compensate for any lacking expertise in your tech stack?
    * Answer: We picked some inspiration from AI generated content, while picking logo and name for our product, so the AI involvement was rather limited so far.

**Tech Stack and Team Allocation:**

* We will code Backend and Machine Learning parts on Python and Frontend on React

Anastasia Martynova (Team Lead) – Designer/Frontend

Maxim Piniagin – Product manager/Backend

Yegor Sokolov – Backend

Marat Medvedev – ML/Backend

Lev Gorbunkov – Frontend

Bulat Kutlugallyamov – Backend/Frontend

Roman Voronov - ML/Backend

{{< hint danger >}}

**Week 2 Feedback by Rustam**  
This report is well written and structured, and it's a pleasure to see how your project takes shape. I liked the figma UI and
overall description of the project. Seems to me, you have fully aligned team that can effectively deliver results.  
Keep up the pace and make sure to put an emphasis on the execution.
Overall - good project and report.  
5/5

{{< /hint >}}

## **Week 3 report**

1. **Prototype Features:**
    * Link to GitHub [repository](<https://github.com/Ozurexus/BookHive>).
    * Since this is our first week of working directly on the code of our site, not the entirety of functionality has been implemented yet.
    * Current functionality. Below are also the images of work in progress pages, you can view planned full design in week 2 report:
        * User is asked to either to log in or register:
         ![alt text](https://i.ibb.co/GPJGDjr/1.jpg)
         ![alt text](https://i.ibb.co/T8qJMw0/2.jpg)
        * User is then asked to enter 5 books and rate them
         ![alt text](https://i.ibb.co/mtTcp5H/3.jpg)
         ![alt text](https://i.ibb.co/JKwY8R6/4.jpg)
        * In personal cabinet, one can view their username and status which is based on amount of rated books, change password and log out.
             ![alt text](https://i.ibb.co/rMxMfH4/5.jpg)
    * Technical details:
        * All information about users, books, and ratings is stored in a locally deployed PostgreSQL database, which was created based on this  [dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset) and was extended with book genres and annotations using Google Books API.

2. **Challenges and Solutions:** During the development, we faced a number of problems:
    1. Our ML developers had a lot of issues with preprocessing, which severely slowed them down:
        * The dataset was pretty raw: some books had no ratings and there were ratings of books, which had no information on them in other tables. Solution was to just remove such books.
        * For Matrix Factorization, books’ IDs had to be normalized from ISBNs, and this was quite difficult on Pandas. The solution was to use PySpark, which uses SQL, however further data augmentation was also hard due to little experience with PySpark. Because of that, after PySpark, data was converted back to Pandas.
        * All these problems took a lot of time for our ML developers, so ML part is not quite ready for the first prototype.
    2. Due to some books in dataset being extremely obscure, Google Books API did not have its annotations and/or genres, we are still working on solution of this issue, for now they just can't be recommended.
    3. Because of imprecise workload estimation on Frontend side, we did not have enough time to create recommendation page.

3. **Next Steps:**
    * ML team still has a lot to work on for the next weeks, as the recommendation model is planned to be implemented using users’ ratings from Dataset.
    * Frontend team will have to finish recommendation page structure and change all pages to look like their planned Figma design.  
    * Also, right now, our system lacks the function to save recommended to books into want to read tab for user.
