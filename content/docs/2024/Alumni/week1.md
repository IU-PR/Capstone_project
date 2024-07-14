---
title: "Week #1"
---

# Week 1 Report: Alumni Portal

## **Presentation**

{{< embed-pdf url="/2024/Alumni/pres-for-report.pdf" >}}

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member         | Telegram ID     | Email Address                     |
| ------------------- | --------------- | --------------------------------- |
| Nazgul Salikhova    | @kokosinka123   | n.salikhova@innopolis.university  |
| Anastasiia Ozerova  | @oneozerova     | l.smirnova@innopolis.university   |
| Chulpan Valiullina  | @Chehmet        | c.valiullina@innopolis.university |
| Anzhelika Akhmetova | @angelika782345 | a.akhmetova@innopolis.university  |
| Olesia Grediushko   | @WellNotWell    | o.grediushko@innopolis.university |
| Liubov Smirnova     | @mangocandle    | l.smirnova@innopolis.university   |
| Galia Shabanova     | @g7l7a          | g.shabanova@innopolis.university  |

### **Value Proposition**

- **The Problem:**

  We face three key problems due to alumni disconnection: 1) Graduates often lose touch with each other and the institution, hindering valuable experience-sharing and mentorship. 2) There is limited interaction between alumni and current students, depriving students of professional insights and guidance. 3) Many students are unaware of university projects and volunteer opportunities, weakening alumni engagement with the university.

- **Solution:**

  Alumni can actively engage by offering mentorship opportunities through organizing events where current students can apply to be mentored. Additionally, we offer exclusive alumni merchandise available for purchase. Alumni can also initiate clubs, welcoming not only fellow graduates but also students and anyone associated with the institution, fostering a diverse and inclusive community. Moreover, our platform facilitates donations from alumni for supporting special student scholarships. To enhance connection and inspiration, we suggest a blog showcasing alumni stories after graduation and an interactive map displays alumni locations worldwide, promoting a sense of global community. Lastly, our AI chat feature streamlines user experience by providing instant assistance, answering queries from students, assisting with event registrations, and facilitating site navigation seamlessly.

- **Benefits to Users:**

  - **Enhanced Alumni Engagement:** Our platform reconnects alumni with each other and with the institution, providing opportunities for mentorship, networking, and collaboration.
  - **Convenience and Efficiency:** Alumni can access a range of services and resources in one centralized platform, streamlining their engagement with the university community.
  - **Recognition and Support:** Advanced students are recognized and supported through special scholarships, fostering a culture of achievement and encouragement within the alumni network.
  - **Global Community Building:** The interactive map feature promotes a sense of global community by showcasing alumni locations worldwide, facilitating connections and fostering a sense of belonging.

- **Differentiation:**

  Our alumni website stands out through its comprehensive approach to alumni engagement, offering a diverse range of features tailored to meet the specific needs of both graduates and current students. From mentorship opportunities and exclusive merchandise to interactive mapping and AI-powered assistance, our platform provides a unique and multifaceted solution to the challenges of alumni disconnection.

- **User Impact:**

  Our platform has a profound impact on the lives of both alumni and current students by fostering meaningful connections, providing valuable support and resources, and promoting a sense of community and belonging. Alumni are empowered to give back to their alma mater and support the next generation of students, while current students benefit from mentorship, scholarships, and access to a vibrant and supportive network of graduates.

- **User Testimonials or Use Cases:**

  1. **Mentorship Success:** A recent graduate joins the mentorship program through the alumni website, connecting with an experienced alum who provides valuable guidance and support in their career journey.
  2. **Proud Merchandise Purchase:** An alumna purchases exclusive merchandise from the website, proudly showcasing her school pride with every wear.
  3. **Entrepreneurship Collaboration:** An entrepreneurial alumnus initiates an entrepreneurship club through the website, fostering collaboration and innovation among members.
  4. **Scholarship Support:** A successful alumna contributes to special scholarships through the website, helping deserving students pursue their academic goals.
  5. **Inspirational Blog Post:** An accomplished alumnus shares their post-graduation story on the alumni blog, inspiring others and fostering a sense of community within the alumni network.
  6. **Easy Pass Access:** An alumnus can request a pass on the platform, simplifying entry to campus facilities and events.

## **Lean Questionnaire**

<details>
<summary>1. What problem or need does your software project address?</summary>
  
Our project solves the problem of the lack of a platform for involving graduates in the future life of the Innopolis University after graduation. We provide the convenient opportunity to do all the alumni need in one place and with the guidance of artificial intelligence. Alumni will have an opportunity to sign to get an ID card to enter the university, become a mentor for younger students, buy special merchandise and make a donation of money. Future work includes pages where students will create events and register to them, volunteer in university activities, and meet with others if they are in the same city.

</details>

<details>
<summary>2. Who are your target users or customers?</summary>
  
Innopolis University graduates and students.

</details>

<details>
<summary>3. How will you validate and test your assumptions about the project?</summary>
  
We are going to let the Innopolis University alumni try to use this platform and check which functions they miss or use most often in the beta-version of our web-site.

</details>

<details>
<summary>4. What metrics will you use to measure the success of your project?</summary>
  
- Number of visits to the website
- Number of registered users
- Number of donations and bought merch
- Number of registered mentors

</details>

<details>
<summary>5. How do you plan to iterate and pivot if necessary based on user feedback?</summary>
  
We are going to listen to the feedback and implement the functions that customers also need and change the parts they don't like or don't use.

</details>

## **Leveraging AI, Open-Source, and Experts**

#### AI Chat for Alumni and Students:

- **Event Registration (for Alumni):** Simplified registration for events (Alumni meetings, events for students in Innopolis that they can visit).
- **Get Advice from Alumni (for Students/High School Students):** Students will be able to receive guidance from alumni like: "When to start a job?", "How to write thesis to successfully complete it on time?", "Was the ... retake difficult?", "What course more suitable ...?" etc.
- **Site Navigation (for All Users):** Easy navigation throughout the platform.

Our team has a strategic plan to leverage the following resources for the development and success of our Alumni project to add AI chat:

1. **AI (Artificial Intelligence):**

   - AI is an essential resource that we will extensively utilize in our project.
   - We will implement AI-driven chat features to facilitate seamless communication and support between alumni and students (RAG system that will allow to retrieve the appropriate answer from dataset for question written in natural language), and facilitate registration for alumni for actual events in Innopolis and other locations to organize Alumni meetings.

2. **Open-Source:**

   - Open-source resources play a significant role in our project’s development and success.
   - We will utilize open-source text generation LLM model for building our AI chat.
   - Additionally, we will try to find prepared datasets to train our model to provide advice related to courses, studying, and jobs. In other case, we will make a questionnaire for alumni.

## **Defining the Vision for Your Project**

- **Overview:**

  Our alumni website is a one-stop platform for graduates of Innopolis University. It aims to reconnect alumni with each other and with the university, providing valuable opportunities for engagement and support. Through features like mentorship programs, merchandise purchases, club initiatives, and scholarship support, we create a vibrant community where alumni can thrive. Our platform also includes AI-powered assistance and interactive mapping features to enhance user experience. We focus on convenience, efficiency, and making a positive impact on the lives of our users.

- **Schematic Drawings:**

  ![system_design](/2024/Alumni/system_design.jpg)

  [<u> Link to Design in Figma</u>](https://www.figma.com/design/ltbfjf5CwubDQ1I9UJGQKq/Untitled?node-id=0-1&t=FNR6wn8R2Dv13Dbc-1)

  ![first_UIdesign](/2024/Alumni/first_UIdesign.png)

- **Tech Stack:**

  - **Front-end:** JavaScript, React, CSS, HTML
  - **Back-end:** Python, Django
  - **ML:** Python, Python Notebook, open-source LLM, Milvus
