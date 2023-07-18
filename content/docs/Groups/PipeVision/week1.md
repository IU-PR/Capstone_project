---
weight: 1
bookFlatSection: true
title: "Week 1 report"
---

# **Week #1**

### **Team Members**

| Team Member              | Telegram ID          | Email Address                      |
| ------------------------ | -------------------- | ---------------------------------- |
| Team Member (Lead) 1     | @a_n_a_s_t_a_s_i_a10 | a.barabanova@innopolis.university  |
| Team Member 2            | @mintnova            | a.smirnova@innopolis.university    |
| Team Member 3            | @amirlansharipov     | a.sharipov@innopolis.university    |
| Team Member 4            | @EveryoneHATEme      | y.dementyev@innopolis.university   |
| Team Member 5            | @Guzel_Zakirova      | guz.zakirova@innopolis.university  |
| (Optional) Team Member 6 | @sundariam           | d.merzakreeva@innopolis.university |
| (Optional) Team Member 7 | @shredding8          | e.zavrazhnov@innopolis.university  |

### **Value Proposition**

- The problem:
  Companies in the pipeline construction and maintenance sector frequently struggle to rapidly and precisely identify the marks of metal and pipeline components from digital images. This job involves a lot of manual effort and is prone to human error, which can result in expensive errors and safety concerns.

- Solution Description:
  We propose a unique approach to this problem, a system that leverages machine learning algorithms to automatically recognize the markings of pipeline and metal components based on their photo images. The system not only eliminates the need for manual input but also significantly reduces the chances of errors.

- Benefits to Users:
  Our software provides several key benefits. First, it increases the speed of marking recognition, allowing workers to complete their tasks more efficiently. Second, it reduces the likelihood of recognition errors, which helps to increase accuracy in pipeline and metal construction and maintenance. As a result, productivity is enhanced, and the likelihood of costly mistakes or safety issues is reduced.

- Differentiation:
  We did not find any similar projects in open sources. Anyway, here are selling points for our solution. Our system integrates with a database to store and retrieve the recognition results, which makes it a more comprehensive solution. Also, the solution has user-friendly interface that is appropriate to the customer.

- User Impact:
  With this automated pipeline marking recognition system, professionals can significantly reduce the time and effort spent on manual and error-prone recognition tasks. This automation leads to higher productivity and cost savings.
  Furthermore, the increased accuracy provided by our software reduces the risk of incorrect identification of pipeline markings, which could potentially lead to costly or even dangerous mistakes in pipeline construction or maintenance. Thus, our solution not only improves efficiency but also enhances safety in the industry.

- User Testimonials or Use Cases:
  At this early stage of the project, we might not have real-world examples or user testimonials. But there are hypothetical use cases based on our understanding of the industry and the problem we’re addressing: - A pipeline construction company used our software to automatically recognize and catalog the markings on their pipeline components. They reported a 50% reduction in the time spent on these tasks, along with a significant decrease in recognition errors. This improvement allowed them to speed up their construction projects and reduce costs associated with errors. - A pipeline maintenance company uses our software to quickly identify pipeline components that need to be replaced or repaired, improving the speed and efficiency of their maintenance operations.

## **Lean Startup Questionnaire**

1. What problem or need does your software project address?
2. Who are your target users or customers?
3. How will you validate and test your assumptions about the project?
4. What metrics will you use to measure the success of your project?
5. How do you plan to iterate and pivot if necessary based on user feedback?

### Answers

1. Our software project addresses the need for an efficient and accurate method of recognizing the markings of pipeline and metal elements based on their photo images. The current manual process is time-consuming, error-prone, and inefficient, which can lead to costly errors and safety issues in pipeline construction and maintenance.
2. Our target users are professionals in the pipeline construction and maintenance industry, working for Gazstroyprom. These workers need to accurately recognize pipeline markings to ensure the correct use of pipeline elements and to maintain safety standards.
3. We plan to validate and test our assumptions about the project through a combination of user testing and data validation. We will collect feedback from the company and test our software on real-world data sets to ensure its accuracy and effectiveness.
4. To measure the success of our project, we will use metrics such as the speed and accuracy of mark recognition, user satisfaction, and the reduction in time and errors in pipeline marking recognition tasks.
5. We will use the feedback we gather from users to iterate on our software. If necessary, we may pivot our approach based on this feedback. For example, if users find certain features difficult to use or ineffective, we will look into refining or replacing these features.

## **Leveraging AI, Open-Source, and Experts**

- AI (Artificial Intelligence): Image recognition with neural networks.
- Open-Source: Leveraging open-source machine learning libraries, pretrained CV models and frameworks for the system development.
- Experts in relevant domains: two master students with knowledge in CV and project management.

## **Inviting Other Students**

We have already formed a team of seven people from our course. Nevertheless, we are open for collabarations with other students, who are more expereinced, to create better solution.

## **Defining the Vision for Your Project**

- Overview:
  The project aims to develop an automated pipeline marking recognition system based on a neural network. The system addresses the challenge of manual pipeline and metal marking recognition, which is time-consuming, error-prone, and inefficient. Our solution provides automated, fast, and accurate recognition, enhancing productivity, reducing errors, and potentially improving safety in the pipeline construction and maintenance industry.

- Schematic Drawings:
  ![Schematic drawing](/PipeVision/schematicDrawing.png "Schema").

- Tech Stack:
  The backend of the application will be developed using Python: OpenCV for computer vision, FastAPI for communication with frontend, SQLAlchemy for database integration. The frontend will be built using TypeScript with React framework because of its efficiency and flexibility. PostgreSQL will serve as the database management system due to its robustness and excellent performance. The neural network will be based on PARSeq-SA model, which is an efficient and effective model with 91.9% accuracy.

- Anticipating Future Problems:
  Obtaining sufficient high-quality data to train the neural network, ensuring the database system can efficiently respond on requests, and ensuring the recognition accuracy is high enough to be useful in a real-world setting. Strategies to address these challenges could include data augmentation techniques, using a scalable backend framework, and continually improving and updating the neural network model based on its accuracy and new data.

- Elaborate Explanations:
  Our application can be divided into four main components: the frontend interface, the backend server, the database, and the neural network. 1. The frontend interface allows users to upload images and view recognition results. It communicates with the backend server to send and receive data. 2. The backend server handles requests from the frontend, processes images using the trained neural network, stores results in the database, and sends results back to the frontend. 3. The PostgreSQL database keeps track of recognition results, allowing users to view past results and providing a source of data for further improvement of the neural network. 4. The neural network is the heart of our system, responsible for recognizing pipeline markings in the images.

{{< hint danger >}}
**Feedback**

I would say your report is strong in technical aspects but weak on business aspects

3/5

_Feedback by Moofiy_
{{< /hint >}}
