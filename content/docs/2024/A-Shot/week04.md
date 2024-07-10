
---
title: "Week #4"
---

# **Week #4**

## **External Feedback**


Over the past week, we made a concerted effort to collect valuable feedback from friends and colleagues about our
desktop application. To make the process efficient and respectful of everyone's time, we utilized Google Forms. This
form featured various rating options for different functionalities of our application, allowing users to rate each
feature on a scale of 1-10 and provide additional comments if they chose. You can find the form
[Here](https://forms.gle/M3eoJdfNbbahjobx9)

The feedback we received was incredibly insightful and highlighted several important issues that required prompt
attention. For example, one user noted that "The image preview delays noticeably when navigating between photos." We
addressed this issue after receiving the feedback. Another user mentioned, "...
too much space for sidebars or between folders and groups." Recognizing the significant impact this had on
user experience, we prioritized and going to fix this issue. Additionally, feedback regarding the UI provided us with
crucial insights that led to further enhancements.

In summary, gathering direct feedback from users has proven to be extremely valuable. It brought several key issues to
our attention and provided us with essential insights for future enhancements. We will ask users to test our
application once more, to see how the fixes of the application have improved or worsened the opinion
of our user in order to create the most User-friendly application

## Testing

We have tested our application according to the following criteria: performance, stability and load tolerance. Below is
a detailed assessment of each criterion:

- **Performance**:
  We evaluated the speed of basic operations and the responsiveness of the user interface. During this testing, we
  noticed that re-uploading photos takes an unexpectedly long time. The application processed these folders
  repeatedly each time, instead of recognizing and skipping the already processed data. To solve this problem, we
  are implementing a local database to store information about previously uploaded photos, which significantly
  reduced the download time for subsequent requests.

- **Stability**:
  Our stability assessment included conducting long usage sessions and monitoring failures. The application has
  demonstrated high stability under normal conditions of use with minimal failures, the causes of which have been
  identified and eliminated. Overall, the application has remained stable over a long period of use.

- **Load resistance**:
  We tested load resistance by uploading a significant number of images and monitoring the functionality of the
  application under maximum load conditions. Although the application as a whole maintained proper functionality
  without failures, we observed significant memory consumption when viewing large folders with photos, which led to
  a noticeable slowdown. Currently, this problem is being solved to improve the performance of the application under
  heavy loads.

The results of our testing have confirmed that although our application meets most of the specified requirements, there
are still areas that need improvement. In particular, optimizing memory usage when working with large folders and
increasing the speed of imports.

## Iteration and Refinement

### We are working on a **Agile** methodology, and now the third spring is underway.

![Agile](/2024/A-Shot/week04/agile/agile.png)

### First Sprint

The initial sprint focused on developing a prototype application.

1. **Planning Stage**: This phase involved brainstorming the primary tasks for the application, selecting tools, and
   distributing tasks for this sprint. Detailed information is available in the week 01 report.
2. **Design Stage**: The design phase was divided into three sections:
    - **Sketches**: Initial ideas about the application’s appearance were transferred to paper as sketches.
    - **Lo-Fi Prototype**: Based on the sketches, a Low-Fidelity prototype was created, outlining the user interface's
      skeleton and the main button positions.
    - **Hi-Fi Prototype**: Building on the Lo-Fi prototype and incorporating feedback, a clickable High-Fidelity
      prototype was developed. More details can be found in the week 2 report.
3. **Development Stage**: The first prototype of the application was created using Kotlin Multiplatform Compose,
   incorporating the main elements from the Hi-Fi prototype.
4. **Testing Phase**: During testing, the prototype's stability and ability to handle a large number of photos were
   evaluated. Bug fixes helped achieve the testing goals.
5. **Deployment Stage**: The prototype was published in the project repository on GitHub.
6. **Feedback Stage**: Feedback was gathered to improve the prototype.

### Second Sprint

The second sprint focused on developing photo grouping and blur detection models.

1. **Planning Stage**: This phase involved researching papers, articles, and existing models relevant to the task.
2. **Design Stage**: It was determined that the blur detection model could be used when importing photos from the user's
   local directory, while the photo grouping model would be beneficial within the application to sort photos for easier
   viewing.
3. **Development Stage**: This stage involved running models on our systems and making necessary adjustments.
4. **Testing Stage**: Models were tested on both training datasets and our own photos to evaluate their performance in
   real-life scenarios, focusing on accuracy, speed, and capacity to handle a large number of photos.
5. **Deployment Stage**: The models were integrated into the application using JNI (Java Native Interface) and ONNX
   Runtime.
6. **Feedback Stage**: It was confirmed that the blur detection model was successfully integrated into the application.
   The photo grouping model, although ready, required additional time for full integration. More details about models
   you may see in week 3 report

### Third Sprint

The ongoing third sprint aims to elevate the application to the MVP level, addressing the second issue identified in the
previous sprint.

1. **Planning Stage**: Key tasks, such as frontend development and model improvement, were outlined. An additional
   issue—enhancing import speed—was identified. To address this, the team decided to use the Room database to store
   information about processed photos.
2. **Design Stage**: User Interface improvements based on key things from the external feedback. You may see it in
   weekly progress report
4. **Development Stage**: Currently in progress, this phase involves frontend development and creating functions for the
   Room database.

At the feedback stage, the team plans to gather potential user opinions and conduct interviews to gain further insights
and ideas for product improvement.

## **Weekly Progress Report**

### **User Interface improvement**

As we mentioned before, we spend a lot of time to find and resolve issues in the UX/UI. External feedback also was
really helpful for this stage
Here you can see example of UI improvement, first screenshot old version and second new variant:

![First image](/2024/A-Shot/week04/UI-upd/old.jpg)
![Second image](/2024/A-Shot/week04/UI-upd/new.jpg)

As you can see on this example, we removed the large, awkward gaps of the sidebars. The selection box has also 
been converted to numbering with a color selector. Moreover, we have replaced the unnecessary demonstration of 
pictures in the group on the right sidebar with a neat slide bar



### **Database integration**

We have reviewed the process of interaction between the user and the application. Instead of blocking the entire 
interface for the duration of the download, we went the other way, with integrating database to our application.
This might allow us:

- To avoid repeated reimports 
- To update the interface as user import new photos

In addition, the database makes it easier and safer to communicate with data, which simplifies work and allows you 
to quickly and conveniently add functions such as sorting, grouping, etc.

We searched for solutions and chose Room database. We succesfully implemeted skelet database and additional classes with
functions. Still need to connect application with this skeleton, test and fix bugs.


### **Frontend Development**

We continued to develop the frontend of our application, meticulously enhancing it to address various UI issues and
improvements. This ongoing development process allowed us to refine the visual and interactive aspects of the interface,
ensuring a more seamless and engaging user experience. By implementing UI fixes and making strategic adjustments, we
have significantly elevated the overall design and functionality of our application’s frontend.

### **Challenges & Solutions**

- **Challenge 1: Analyze feedback and improve UI**  

  *Problem*: Users and we as contributors were not happy with the interface to a greater extent
  *Solution*: We brainstormed the issues, searched for interesting UI-solutions and make more user-friendly interface

### **Conclusions & Next Steps**


- **End Database Integration**: We still need work to end database integration and test it to resolve all issues.
- **End Frontend**: Some things are not included yet, so we need to finalize them to make the product look presentable
- **Beta-testing**: We want to contact more people, to give them access to the beta-test of our product. We will ask
  them to test and analyze functionality of the product and provide feedback. This way may give us more insights and
  help to identify any flaws
- **Multiplatform deploy**: In plans to adaptive the application to the Windows and MacOS to allow users who do not use
  Linux as the main system to use our application without problems 
- **Dark Theme**: As the instrument for the photographers, A-Shot in dark theme might be useful to a lot of people,
  because a dark theme may put less strain on the eyes in the evening or at night than a white one. Moreover, it is much
  more convenient for the human eye to look at photos on a dark background than on a light one. But for now, this feature
  not in the high priority.
- **Database finalizing**: We should solve challenges with database, test and deploy to the MVP stage. Challenges and
  solutions will appear in the week 5 report
