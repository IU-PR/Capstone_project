---
weight: 1
bookFlatSection: true
title: "To be announced - Identification of compounds"
---

# **To be announced - Identification of compounds**

{{< embed-pdf url="/PDF/To_be_announced.pdf" >}}

# **Week #1 Progress report**

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member        | Telegram ID | Email Address                     |
|--------------------|-------------|-----------------------------------|
| Evgenij Ivankin    | eugen_iv    | e.ivankin@innopolis.university    |
| Vitaly Mahonin     | tNabuki     | v.mahonin@innopolis.university    |
| Timolai Andrievich | tandrievich | t.andrievich@innopolis.university |

## **Value Proposition**

### Identify the Problem:
For decades, chemical scientists and students have wasted their time on converting compound representations from one form to another. It is not only a problem of wasting several minutes per formula, but also the fact that the algorithms for such conversions are pretty complex and require students to study them for about half a year before they can be applied. Even experienced scientists can make errors due to human factors, so double-checking the formula is usually required. People also tend to forget things, so they need to restudy the algorithm from time to time. Additionally, sometimes even non-chemistry people need to do some chemistry, but the main obstacle for them may be not knowing how to identify the name of the molecule from a drawing, as well as not having enough time to learn how to do it.

### Solution Description:
To provide the most user-friendly experience possible, we need a mobile application that can instantly name a compound and provide its simple string notation (e.g. SMILES/InChl/IUPAC) by just taking a picture of its graphical representation.

### Benefits to Users:
With this solution all three groups of users will be satisfied:
- Scientists will no longer waste their precious time doing mechanical work.
- Students can study less boring material.
- Non-chemistry people now have no barriers to doing basic chemistry.

### Differentiation:
There are already some applications that solve a part of this problem. The closest analog is the "Organic Compound Identifier" app, but it does not detect the compound from the photo/drawing. Rather, it prompts the user to input the formula in the graph form by placing predetermined blocks of atoms and then connecting them. It is also limited to organic compounds only. Our application, on the other hand, is general-purpose for any compound, faster to apply, and easier to use.

### User Impact:
The major impact is made on students. While they still need to study the principles of compound representation conversions, now knowing only the essentials reduces the half-year course to several weeks. Scientists will be able to concentrate more on the research they are doing, spending no time identifying and searching for molecules in the database by hand. Lastly, now even inexperienced people can be involved in some parts of science.

Overall, all the positive impact leads us to a faster growth of this science in both aspects: study and researching, as well as simplification of some domains of chemistry.

### Use Cases:
1. Scientist
- A chemical scientist working on a research project needs to identify a compound from a graphical representation. She opens the app, takes a picture of the compound, and obtains its name and linear notation instantly, saving her time and effort.
- Another chemical scientist is looking at a molecule structure in a conference presentation but cannot recognize it. He quickly takes a photo of it using the app and gets an accurate name and SMILES string.

2. Students
- A chemistry student is practicing identifying compounds from graphical representations as part of their homework assignment. Instead of manually converting them one by one, he uses the app to take photos of each one and quickly get their names and SMILES notations.
- While studying for an exam, a chemistry student comes across a compound that she is unfamiliar with. She scans its representation into the app, receives its name and SMILES string, and can continue with her studies.

3. Non-Chemistry people
- A user is browsing social media and sees an interesting post about a molecular structure. They snap a picture of it, and the app identifies the compound, providing them with its name and SMILES notation, which they can then share with others or look up for more information.
- A person is planning a DIY home project that involves using different chemicals. Given the idea, they saw in a chemistry book, but it was made for professionals and some compounds are just drawn with no naming. So they can use this app to easily determine the names of the needed compounds (or if there is no name, just SMILES notation), so now they can search for them on the internet.

## **Lean Startup Questionnaire**

1. What problem or need does your software project address?
> Our software project addresses the problem of wasting time and effort in converting organic compound representations from one form to another. It also aims to simplify the identification of compounds from graphical representations, making it easier for non-chemistry people to do basic chemistry.
2. Who are your target users or customers?
> Our target users are chemical scientists, students, and non-chemistry people who need to identify compounds from graphical representations.
3. How will you validate and test your assumptions about the project?
> We plan to validate and test our assumptions by conducting user interviews, surveys, and usability testing. We will gather feedback from early adopters and iterate accordingly.
4. What metrics will you use to measure the success of your project?
> The metrics we will use to measure the success of our project include user engagement (number of active users, frequency of app use), user satisfaction (ratings and reviews), and conversion rates (number of paid subscribers).
5. How do you plan to iterate and pivot if necessary based on user feedback?
> We plan to iterate and pivot based on user feedback by regularly collecting user feedback through surveys and usability testing. We will prioritize feature requests and bug fixes based on user impact and implement changes in iterative releases. If necessary, we are open to pivoting our product strategy or target market based on data-driven insights.

## **Leveraging AI, Open-Source, and Experts**

- AI (Artificial Intelligence):
> We aim to use AI tools such as Copilot, Tabnine, ChatGPT and others during the development process.
- Open-Source:
> We will utilize publicly-available research in our area to develop an efficient AI that meets the requirements of our target audience.
- Experts in relevant domains:
> We plan to leverage experts in relevant domains by engaging them to provide insights, suggestions, and feedback on our product design and functionality.

## **Inviting Other Students**

We are **NOT** looking for new teammates.

## **Defining the Vision for Your Project**

### Overview:
- Summary:
Our project is a software program that uses AI to convert images into SMILES notation, a simplified chemical representation. The purpose of this program is to make it easier for researchers and scientists to translate chemical structures in images into a format that can be easily analyzed and shared.

- Problem or Need:
Analyzing chemical structures from images is a time-consuming and error-prone process, which can slow down research and prevent scientific breakthroughs. Our project addresses this problem by providing a fast and accurate way to convert chemical structures in images into SMILES notation, which can be easily analyzed and shared among researchers and scientists.

- Benefits and Impact:
By providing a more efficient way to analyze chemical structures in images, our software program will save researchers and scientists valuable time and resources. Additionally, the accuracy of the program will reduce errors in data analysis, leading to more reliable results and faster scientific discoveries. Ultimately, our project will have a positive impact on the scientific community by promoting greater collaboration and knowledge sharing.

### Schematic Drawings:
![](https://i.ibb.co/DrvPS1T/Screenshot-from-2023-06-10-22-37-50.png)

### Tech Stack:
Based on the project requirements, team expertise, and considerations for scalability, performance, security, and ease of development, we have decided to utilize the following technologies, frameworks, and programming languages in our project:

Python: We will be using Python and PyTorch for neural net model development. Python is a popular and powerful programming language that has strong support for data analysis, machine learning, and artificial intelligence. Our team is experienced in Python and it is well-suited for building complex models quickly and efficiently. It also provides many useful libraries and packages such as NumPy, Pandas, and TensorFlow, which further enhances our productivity, reliability, and accuracy.

Flutter: We will be using Flutter for our mobile application UI. Flutter is a modern and versatile framework that allows us to build beautiful, responsive, and performant interfaces for both Android and iOS platforms with a single codebase. It is written in Dart, a fast and easy-to-learn programming language that enables us to create robust and flexible applications. This choice not only allows us to simplify the development process by minimizing the maintenance cost and testing efforts but it also ensures a high-quality user experience across different devices.

Overall, this tech stack provides an efficient, effective, and sustainable way to meet our project goals and challenges. It leverages the strengths and expertise of our team members while taking into account the needs and expectations of our target users. We are confident that by utilizing Python for model development and Flutter for mobile UI, we can deliver a top-notch product that meets the highest standards of quality and innovation.

### Anticipating Future Problems:
During the project development and deployment phases, we anticipate a few potential challenges and obstacles that could arise:

1. Technical complexities - As our model may be big and slow, it may take a lot of time and resources to train and evaluate it. This can affect the overall performance and scalability of our application. Additionally, integrating a complex model with the mobile application UI can be technically challenging and may require significant modifications to the existing codebase.

Mitigation strategy: To address these challenges, we will consider optimizing our model by reducing its size and improving its processing speed. We may also explore using pre-trained models or, in the worst case we plan to use cloud-based services (because the main point is to remain autonomus) to offload some of the computational workload. Furthermore, we can break down the integration process into smaller, manageable tasks that can be implemented incrementally and tested thoroughly.

2. External dependencies - Our project may depend on external factors such as third-party APIs, data sources, or platform-specific requirements. Any changes or disruptions in these dependencies can impact the functionality and reliability of our application.
Mitigation strategy: To mitigate these risks, we will ensure that we use reliable and trustworthy APIs and data sources that have sufficient documentation and support. We will also have fallback plans in place in case of any disruptions or changes in these dependencies. Additionally, we can test our application on multiple platforms and devices to identify and address any compatibility issues before the final release.

Overall, by anticipating these potential challenges and proposing appropriate mitigation strategies, we can minimize the risks and uncertainties associated with the project development and deployment phases. We can also ensure that our team is prepared to tackle any issues that may arise during the process and deliver a successful product that meets the needs and expectations of our users.

### Elaborate Explanations:
The core functionality of our application lies in its image processing and classification capabilities. By taking advantage of state-of-the-art machine learning techniques, we are able to achieve high levels of accuracy and speed, making the process of identifying chemical compounds as seamless as possible. Our mobile application has an intuitive user interface that makes it easy for anyone to use, regardless of technical background.

One of the unique aspects of our solution compared to existing alternatives is its broad scope. Unlike other applications that are specific to organic compounds or have limited functionality, ours is designed to work with any type of molecule. Additionally, our application uses innovative techniques such as deep learning and image processing to provide accurate results quickly and efficiently. We believe that our solution will revolutionize the way people think about chemistry and make it accessible to a wider audience.

{{< hint danger >}}
**Feedback**  
I think this is a wonderful project that can benefit a lot of professional chemists and students. Conversion of complicated graphical representations into name of the compound is an interesting technical project that involves a lot of different technologies. 

Overall, your report effectively presents a problem-solution approach and conveys the potential impact and benefits of the proposed mobile application. It would be valuable to further elaborate on the implementation plan, including the technology stack, development roadmap, and potential challenges to be addressed. 

{{< /hint >}}

# **Week #2 Progress report**
## **Tech Stack Selection**

We have already chosen our tech stack on week 1 and decided to keep it.

## **Architecture Design**

1. **Component Breakdown**: There are two basic components: UI and AI, which interact in a request-response manner. The UI requests to analyze a taken photo, and the AI responds with the detected SMILES/InChl/IUPAC notations.

2. **Data Management**: The UI module is supposed to store some user settings, which will be stored using *Hive*. We don't need any database for the AI component as it is self-sufficient.

3. **User Interface (UI) Design**:

There wil be two basic screens:

### Shot screen
![](https://i.ibb.co/GMQz5xL/shot.png)

### Analysis result screen
![](https://i.ibb.co/ZB2wtm7/res.png)

4. **Integration and APIs**: Our application is designed to be fully autonomous, so we will not use any external APIs.

5. **Scalability and Performance**: There is no scaling problem at all since each application is complete and does not require external resources, so there is nothing to scale. Also we will pay more attention to performance since we are working on mobile app without separated backend.

6. **Security and Privacy**: Since the application is designed to be ready-to-use out of the box without any registration, we have no private data to store anywhere.

7. **Error Handling and Resilience**: We plan to use Firebase Crashlytics to handle application crashes for further analysis and fixes.

8. **Deployment and DevOps**: We plan to use CI/CD to automatically build and deploy new application versions to all distribution platforms, as well as registering new Crashlytics handlers for it on the push into the `main` branch. We will use the `dev` branch for application development.

## **Week 2 questionnaire:**  

1) Tech Stack Resources: We are already familiar with our tech stack so we do not use any books on it.

2) Mentorship Support: We are not seeking a mentor for our project.

3) Exploring Alternative Resources: We are going to use official documentation on Flutter, Python and Pytorch.

4) Identifying Knowledge Gaps: We have no knowledge gaps related to our tech stack. See our team allocation below.

5) Engaging with the Tech Community: We have not engaged with tech community and do not plan to do so.

6) Learning Objectives: We did not set any specific learning objectives.

7) Sharing Knowledge with Peers: We did not organized any knowledge-sharing sessions or discussions, since we do not have teammates unfamiliar with our tech stack.

8) Compensating Lacking Expertise with AI: As mentioned above, we are already familiar with our tech stack, so we did not compensate for any lacking expertise in our tech stack.


## **Tech Stack and Team Allocation**


| Team Member        | Responsibilities | Tech Stack |
|--------------------|------------------|------------|
| Evgenij Ivankin    | AI               | Pytorch    |
| Vitaly Mahonin     | Mobile App       | Flutter    |
| Timolai Andrievich | AI               | Pytorch    |

{{< hint danger >}}
**Feedback**
Overall, the progress report is very short and do not describe your group progress very well. It is good that you feel confident in your tech stack, but it will also be wonderful to see a more detailed description of the work done. If you think this is an easy project and that you and your team knows exactly how it needs to be build, consider adding some features that you haven't implemented before. You may take an opportunity to learn new things and have fun while you building this app.
  
Some specific comments - this project report say that main goal of the app is doing image processing and classification, but no details on the model, ML architecture and data is provided. To mee it seems rather strange, because the main part of this project is the model. Are you taking the open-source model or training your own? Are the pictures provided from the app that you already build or this is a mockup of the app? This report raised more questions than it provides answers, so make sure to provide more details on your next week progress report. 3/5 
{{< /hint >}}


# **Week #3 Progress report**
## **Technical Infrastructure**
We set up our development environments (IDE, linters, project building) locally. Also, we made it possible to work together by creating GitHub repositories.
We are planning to handle work on AI model with our own computational resources (like our personal GPUs in our computers) and utilizing free quotas of services like Kaggle and Google Colab.

## **Frontend Development**
This week, we implemented the first-priority task which was image retrieval.

To achieve this, we used two screens for two image sources: **camera** and **gallery**. Additionally, an in-app cut interface was implemented for both camera source and gallery source.

### Current State Showcase
[Video](https://disk.yandex.ru/i/UDfn8_ZnaLrfUw)

### Repository

The whole frontend is developing in [this](https://github.com/Senopiece/compound_scanner/tree/v0.0.1) repository from now and for the future posts.

### Release

You can touch the application yourself installing apk from [this](https://github.com/Senopiece/compound_scanner/releases/tag/v0.0.1) release.

All further versions would be published on [this](https://github.com/Senopiece/compound_scanner/releases) page.

### Further development

Although we have taken the first steps, we still need to develop the ML model separately and integrate it into the frontend at a later stage.

Currently, the frontend is experiencing some performance issues, bugs, and unhandled UX scenarios. For instance, when the application fails to find a camera, it crashes without providing any feedback to the user.

Further development plan:
1. add crashanalytics
2. complete resulting page
3. complete crop box for gallery screen
 > on this screen crop box must also be draggable, not only scalable
4. cover all the branching paths
 > no camera / invalid image from gallery / etc...
5. fix bugs
 > crop box can have negative scales / flashlight button is sometimes glitchy / etc...
6. add model
7. optimize
8. improve appearance
  - styles
  - icon
  - splash icon
  - proper naming
9. add animations


## **Backend Development**
Firstly, we studied most common chemical notations and decided to use [InChI](https://en.wikipedia.org/wiki/International_Chemical_Identifier) because it provides one-to-one mapping to the compounds unlike (for example) SMILES does. 
Secondly, we researched available AI model architectures to apply in our project. We decided to use the following structure: CNN Encoder -> Decoder with attention. We will use EfficientNet-v2 as our encoder because it shows good results in similar tasks and can fit in devices like mobile phones.

### Further development
1. Make dataset for training. We will use samples from public datasets with printed formulas like [BMS dataset from Kaggle](https://www.kaggle.com/competitions/bms-molecular-translation/data) and [Image2SMILES](https://zenodo.org/record/5356500). Also, we are planning to add some handwritten examples either by making them by ourselves or finding a public dataset.
2. Train the model.
3. Validate the model.
4. Integration with frontend (mobile app).

## **Data management**
We are not planning to have database in our MVP, but considering adding it for some extra features. For example, a local (since we are focusing on making app work offline) database of IUPAC names of compounds.

## **Prototype Testing**

### Frontend
Initial rounds of testing have been conducted for the frontend component. Currently, only integration tests are available as there are no widget or unit tests in place.

This week, a manual test was performed on the frontend prototype which resulted in the discovery of some bugs mentioned above. However, all identified issues were addressed and there were no usability concerns found.

## **Team Communication**

To ensure that our frontend and backend are in sync, our team has conducted several meetings. During these meetings, we discussed the initial plan in detail, including error codes and the general AI API.


# **Week #4 Progress report**

## Feedback

We gathered feedback from our chemistry student friends who had the opportunity to use our mobile
application.
They noticed that the app had a raw appearance and lacked the ability to translate into other
chemical notations, particularly the IUPAC nomenclature.
We will work on improving the user interface (UI)
and incorporating conversion to other notations using
libraries like [RDKit](https://www.rdkit.org/docs/index.html)
and [OpenEye](https://docs.eyesopen.com/).

## Testing
We validated our neural network using a test dataset.
Additionally, we specifically examined cases involving images
with multiple formulas, images without formulas, and handwritten formulas.
Overall, the model performed well, but it had some issues with handling specific cases.
We plan to fine-tune the model and possibly develop another model specifically
for formula detection in images, which can work in conjunction with the existing one.

## Iteration

We trained our model on the BMS dataset that we mentioned in previous week and fixed various bugs in
the application. The iterative process allowed us to make improvements and enhancements based on the
feedback and testing results, ensuring a more refined and reliable product.

During this week, we prioritized gathering external feedback, testing our prototype, and iterating
on the project. By involving chemistry students, we gained valuable insights into the app's
usability and identified areas for improvement. Testing helped us evaluate the effectiveness and
reliability of our neural network, and we discovered the need for additional fine-tuning and a
separate model for formula detection on images. The iterative approach allowed us to refine our
design, features, and functionalities based on the feedback and testing results, ensuring a product
that aligns with our initial vision.


{{< hint danger >}}

**Feedback by Rustam**  
Week 3 - Looks good, keep up the good work and I am sure you will finish with the nice and neat prototype!
Week 4 - only one student? This is not nearly enough.
Overall, somewhat dry reports and not very impressive progress on the project.
4/5 for the week 3
3/5 week 4
{{< /hint >}}

## **Week #5 Progress report**

During the previous week, we actively sought feedback from 10 chemistry students to gather valuable
insights and understand their needs better. As we delved into the feedback, we realized that we had
somewhat underestimated the complexity of porting our AI model to the mobile platform. However, we
approached this challenge head-on during this week, dedicating our efforts to fixing the problems
and implementing the features that were highlighted in the previous week's feedback. Additionally,
our primary objective was to successfully port the AI model to mobile while ensuring optimal
performance and user experience.

Considering the substantial progress we made in addressing the feedback, we didn't find it necessary
to gather another wave of feedback this time. Nevertheless, we are proud to announce that we were
able to implement about 50% of the crucial features proposed by feedback, indicating the successful incorporation of
valuable improvements. This achievement, however, means that we still have an ample amount of work
to accomplish in the upcoming week to ensure the application meets the expectations of our users.

### Implementing necessary changes or enhancements

This week was entirely dedicated to the meticulous implementation of a significant feature that
significantly enhances our application—a standalone AI capability. Recognizing the potential impact
it can have, our team members invested a considerable amount of time and effort, approximately 40
hours each, for a total of five days. Our primary focus was on effectively porting the AI model to
the mobile platform while taking into account the constraints and challenges inherent to mobile
devices.

To ensure a seamless integration, we engaged in extensive experimentation with various models,
configurations, and tech stacks. One notable task we accomplished was the conversion of our AI model
from PyTorch to TensorFlow. This transition was motivated by the fact that TensorFlow Lite (TFLite)
offers superior support and optimization for mobile devices compared to PyTorch Lite (PTLite).
Through meticulous testing and analysis, we verified that TFLite was better suited for our needs and
would deliver optimal performance on mobile.

During the conversion process, we encountered a roadblock when we discovered internal bugs within
PTLite that were affecting the functionality of our model. To resolve this, we dedicated a full day
to investigating the issue and ensuring that the problem was not due to any shortcomings on our end.
Through thorough debugging and collaboration with the framework's developers, we were able to
identify and address the internal bugs, ultimately ensuring the smooth functioning of our AI model
on the mobile platform.

Despite the challenges we encountered along the way, we are pleased to share that by the end of this
week, we successfully integrated the AI model into our application, marking a significant milestone
in our development journey. However, it is important to note that this task consumed the entirety of
our focus and efforts throughout the week, underlining the dedication, problem-solving skills, and
commitment of our team members.

As we look forward to the upcoming week, we acknowledge that there is still plenty of work to be
done. With the major feature of the AI model successfully implemented, we will now shift our
attention to other necessary changes and enhancements identified in the feedback. Our goal is to
ensure a seamless user experience, robust functionality, and the delivery of a truly valuable tool
for chemistry students.


{{< hint danger >}}
The report is good. And noted the PDF on top - good. 5 for the week. Good work! Good luck with project and final presentation!
{{< /hint >}}