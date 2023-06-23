# Mushroomity #

Hello! We're an international team that will create an application called `Mushroomity`. This application
will identify the type of some mushroom by its photo and location.

## Week 1 ##
### Team Formation and Project Proposal ###

To create the application, our team contains ML-engineers for creating ML-model to identify mushrooms and
Flutter-developers who will create the mobile application.

#### Team members ####

| Team Member      | Telegram ID       | Email Address                     |
|------------------|-------------------|-----------------------------------|
| Timofey Didenko  | @n1ce_timothy     | t.didenko@innopolis.university    |
| Artyom Makarov   | @smulemun         | a.makarov@innopolis.university    |
| Damir Abdulayev  | @SpeedFireF       | d.abdulayev@innopolis.university  |
| Danil Kuchukov   | @xFonzie          | d.kuchukov@innopolis.university   |
| Almaz Dautov     | @hir0t            | a.dautov@innopolis.university     |
| Gleb Statkevich  | @glebkkevich      | g.statkevich@innopolis.university |
| Elmir Vadigullin | @Elmir_Vadigullin | e.vadigullin@innopolis.university |

---

#### Value Proposition ####

Our app solves the problem of identifying the type of mushroom by using photo and location data. It is a common issue
for mushroom hunters, farmers, and even ordinary people to accurately identify the types of mushrooms they come across.
Our app provides a unique solution to this issue by using AI to recognize the type of mushroom from photo and location
data. Our app is unique because it provides accurate and reliable identification of mushrooms, which is not available in
existing alternatives.

- Identifying the Problem: Many people make mistakes while collecting mushrooms, which can lead to poisoning and even
  death. In Russia alone, mushrooms poison thousands of people each year.
- Solution Description: Our app will identify the type of mushroom and indicate whether it is safe to eat or not.
- Benefits to Users: Our app enhances the safety of mushroom hunters and farmers by providing accurate identification of
  mushrooms. It also helps people to learn about different types of mushrooms and avoid consuming poisonous ones. Our
  app is user-friendly and provides a seamless experience to users.
- Differentiation: We conducted research on existing alternatives and found that they all have disadvantages that our
  app will overcome. For example, "Picture
  Mushroom" ([Google Play](https://play.google.com/store/apps/details?id=com.glority.picturemushroom&hl=en&gl=US),
  [App Store](https://apps.apple.com/us/app/picture-mushroom-fungi-finder/id1474578078)) cannot identify non-mushroom
  objects in photos, requires an internet connection, and is expensive. "Mushroom identificator"
  ([App Store](https://apps.apple.com/us/app/mushroom-identificator/id1227854971)) often incorrectly identifies
  mushrooms, and "Shroomify"
  ([Google Play](https://play.google.com/store/apps/details?id=com.mushroom.shroomify&hl=en&gl=US),
  [App Store](https://apps.apple.com/ca/app/shroomify-canada-mushroom-id/id1490594715)) only provides identification for
  certain locations. Our app will provide accurate identification offline and will be affordable.
- User Impact: Our app will have a positive impact on the safety of mushroom hunters, farmers, and ordinary people. It
  will also promote awareness about different types of mushrooms and their characteristics.
- User Testimonials or Use Cases:
  [In 2017](https://www.latimes.com/local/lanow/la-me-ln-mushroom-sickness-20170602-htmlstory.html)several a toxic
  mushroom poisoned people in California because they did not have an app to identify it. Our app will help all
  people, from professional mushroom pickers to beginners. We will also organize events to help professionals share
  their experiences with others in local areas.

---

### Lean Startup Methodology ###

Our software project addresses the problem of identifying the type of mushroom by using a photo and location data.

Our target users are mushroom hunters, farmers, and ordinary people who come across mushrooms and want to identify them.
We will also consider occasional mushroom pickers and beginners.

Before creating a dataset for training our AI model, we will consult with mushroom specialists to determine what
information we need to collect. We will also share our results with our mentor for feedback. Before developing the app,
our designer will create detailed designs, which we will use to make improvements.

We will ask users to test new features and use their feedback to decide what to do next. We will also ask our friends
and relatives to collect mushrooms and test the app.

---

### Leveraging AI, Open-Source, and Experts ###

We will conduct our own research to find the best CNN-model for identifying mushrooms. We will also use a second model
to analyze location data. These two models will form our AI model.

We have not found any open-source projects or experts that can help us at this time.

### Defining the Vision for Your Project ###

- Overview: Our app uses AI to identify the type of mushroom using photo and location data. Users can take a photo of
  the mushroom and provide location data, and our app will provide an accurate identification of the mushroom.
- Schematic Drawings: Our app consists of a user interface, an AI algorithm for mushroom identification, and a database
  of mushroom types. The user interface allows users to take a photo and provide location data. The AI algorithm
  processes the photo and location data to identify the type of mushroom. The database provides information about
  different types of mushrooms.
- Tech Stack: Our app uses Python for the AI algorithm, Flutter for the user interface, and Postgresql for the database.
- Anticipating Future Problems: We anticipate potential problems related to the accuracy of identification and user
  engagement. We will mitigate these problems by improving the AI algorithm and user interface.
- Elaborate Explanations: Our AI algorithm uses computer vision and machine learning to identify the type of mushroom
  from a photo. It analyzes the shape, color, and texture of the mushroom to provide an accurate identification. The
  database provides information about different types of mushrooms, including their characteristics and toxicity levels.
  Our app is unique because it provides accurate and reliable identification of mushrooms even offline, which is not
  available in existing alternatives.

Here's how the structure of the project will look like:
![](../../../static/Mushroomity/Project%20Structure.PNG)

---

{{< hint danger >}}
**Feedback**

**Value Proposition**

Good stating for the problem. But
> Our app stands out from competing solutions because

How did you know that you stand out? Did you make any market research?

Uses cases stated are not correct. You need to give details how your product will be used and by whom exactly.

**Lean startup question**

The whole section very short, and you didn’t spent much time considering answering.
How will you act on the feedback, how will you iterate on it?

**AI**

What AI algorithm will you use?

**Vision Of The Project**
Missing Schematic Drawings

**Overall**

The report is weak. And I think it was made very fast. Without much consideration.

2.5/5

_Feedback by Moofiy_
{{< /hint >}}

## Week 2 ##

In week 1, we formed a team based on each person's knowledge and expertise. We have 2 people skilled in Flutter
development, 4 strong in Data Science, and 1 team leader and designer who connects everyone together. This week, we were
asked to focus on architecture design and tech stack. Since we already know which technologies we will use, we will
concentrate more on architecture design. We have created a backlog for our project, where we collect all tasks necessary
to create the entire app.

### Architecture Design ###

Our app will be as simple as possible. To describe it, we will use some topics you provided:

Component Breakdown: The main part will be the app itself, which will be downloaded to the user's phone. The app will
request access to the camera for taking photos. It will also be connected to our server, which is the second part. The
server will contain all user information, such as contacts and account passwords. If the user agrees, the server will
also download photos of mushrooms that we will use to improve our model. The final component of the project is the
model. We will train the model using our sources only, and the prepared model will be stored in the app for mushroom
identification.

Data Management: We will use Firebase, specifically the Real-time Firestore database, for data storage. It will store
information about users and chats. Additionally, there will be a server-side storage for some mushroom photos.

User Interface (UI) Design: Starting next week, our designer will create designs for all pages and elements in our app.
Before developing anything in Flutter, our team will aim to create the best design possible.

Integration and APIs: There will be no APIs in our project.

Scalability and Performance: Initially, we will use only free services because we are students and don't have the funds.
If we secure investments, we will scale our app to provide better performance for our users.

Security and Privacy: Firebase offers security settings for projects, so user data will be protected. The only way to
steal data from the database is to gain access to a user's phone with the app installed. Users must create an account
with a password for chatting in our app, and they can enable 2-factor authentication if needed.

Error Handling and Resilience: We will create a system that handles errors and sends them to our server, while the user
receives a message indicating that an error occurred.

Deployment and DevOps: We have already created a repository on GitHub. Firebase also provides a reliable interface for
connecting Flutter applications, which we will use.

### Questionnaire ###

1. Tech Stack Resources: We will not rely on project-based books. Instead, we believe that alternative resources and
   mentorship support will be sufficient for this project.
2. Mentorship Support: We have invited [Yusuf Mesbah](https://t.me/Yusufroshdy)
   and [Andrew Milevsky](https://t.me/notnepho) as our mentors. Yusuf has extensive experience in ML-engineering, and we
   have worked with him on ML and NIC courses. Andrew Milevsky is a seasoned Flutter developer. Additionally, we have
   invited a professional mushroom picker from Russia to help us learn how to analyze mushrooms. We believe their
   expertise and fresh perspective will be invaluable to our project.
3. Exploring Alternative Resources: We will use official documentation for all technologies we are using. Additionally,
   we will utilize YouTube tutorials to develop our project.
4. Identifying Knowledge Gaps: Our main challenge is identifying mushroom types, as none of us have experience in this
   area. However, with the guidance of our mentors and the help of a professional mushroom picker, we are confident that
   we will fill this gap soon. Additionally, we have invited an experienced Flutter developer to join our team to ensure
   we have the necessary expertise.
5. Engaging with the Tech Community: To stay up-to-date on the latest developments in the AI field, we are actively
   participating in the [OpenAI community forum](https://community.openai.com/) and [Kaggle](https://www.kaggle.com/).
   We are also interested in joining the [Open Data Science](https://ods.ai/) project and attending local events to
   share our project and receive feedback from the professional community.
6. Learning Objectives: Our team is divided into two groups: ML and Flutter developers. The ML group will search for
   datasets for the project and determine the best way to analyze them. The Flutter group will revise their knowledge in
   developing on Flutter. Additionally, everyone on the team will increase their knowledge in identifying mushrooms.
7. Sharing Knowledge with Peers: We have created an organization and repository on GitHub to facilitate collaboration.
   Each team member will review and provide feedback on completed tasks, and we will hold weekly meetings to share
   results, provide new ideas for the project, and improve our communication.
8. Leveraging AI: We will try to find prepared resources from Kaggle, and we will also utilize OpenAI services, such as
   ChatGPT, to expedite the process of acquiring knowledge and expertise.

---

### Tech Stack and Team Allocation ###

In total, we have this picture:

- Flutter: Flutter will be used to create a mobile app connected to the Firebase
  server. [Gleb](https://github.com/staglente) (lead) and [Elmir](https://github.com/VadigullinElmir1) are on charge.
  They will collaborate and exchange tasks as needed.
- Server: The server will store information about users and chats and will be created using
  Firebase. Gleb and Elmir are responsible for this task.
- Dataset: The dataset will be created using various methods mentioned above. [Danil](https://github.com/xFonzie)
  (lead), [Artyom](https://github.com/Smulemun), [Damir](https://github.com/SpeedFireF)
  and [Almaz](https://github.com/thehir0) will handle that.
- AI-model: The AI model will be constructed using CNN and ANN together because we might not rely solely on pictures.
  Artyom (lead), Danil, Damir and Almaz will work on this part.
- Design: Before creating the application, we must understand its appearance. [Timofey](https://github.com/Zener085)
  will handle the design aspect.

---

## Comments that will be removed ##
As a team leader of the team, I would kindly ask you to send feedback a bit earlier. For our team, it's kinda difficult
to resolve some problems that you wrote in the feedback on the last day. We spent much time doing our stuff, and then we
had to do it again just because you don't like our point of you. I also ask you to provide stronger articles for each
week and feedback and, also, don't forget about grammar. As for me, it was hard to understand what you wanted from us
and then get a message that something that was not described well was wrong or missed. Moreover, there were lots of
grammar mistakes, that's annoying.

---


{{< hint danger >}}
**Feedback**  

**1. Component Breakdown**

Good, but better to represent the divine thorough bullet points  

**2. Data Management**

Good!!

**3. UI Design**

Missing designs.

**4. Integration and APIs**

Then how will you integrate with the model?


**5. Scalability and Performance**
We understand that you are students and don’t have money we don’t ask you to use any paid services. We ask you what will be your plan to ensure scalability. 
BTW all students answered it. Why couldn’t you?

**6. Security and Privacy**
Good

**7. Error handling and Resillience**
How? What will be the mechanism when dealing with a crash? 

**8. Deployment and DevOps**
Good

**Answering questioner**
Moderate answering. 
What Youtube tutorials you made? 

But having a person who knows Mushroom types, this is indeed very good. 
Points 4,5,6,7 and 8 are good!


**Overall**
The report is partially weak, you didn’t spend much time answering nor thinking on the first part. It is clearly show that you didn’t spend much time reflecting on the questions.

Grade 3/5


_Feedback by Moofiy_
{{< /hint >}}


{{< hint danger >}}
**Feedback**  

Comments that will be removed #
>  because you don’t like our point of you.

First it's point of view, not point of you. Second, not because I didn't like it, it's because it was wrong.
Third, please don't talk about grammar when you yourself, don't know how to write grammatically correct text :)

Grammatical errors in your comment:

- "As a team leader of the team" - "of the team" is redundant when "team leader" is already used.

- "it’s kinda difficult" - "kinda" is informal and not considered Standard English. It should be "kind of".

- "and then we had to do it again just because you don’t like our point of you." - It should be "point of view," not "point of you."

- "I also ask you to provide stronger articles for each week and feedback and, also, don’t forget about grammar." - The conjunctions here are causing confusion and make the sentence grammatically incorrect. You need to split this into separate sentences or rephrase.

- "Moreover, there were lots of grammar mistakes, that’s annoying." - This sentence contains a comma splice. The two independent clauses should be separated by a period or a semicolon, or linked by a conjunction.


_Feedback by Moofiy_
{{< /hint >}}