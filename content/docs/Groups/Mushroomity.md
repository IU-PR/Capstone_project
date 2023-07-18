# Mushroomity #

<div style="text-align: center;">
  <img src="/Mushroomity/project_logo.png" alt="Logo" width="546" height="546">
</div>

Welcome to Mushroomity, a dedicated team committed to making a significant impact in reducing the number of mushroom
poisoning cases.
Our mission is to raise awareness, educate, and empower individuals to safely enjoy the wonders of
mushrooms without the risk of harm.

At Mushroomity, we understand the importance of distinguishing edible mushrooms from potentially toxic ones.
Our team of programmers, scientists and mycologists collaborates to provide valuable insights and resources to ensure
the well-being of mushroom enthusiasts.

Our mycologists are at the forefront of mushroom identification and classification. They meticulously study different
species, their distinct characteristics, and potential risks associated with consumption.

Understanding the symbiotic relationships between mushrooms and other organisms helps us identify potential
risks and educate individuals about the importance of preserving the delicate balance of nature.
By studying these compounds, we aim to develop methods for detecting harmful substances
and raising awareness about the dangers they pose.

Through our research, Mushroomity strives to reduce the number of mushroom poisoning cases worldwide. Our team is
dedicated to providing reliable information, resources, and support to ensure that individuals can confidently enjoy the
benefits of mushrooms while minimizing the risks.

Use our application to create a safer mushroom-loving community. Whether you are a novice enthusiast, an avid forager,
or simply curious about mushrooms, Mushroomity is here to guide you towards a safer and more enjoyable mushroom
experience. Together, let's embrace the wonders of mushrooms while prioritizing our well-being.

Here's our presentation of the project {{< embed-pdf url="/Mushroomity/Mushroomity.pdf" >}}


# Week 1 #

## Team Formation and Project Proposal ##

To create the application, our team contains ML-engineers for creating ML-model to identify mushrooms and
Flutter-developers who will create the mobile application.

### Team members ###

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

### Value Proposition ###

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

## Lean Startup Methodology ##

Our software project addresses the problem of identifying the type of mushroom by using a photo and location data.

Our target users are mushroom hunters, farmers, and ordinary people who come across mushrooms and want to identify them.
We will also consider occasional mushroom pickers and beginners.

Before creating a dataset for training our AI model, we will consult with mushroom specialists to determine what
information we need to collect. We will also share our results with our mentor for feedback. Before developing the app,
our designer will create detailed designs, which we will use to make improvements.

We will ask users to test new features and use their feedback to decide what to do next. We will also ask our friends
and relatives to collect mushrooms and test the app.

---

## Leveraging AI, Open-Source, and Experts ##

We will conduct our own research to find the best CNN-model for identifying mushrooms. We will also use a second model
to analyze location data. These two models will form our AI model.

We have not found any open-source projects or experts that can help us at this time.

## Defining the Vision for Your Project ##

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
<div style="text-align: center;">
  <img src="/Mushroomity/project_structure.png" alt="Project structure" width="1265" height="511">
</div>

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

# Week 2 #

In week 1, we formed a team based on each person's knowledge and expertise. We have 2 people skilled in Flutter
development, 4 strong in Data Science, and 1 team leader and designer who connects everyone together. This week, we were
asked to focus on architecture design and tech stack. Since we already know which technologies we will use, we will
concentrate more on architecture design. We have created a backlog for our project, where we collect all tasks necessary
to create the entire app.

## Architecture Design ##

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

## Questionnaire ##

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

## Tech Stack and Team Allocation ##

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
We understand that you are students and don’t have money we don’t ask you to use any paid services. We ask you what will
be your plan to ensure scalability.
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
The report is partially weak, you didn’t spend much time answering nor thinking on the first part. It is clearly show
that you didn’t spend much time reflecting on the questions.

Grade 3/5

_Feedback by Moofiy_
{{< /hint >}}

{{< hint danger >}}
**Feedback**

Comments that will be removed #
> because you don’t like our point of you.

First it's point of view, not point of you. Second, not because I didn't like it, it's because it was wrong.
Third, please don't talk about grammar when you yourself, don't know how to write grammatically correct text :)

Grammatical errors in your comment:

- "As a team leader of the team" - "of the team" is redundant when "team leader" is already used.

- "it’s kinda difficult" - "kinda" is informal and not considered Standard English. It should be "kind of".

- "and then we had to do it again just because you don’t like our point of you." - It should be "point of view," not "
  point of you."

- "I also ask you to provide stronger articles for each week and feedback and, also, don’t forget about grammar." - The
  conjunctions here are causing confusion and make the sentence grammatically incorrect. You need to split this into
  separate sentences or rephrase.

- "Moreover, there were lots of grammar mistakes, that’s annoying." - This sentence contains a comma splice. The two
  independent clauses should be separated by a period or a semicolon, or linked by a conjunction.

_Feedback by Moofiy_
{{< /hint >}}

# Week 3 #

This week, we initiated the creation of all components required for the project. We developed the initial UI design for
the primary pages, crafted parsing scripts to automatically generate datasets, and established the back-end systems for
the application. However, we encountered some issues along the way.

## Developing the first prototype, creating the priority list ## 

As we only began working on the project this week, we have yet to produce a functional prototype for users to test.
Nonetheless, we developed a basic frontend system that incorporates the primary functions of the project.

- Technical Infrastructure: To be prepared, we only need from everyone to know how to work with their tech stack and
  some GPUs for training our model:
  - The first 2 weeks our main developers (Gleb and Elmir) reminded Flutter, and for today they are ready to create
    everything our app needs to. They've already created a starter part of the app, but we decided to remove it after
    contacting the professor.
  - Right now we don't need GPUs for training our model because we don't have the model:) But our own GPUs are
    prepared and just waiting.
  - In total, our team has already created all stuff for working together (organization, repositories and projects for
    them). Also, we conducted with the professor, who knows a lot about mushrooms, and now we understand, how to
    prepare the model and create an application.
- Backend Development: Right now we don't have any backend due to we started in the wrong way.
  There will be explanation about it later.
- Frontend Development (UI):
  We have created the first version of the main pages in the app. Next week we will change the design a bit, but now you
  may see this picture:
  - When you open the app, you firstly have to log in or sign
    in:

    <div style="">
      <img src="/Mushroomity/login_page.png" alt="Login" width="376" height="768">
    </div>

  - After that, you go to the main page, where you can go to other pages or analyze mushroom by
    photo:

    <div style="">
      <img src="/Mushroomity/main_page.png" alt="Main page" width="376" height="768">
    </div>

  - After taking a photo, you go to the page with this photo and description of mushroom in
    it:

    <div style="">
      <img src="/Mushroomity/info_page.png" alt="Information page" width="376" height="768">
    </div>

    The description might be changed, now it's just an example.
  - Of course, you may want to change language or log out. For that, you may go to the settings
    page:

    <div style="">
      <img src="/Mushroomity/settings_page.png" alt="Settings" width="376" height="768">
    </div>

  - In addition, in the app you will also be able to chat with other people about any topics you want by using
    forum:

    <div style="">
      <img src="/Mushroomity/forum_page.png" alt="Forum page" width="376" height="768">
    </div>

- Data Management: All data for models are stored now in Google Drive. We have a parser script that parses some sites,
  takes photos of mushrooms with their names and stores that in some packages. Packages are created in the following
  way:
  There are lots of packages for each family of mushrooms. In each package, there are some packages also for each type of
  mushrooms. Finally, in each package, there are some photos of mushrooms of this type and family.
- Prototype Testing: We cannot start testing the app because now there's nothing that can be tested.

Simply speaking, we don't have anything to show except design. And it happened because we didn't realize how we have to
analyze mushrooms. Here are some details:

---

## Professional mushroom picker ##

Last week, we mentioned that
`we have invited a professional mushroom picker from Russia to help us learn how to analyze mushrooms`. Unfortunately,
this individual did not show up or respond to our attempts to contact them. Consequently, we began searching for someone
else who could assist us. Finally, this week we spoke with a professor from Kazan Federal University who informed us
that we had misunderstood the problem. Initially, we believed that a photograph of a mushroom would be sufficient to
identify one of the 1,000 types of mushrooms in the world. However, as it turns out, there are more parameters to
consider than just a photo. Additionally, there are 1,000 types of mushrooms in Tatarstan only. Therefore, we have
decided to focus solely on our region to improve the accuracy of our model in its initial stages. Furthermore, we need
to identify the main parameters that cannot be determined by a photo. For example, a crucial parameter for identifying
the type of mushroom is knowing where it grew. If it grew on a tree, we might also be able to determine the type of
tree. Of course, we cannot include all parameters, or else people would need to spend an excessive amount of time
marking all the details.

---

## Future work ##

Next week, our main objective is to locate high-quality sources containing numerous photos of mushrooms from Tatarstan.
Additionally, we will identify the primary parameters required for mushroom identification and adjust our model by
incorporating these parameters into the photos. Since we cannot provide all the necessary details to the Flutter team,
their task will be to develop other essential features such as  `log in`  and  `page switching` .

{{< hint danger >}}
**Feedback**  


**Prototype Features**<br>
Missing section


**User Interface**<br>
The UI you created is too basic. It look neat though. I would advice you instead of creating everything from scratch you can utilise Figma community. There you can see a lot of pre made design that you can follow or use their components.

PS: Images doesn’t show on the site, you should fix that.


**Challenges and Solutions**<br>
Missing section, or is it the Mushroom expert guy?
If so, then it’s good that you are trying to find alternative solution.
But think you should keep trying to find an expert this will make your app better.

**Next Steps**<br>
Good, but how will you secure those images?



**Overall**<br>
Please stick to the report template and provide answers to what is requested.
For example where are your features? Challenges?

**Grade<br> 4/5**





_Feedback by Moofiy_
{{< /hint >}}

# Week 4 #

## External Feedback ##

We have found testers from the Russian community who are ready to start using our application and provide feedback. We
hope that they will be of great assistance, especially since some of them are experts in mycology. Unfortunately, our
prototype is not yet complete, but we are working diligently to finish it as quickly as possible so that we can provide
the application to our testers next week.

---

## Testing ##

In general, we did not dedicate a significant amount of time to testing the app due to a lack of available resources.
Here are some details regarding this matter.

### Flutter ###

This week, we only connected the linter for the project. Our plan for next week is to include automated tests for the
project, focusing on the app's core functionality while our friends use the prototype.

### ML ###

This week, our focus was on creating the dataset. Therefore, we did not spend much time considering how to test our AI
model.

---

## Iteration ##

As you may recall, this week can be considered as the first iteration of our project.

### Design ###

We made some minor changes to the design (refer to the week 3 report). There are changes in colors only.

### Flutter ###

We focused on the main functionality of the application. One team member worked on integrating the model and deploying
the server, while another teammate worked on creating the main page of the application with the "Upload photo"
functionality. Since we aim to provide the prototype to our testers as soon as possible, we are dedicating a significant
amount of time to implementing the main functions and creating the server for storing photos and adding users.

### Data ###

We finished the dataset, which now contains around 40,000 photos of mushrooms (with no augmentation) of 400 types of the
most popular mushrooms in Russia. Here's
a [link](https://drive.google.com/drive/folders/11xssHFrwALQwNvw5jEcmnGDOt6MaOKWW) to a part of the dataset you can see
right now.

### Model ###

For analyzing photos, we used [Xception](https://keras.io/api/applications/xception/) and added our own layers. This
model will be used in the prototype, and next week we will enhance the model to request additional information (not from
the photo) for better determination.



{{< hint danger >}}
### Dear Mushroomity, I already graded you last week, but it seems like that something wrong happened with the push

**Feedback** 

**External Feedback**<br>
So you don't have feedback.
It's week 4, and your prototype is not ready yet? Why?
It's super easy to create a prototype and get feedback from it.
A lot of students have already done that.

**Testing**<br>
Okay, setting up a linter is good, but this is not testing.

A linter checks your code for potential issues and style consistency without executing it, while testing involves executing your code and verifying that it works as expected under different conditions.

Besides, any Flutter project comes with a built-in linter. So basically, you did nothing?

**Iteration**<br>
Okay, it's good that you are thinking of the iteration. Also, keep in mind:

An iteration plan is essentially the plan for an upcoming iteration. It would typically outline:
* The goals and objectives for the iteration: what the team aims to achieve.
* The features to be developed.
* The tasks needed to develop these features. This might include coding, testing, design tasks, etc.
* Any assumptions or dependencies.
* A timeline for the iteration.

**Overall**<br>
The report is weak. It's clear that you haven't made much progress. If you don't have a prototype and didn’t started development. You are approaching week 6. At this pace, you might fail the course.

Please pay attention to the development and progress of your project.

**Grade: 2/5**

_Feedback by Moofiy_
{{< /hint >}}


# Week 5 #

During this week, our team focused on working with the application and upgrading the AI model. We also received valuable
feedback from our testers, which helped us gain insights into our mistakes and how to rectify them.

[Here](https://drive.google.com/drive/folders/1wY18jDB6oyiyjMIQR5KuGJEi6PNIxFtq) you can find a prototype (it will be
updated for the testers during the week)

At the beginning of the week, we shared our prototype with the testers we had recruited two weeks ago. We allowed them
to install the application and analyze various mushrooms. Initially, our AI model was trained to determine only 100
types of mushrooms, resulting in numerous mistakes by our testers. However, we prioritized the usability of the
application over its correctness.

One issue we encountered was that three photos provided by the sample users were too large. As a result, the users
struggled to capture the mushrooms in the best possible way, leading to suboptimal images for analysis by the model.
Consequently, the model faced difficulties in accurately analyzing these photos.

In terms of feedback collection, we made the mistake of not collecting answers to specific questions from our testers.
Instead, we simply waited for any feedback they could provide. However, this approach proved to be inadequate as users
primarily reported problems that we were already aware of. Despite informing them that the model was not performing
well, users still struggled to understand all the mushrooms correctly. Additionally, some users found it challenging to
articulate their feedback effectively. To address these issues, we have decided to create forms with specific questions
for users to answer, ensuring better feedback collection in the future.

Moving forward, our focus for the upcoming week will be on updating the application to improve its appearance and
performance for our users. We plan to add more features, particularly descriptions for as many types of mushrooms as we
can complete.


{{< hint danger >}}
**Feedback**

**Collecting and documenting feedback**<br>
Missing


**Feedback analysis**<br>
missing

**Roadmap and enhancement**<br>
missing
the enhancement part is short.

The report is weak and doesn't relate to any of the requested tasks 


**Grade: 0/5**


_Feedback by Moofiy_
{{< /hint >}}
