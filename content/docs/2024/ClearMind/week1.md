---
title: "Week #1"
---

# Week #1

## **Presentation**
{{< embed-pdf url="/2024/ClearMind/clearmind.pdf" >}}
## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Sergei Polin (Lead)     | @vilfer | s.polin@innopolis.university |
| Eleonora Pikalo            | @elpi_tg | e.pikalo@innopolis.university |
| Alexandra Egorova            | @kurkune | a.egorova@innopolis.university |
| Mikita Drazdou            | @droz_nik | m.drazdou@innopolis.university |
| Iakov Saparov            | @outrun32 | i.saparov@innopolis.university |
| Natalia Agapova | @nhefy | n.agapova@innopolis.university |
| Anastasiia Ankudinova | @solncemy | a.ankudinova@innopolis.university |

### **Value Proposition**

#### **Problem**:
Many people struggle to get professional care for mental health conditions like stress, anxiety, and depression. There are many criteria why people don’t go to therapy with professionals, such as shyness, unwillingness to disclose, geographical location, time of day, etc. The main problem is that not everyone is ready to disclose their experiences and mental health problems to stranger.  We want to offer a solution for such people, when they can get qualified and diverse first aid from a psychologist at any time of the day in a short period of time. 

#### **Solution**
The AI-Psychologist is a mental health solution that leverages artificial intelligence to provide psychological support. This platform has the ability to communicate with a virtual psychologist through text and voice messages. 
The AI has main features:
 1. 24/7 access: The user can get mental help at any time, despite a human psychologist can’t get this ability.
 2. Voice message integration: The user can express the problem using a voice message, which makes it easier
 3. Anonymity and privacy: User doesn’t have to worry about their data, since the platform provides complete anonymity.
 4. Individual approach: AI can get the advises based on user messages and individual needs.

#### **Benefits to Users**
 1. Greater accessibility: By being accessible at all times and locations, the AI-Psychologist helps people who might not otherwise seek mental health treatment by removing barriers to it.
 2. Cost-effective: It offers a less expensive substitute for conventional therapy, enabling a larger population to get mental health care.
 3. Immediate support: Instead of waiting for a scheduled treatment session, users can get help and responses right away when they need it.
 4. Enhanced engagement: By enabling more dynamic and captivating interactions, the audio message feature can raise user satisfaction.
 5. Comfort and Privacy: Being able to stay anonymous.
 6. Personalization: Personalized reactions and advises.

#### **Differentiation**
We provide a free website for people who need psychological help. Our service works as a mental first aid kit, not as a long term psychological help. We also never assign diagnosis, we can only give advice to our users. Our service is absolutely free for everyone, so people from different social groups can use it.

#### **User Impact**
Using our service can help calm down in stressful situations, and as a result users may become less agressive and anxious about their life situations. Also, our website can help people realise their feelings and problems to later discuss them with a certified therapist.

#### **User Testimonials or Use Cases**
Our website can be used during anxiety and panic attacks, when a person may need urgent help. It also can be used for some quick advice situations, for example, when someone feels stressed out, sad, lonely or discouraged. Our service can also help analyze one’s feelings and figure out what they may mean. Our service is not supposed to give diagnosis or help in deep situations such as depression, trauma or other mental illnesses.

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. **What problem or need does your software project address?** 
   
   Our software project addresses the significant challenge faced by introverts and individuals with social anxiety who find it difficult or uncomfortable to talk to a human therapist about their personal problems. Traditional therapy sessions often require verbal communication and face-to-face interactions, which can be overwhelming and stressful for introverts. As a result, these individuals might avoid seeking the help they need, leading to unresolved mental health issues.

2. **Who are your target users or customers?**

   Our target users are introverts and individuals who require immediate mental health support but are uncomfortable seeking help from human therapists. Our primary customers are the heads of universities and schools, who are responsible for student well-being and are interested in implementing innovative mental health solutions to support their students.

3. **How will you validate and test your assumptions about the project?**

   We will validate and test our assumptions by conducting a pre- and post-intervention emotional assessment with a group of test participants. Initially, participants will complete a survey measuring their current emotional state. They will then engage with our AI psychologist for some time. After the interaction, we will administer the same emotional assessment to get any changes in their emotional well-being. Comparing the pre- and post-intervention results will help us determine the effectiveness and impact of our AI psychologist.

4. **What metrics will you use to measure the success of your project?**

   We will use the following metrics to measure the success of our project:
   - User Engagement: The number of active users and the frequency of their interactions with the AI.
   - User Satisfaction: Feedback collected through post-interaction surveys.
   - Emotional Impact: Changes in participants' emotional well-being as measured by pre- and post-intervention assessments.
   - Retention Rate: The percentage of users who continue to use the service over a specified period.
   - Referral Rate: The number of users who recommend the service to others.

5. **How do you plan to iterate and pivot if necessary based on user feedback?**

   We plan to iterate and pivot based on user feedback through the following steps:
   - Collect Feedback: Regularly gather feedback from users via surveys, in-app feedback forms, and user interviews.
   - Analyze Data: Continuously analyze the feedback and usage data to identify patterns and areas for improvement.
   - Implement Changes: Make necessary adjustments to the AI's responses, user interface, and overall functionality based on the feedback.
   - Test Updates: Conduct beta tests with a small group of users to ensure the changes positively impact the user experience.
   - Repeat: Continuously repeat this process to refine and improve the service, ensuring it meets users' evolving needs and expectations.

## **Leveraging AI, Open-Source, and Experts**

1. AI Integration: We’re using some amazing tech like GPT-4O and LangChain to create smart, personalized responses. Whisper is in the mix too, making sure we get speech recognition right so our interactions are smooth and easy.

2. Open source technologies: We love open source! It makes our platform strong, scalable and transparent. It also allows us to integrate with different services and take advantage of the global technology community. We will be actively using the Diffusers library, which will allow us to have broad access to AI technologies.

3. Expert Collaboration: While we don’t have psychology majors, we’ve got Daria Kostyunina, a pro at supporting students, on our side. She helps us make ClearMind super helpful for younger users and anyone looking for some initial mental health support.

## **Defining the Vision for Your Project**

### **Overview** 
ClearMind aims to be the go-to AI psychologist for those who find it hard to trust others with their mental health concerns. Our vision is to create an accessible, user-friendly platform that offers immediate, empathetic, and personalized support to individuals in need. We aim to provide a reliable first step for people seeking mental health assistance.

### **Schematic Drawings** 
![Schematic](/2024/ClearMind/schema.png)

### **Tech Stack** 
Next.js for the frontend, Tailwind CSS for styling, PyTorch for machine learning, LangChain for natural language processing, Diffusers for calling AI models, and FastAPI for the backend.
