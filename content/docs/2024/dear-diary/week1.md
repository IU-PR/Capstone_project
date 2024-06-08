## **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Alyona Maksimova (Lead)  | @acode113 | a.maksimova@innopolis.university |
| Elizaveta Nikolaeva            | @nikolaevalizza | e.nikolaeva@innopolis.university |
| Kristina Bondarenko            | @ohibloom | k.bondarenko@innopolis.university |
| Andrew Levada            | @andrewlevada | a.levada@innopolis.university |


## **The value proposition**

### **Problem**
Traditional self-help tools are often ineffective because they rely on generic templates that do not cater to individual needs. Users face challenges and inefficiencies due to the lack of personalized support and feedback.

### **Solution Description**
Our solution offers a personalized AI-driven self-help tool that evolves and thinks alongside the user. It is designed to provide customized support and feedback, adapting to individual needs and circumstances. This approach ensures that users receive relevant and effective guidance tailored to their unique situations.

### **Benefits to Users**
- **Resource Efficiency:** Users save time and effort by receiving personalized guidance without needing to sift through generic advice.
- **Accessibility:** Available anytime, offering immediate support whenever needed.
- **Privacy:** Users can explore and address their issues privately, without the need to involve others.

### **Differentiation**
Our tool stands out because it provides continuous, personalized feedback, unlike other solutions that offer static, one-size-fits-all advice. This dynamic interaction helps users achieve better results and a deeper understanding of their emotions and behaviors.

### **User Impact**
By using our tool, users gain greater self-awareness and are better equipped to handle complex emotions. This leads to improved overall well-being and mental health, helping them navigate life's challenges more effectively.

### **User Testimonials and Use Cases**
- **Ahmet, a Programmer:** Feeling overwhelmed at work, Ahmet uses our app instead of venting his frustrations on loved ones. This helps him manage stress more constructively.
- **Aida, a Student:** Facing exam anxiety, Aida loses motivation. Our app helps her understand the importance of her studies for her future, helping her regain focus and motivation.
- **John, a Bank Worker:** John uses our app to better understand people and improve emotional intelligence, enhancing customer interactions and personal relationships.
- **Sara, a Teacher:** Sara uses our app to enhance her personal growth and emotional well-being, making her more effective and empathetic in her teaching career.

These examples illustrate how our personalized self-help tool can significantly improve users' lives by providing timely, relevant, and private support.

## **Short Value Proposition:**
Our AI-driven self-help tool helps individuals who want personalized guidance to manage their emotions and improve their mental health by providing customized recommendations and real-time feedback. Unlike traditional self-help methods that rely on generic templates, our solution leverages AI to offer tailored support and continuous adaptation to the user's needs.


## **Lean Questionnaire**

**1. What problem or need does your software project address?**

Our software project addresses the ineffectiveness of traditional self-help tools, which often rely on generic templates and fail to provide personalized support. Users need a solution that offers customized guidance and feedback to help them manage their emotions and mental health effectively.

**2. Who are your target users or customers?**

Our target users include:

- Anyone seeking personalized mental health support to navigate daily challenges and improve their overall well-being.
- Individuals looking for self-improvement tools to enhance their personal growth and emotional intelligence.

**3. How will you validate and test your assumptions about the project?**

- Conducting user interviews and surveys to understand their needs and pain points.
- Analyzing existing solutions and identifying their shortcomings.
- Conducting usability testing sessions with prototypes to assess user interaction and gather feedback.

**4. What metrics will you use to measure the success of your project?**

- **User engagement:** Tracking daily and weekly active users.
- **Retention rates:** Monitoring how many users continue to use the app over time.
- **User satisfaction:** Collecting user feedback through surveys and reviews.
- **Improvement in well-being:** Measuring changes in users’ reported stress levels and emotional well-being before and after using the app.
- **Feature usage:** Analyzing which features are most frequently used and most beneficial to users.

**5. How do you plan to iterate and pivot if necessary based on user feedback?**

- Regularly collecting and analyzing user feedback.
- Implementing changes and improvements based on user suggestions and pain points.
- Conducting A/B testing to determine the most effective features and functionalities.
- Being flexible and open to making significant changes to our approach if initial assumptions prove incorrect or if user needs evolve.

## **Leveraging AI, Open-Source, and Experts**

To enhance our project, we will:
- leverage AI for personalized recommendations and real-time feedback.
- utilize open-source technologies to accelerate development and reduce costs.
- collaborate with mental health experts to ensure the accuracy and effectiveness of our guidance, ensuring our tool provides the highest quality support for our users.

## **Defining the Vision for Your Project**

### **Overview:**

"Dear Diary" aims to provide personalized mental health support and self-improvement tools to users facing daily challenges and seeking to enhance their overall well-being. The platform will offer customized guidance and feedback, addressing the inefficiencies of traditional self-help methods by adapting to individual needs and circumstances. By leveraging AI-driven algorithms, users will receive tailored recommendations and real-time assistance, empowering them to manage their emotions effectively and improve their mental health.

The primary problem our project addresses is the lack of personalized support in existing self-help tools, which often provide generic advice that may not resonate with individual users. By offering customized guidance, our platform seeks to enhance user engagement and satisfaction, leading to better outcomes in managing stress, anxiety, and other emotional challenges. The intended benefits include increased self-awareness, improved coping strategies, and overall enhanced well-being for our users.

### **Schematic Drawings:**
Interactions within the system:

{{<mermaid>}}
graph TD;
    subgraph "Device"
        iOS_App
        Local_Data_Storage
    end
    subgraph "Serverless Provider"
        ML_API
    end
    iOS_App --> Local_Data_Storage
    iOS_App -->|API Request| ML_API
    ML_API -->|API Response| iOS_App
{{</mermaid>}}


### **Tech Stack:**

**Backend:** Python will be used for backend development, and the specific framework will be chosen at a later stage based on project requirements and team expertise. This flexibility allows us to select the most suitable framework that aligns with our project goals.

**Data Storage (Mobile):** CoreData will be used for local data storage within the iOS application, providing efficient and reliable storage and retrieval of user data on the device.

**Deployment:** We'll utilize TestFlight for beta testing and distributing pre-release versions of our iOS app to external testers, allowing for feedback and bug testing before the official release. This streamlined approach to deployment ensures efficient testing and validation of our application without the immediate need for cloud platform deployment.

**Design and Prototyping:** Figma will be utilized for designing and prototyping the user interface, allowing for collaborative design iterations and ensuring a seamless user experience.

**Mobile Development:** For iOS mobile development, we'll use Swift programming language and the iOS SDK to create a native mobile application. Swift will enable us to build high-performance, feature-rich applications optimized for iOS devices. We'll also utilize API integration to connect our iOS app with backend services for data retrieval and manipulation.