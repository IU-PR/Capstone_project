---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:
As of now, we are still working on stable technical infrastructure. Every team member is working on his own subtask (in most cases every other subtask has its own technological stack). However, some problems may occur when we "connect" our models into a complete pipeline.
For example, different open source models use different version libraries. This may cause severe errors in the work of our application.

- **Backend Development**:

   ML part:
    * Stable Diffusion V1.5 + TensoRF
    TensoRF generates scene based on set of images of specific object from different angles. However, techniques that allow the creation of a scene without initial image(s) exist. TensoRF "не завелся". To calculate the value of loss-function, TensoRF require an image of an object from a specific angle. While generating such images we do not give any foreshortenings as a parameter, but we need to determine an angle without any information given. Since it is difficult to perform such an operation precisely, the model cannot update its weights in a proper way.

    * Stable Diffusion V1.5 + SyncDreamer + TensoRF
    To solve the problem about accurate determination of requred angles, we used MultiView Diffusion models. Using SyncDreamer we were able to generate 16 forshortenings. We knew the exact position and angles of needed view. However, it was also necessary to convert all these into a rotation matrices. We did not figure out how to properly convert necessary information about views into a rotation matrices. Thus, such "issue" made the training process of the models difficult for us to implement due to our insufficient knowledge.

    * Stable Diffusion V1.5 + Wonder3D + NeRF
    Unlike SyncDreamer, Wonder3D model gave us an ability to generate new views with the properly initialized rotation matrices. That is why we decided to work using this approach. We already generated 2 3D models. You can see one of them here:
![Girl_1](/static/2024/OmniShaper/Girl_1.gif)

   Web part:
    * Unfortunately, we did not manage complete the web backend due to unfinished ML part of our backend.
    Without working AI pipeline, there will be no working backend for our web application. As you know, the ML part is the hardest to implement. We will finish the first prototype (something like MVP) before the next meeting with our TA.

- **Frontend Development**:

...

- **Data Management**:

...

- **Prototype Testing**:
We did not build our AI pipeline yet (all models are not connected yet). However, we tested the whole system without a proper interface set up:
    * Firstly, we passed the prompt to a LLM model:
    "house";
    * Secondly, LLM model generated a new prompt for a Diffusion model:
    "mansion house, two-storey house, country living, English countryside, small cottage, modern house, large house, family home";
    * Thirdly, we pass the modified prompt to a Diffusion model, that generates the following image:
![House_1_img](/static/2024/OmniShaper/House_1.png)

    * Fourthly, we pass the image to Wonder3D to get the set of images of and object from different angles:
![House_1_img](/static/2024/OmniShaper/House_1_collage.png)
    
    * Lastly, we pass all the images into NeRF and get the final version of our 3D model:
![House_1](/static/2024/OmniShaper/House_1.gif)

## **Weekly Progress Report**:

Our team developed working yet not finished (connected) AI pipeline. All functions work correctly, but everything is not "automated" yet. We are working on it and planning to finish it in the couple of days.

### **Challenges & Solutions**
The hardest challenge was to test and implement the working idea (out of 3) and get the first results.
Another difficult challenge is to find suitable open source models for each of the pipeline. 
And "prompt-engineering", of course...

### **Conclusions & Next Steps**
On the next week we are planning to completely finish our AI pipeline, convert currently existing solution into a working prototype, and set up a correct UI/UX design for the web application.
