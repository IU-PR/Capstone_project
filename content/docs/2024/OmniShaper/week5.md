---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

- **Feedback collection plan**

We did not have a strict set of rules for a feedback collection process. We have prefered personal meetings (offline/online - depending on a person.) and showed them what we have for now and how we did it. During the meeting, one member from our team were taking a few notes about key points of customer's feedback.

- **Conducted user surveys or feedback sessions**

In total, 3 feedback sessions were taken. One of them included the student of an architecture university and another two - with the representatives of an bureau of Architecture. The mean duration of one interview - 30-50 minutes depending on the number of questions from interviewees.

- **Analyzing feedback, identifying and prioritizing issues**

The main takeaways from the interviews were:
1) Design - As of now, the design of the main page is not visually appealing for an ordinary user. It looks more like a website from 2010s;
2) The website looks "poor" - Right now, we only have one feature - text-to-3D generation. In order to make our product "pure", we have to consider adding more features to the main website;
3) The generated 3D models' quality do not meet customers' expectations - Due to early stages of development of generative AI in 3D modeling, ML models are not able to generate "stunning" 3D models. However, we are working on the improvement of our AI pipeline's generative capabilities;
4) Too much time is being spent on the process of generation - throughout a few weeks we achieved a significant improvement in terms of inference time. Initially, it took about 35-70 minutes for our AI pipeline to generate single 3D model. Right now, it takes only a few minutes. (Everything were run locally, on usual laptops)

## **Roadmap**:
You can see our roadmap in the image below:
![Roadmap](/static/2024/OmniShaper/roadmap.jpg)


## **Weekly Progress Report**:
1. Pipeline Division

Divided the project pipeline into two distinct parts:
- Text-to-Image Generation: Developed a mechanism to generate multiple images from a single text prompt.
- Image-to-3D Model Generation: Implemented a process to convert a selected image into a 3D model.

This division enhances the modularity of the system, making users to be able to select the image on which the 3d model will be generated. It provides a clear workflow for users to follow, improving the overall user experience. The pipeline division also making it easier to manage and debug each part separately.

2. API Updates

Updated the API to support two types of requests:
- Text Prompt to Images: Users can submit a text prompt along with the desired number of images to be generated. The API then returns the generated images.
- Image to 3D Model: Users can submit an image to receive the corresponding generated 3D model.

The new API structure provides flexibility and improves the functionality of the system.
It allows for a more streamlined process, ensuring that users can easily transition from generating images to creating 3D models.

3. Front-End Updates

Enhanced the front-end interface to allow users to select the image they wish to use for 3D model generation.

Improved user interface makes it easier for users to navigate through the generated images and select their preferred one.
Enhances user engagement and satisfaction by providing a more interactive and intuitive experience.

4. MicroDreamer Configuration

Updated the configuration of MicroDreamer, the component responsible for generating 3D models, to improve its performance and output quality.

The updated configuration results in better quality 3D models, with more accurate and detailed representations.

### **Challenges & Solutions**
Our main model - MicroDreamer - as of right now has problems with config file, as its meshes are quite inaccurate and lead to unsatisfying results. This problem, we think, can or might be resolved by adjusting config file to meet our needs, but this process is very accurate and needs a lot of testing. If the problem will persist, we will be forced to find another model that will generate 3d objects from images.

Transfering data from api backend to frontend was not as straightforward as it was expected. We needed to transfer our generated files straight to frontend as web responses for the frontend host not to mess with its permanent memory. Thankfully, there is an encoding and decoding (base64) algorithm, which we used, that does  the job fine.

But right now the main problem is in testing, as 3/7 PCs at best can fully run the project, hence we need to place the project on a server ASAP.

### **Conclusions & Next Steps**
Significant progress was made this week in the text-to-3D generation process. As a result of Stable Diffusion 3, the image quality has improved, and the user experience has become more convenient by providing customers with a choice of images for 3D generation. Users have provided feedback about their experience with the new features. We will incorporate this feedback into future improvements.

Key points:

• Probably it would be better for us if service was already deployed, because its exactly the point where we falling behind. We will take this lag as a lesson for the next iteration. 
• MicroDreamer does not yet give us sufficient quality for the generation, but we hope that we will find a way to improve it.

Next steps:
- Refine Website Design: Improve the aesthetics and user interface of the website to create a more polished and engaging experience.
- Integrate Firebase: Connect our service with Firebase for authentication and secure storage of generated 3D objects.
- Dockerize Project: Wrap our entire ML pipeline & API into a Docker image to simplify deployment.
- Set Up Inference VM: Establish a virtual machine dedicated to running the inference process for our model.
- Model Inference: Optimize and execute model inference on the dedicated virtual machine.
- Explore Stable Diffusion 3 for Multiview: Investigate using Stable Diffusion 3 for the multiview generation stage of MicroDreamer to potentially improve 3D model quality.
- Improve Generation Quality: Brainstorm and implement strategies to further enhance the quality and realism of the generated 3D models.
