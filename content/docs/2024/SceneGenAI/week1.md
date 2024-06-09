---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member          | Telegram ID   | Email Address                      |
| -------------------- | ------------- | ---------------------------------- |
| Bulat Akhmatov       | @bulatik1337  | b.akhmatov@innopolis.university    |
| Alexandra Vabnits    | @sashhhaka    | a.vabnits@innopolis.university     |
| Amir Nigmatullin     | @cheezy_on_me | am.nigmatullin@innopolis.university |
| Mintimer Karimov     | @JIeru0H      | m.karimov@innopolis.university     |
| Nurislam Zinnatullin | @zaurall      | n.zinnatullin@innopolis.university |
| Bahdan Shah          | @bodashkaxd   | b.shakh@innopolis.university       |
| Daniil Tiuftin       | @daniil_ktr   | d.tiuftin@innopolis.university     |

### **Value Proposition**

- **Identify the Problem**:  
   For users of [the Leroy Merlin website](https://leroymerlin.ru/) it is important to visualize products against relevant backgrounds to represent the scale of the products and how they look in a real environment.  
   **Current solution**: Leroy Merlin solves this problem by filming in a photo studio. For example, a vase is photographed against the background of the interior, a drill on a table in the workshop, and garden furniture against the background of a garden plot. Such filming is labor-intensive; it is necessary to organize the logistics of goods to the photo studio, and in the case of garden furniture, it is difficult to organize a place for filming in general. Sometimes, Leroy Merlin uses 3D rendering instead of a photo shoot, but this is also labor-intensive and expensive.
   **Proposed solution**: Generative neural networks can help solve this problem by generating backgrounds that match the product.

- **Solution Description**:  
   Using AI to create a service tool that integrates backgrounds into product images on the online shop. This tool will help clients to visualize product sizes in the environment they want, eliminating the need for extensive photoshoots or 3D rendering.

- **Benefits to Users**:   
   Users will benefit from a more immersive shopping experience and clear understanding of how products fit into their desired spaces. This also leads to better purchasing decisions and customer satisfaction.

- **Differentiation**:  
   Existing software for background image generation, such as Photoroom, 24 AI, and PicWish, generate acceptable results on general requests. However, this background is usually not related to the product or topic, which is integral to our needs. Additionally, each of these products works well only in English, which presents its own problems. On the positive side, we discovered some convenient features such as the ability to easily redact the original image, which we will consider implementing in the tool.

- **User Impact**:  
   Beyond improving user engagement, our software project extends to driving sales through enhanced visualization, and potentially optimizing the e-commerce industry's approach to product representation by reducing resource-intensive photoshoots.

- **User Testimonials or Use Cases**:  
   Potential user testimonials might highlight how the tool helped them accurately visualize furniture in their living space, leading to a satisfying purchase and a seamless online shopping experience.

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address?  
   
   Our project addresses the need for users of the Leroy Merlin website to visualize products in realistic environments for scale and appearance.

2. Who are your target users or customers?

   Our customers are the Leroy Merlin website, who need an efficient way to display their products to their clients.

3. How will you validate and test your assumptions about the project?

   Representatives from Leroy Merlin will provide feedback about our idea and express their wishes.

4. What metrics will you use to measure the success of your project?

   Leroy Merlin representatives will evaluate the success of the project based on their satisfaction with the results and factors such as image realism, processing speed and user interface usability.

5. How do you plan to iterate and pivot if necessary based on user feedback?

   We will identify areas that need improvement and prioritize them for future updates. We are willing to adjust our approach based on this feedback, ensuring the system aligns with the needs and preferences of our client.

   

## **Leveraging AI, Open-Source, and Experts**

- **AI**:  
   We will use AI for the major part of our project for recognizing fitting backgrounds, generating them and applying them to the product image.

- **Open-Source**:  
  Our plans involve using open-source libraries and tools, such as translation APIs, to save time in development of our project. Specifically, we plan to utilize the following models:

  - transparent-background: A tool for removing the background from images. More details can be found [here](https://pypi.org/project/transparent-background/).
  - photo-background-generation: A model for generating photo backgrounds. More details can be found [here](https://huggingface.co/yahoo-inc/photo-background-generation).
  - BLIP image captioning large: A model for generating image captions. More details can be found here [here](https://huggingface.co/Salesforce/blip-image-captioning-large).
  - 
   We also assume that this list may change in the final product.

- **Experts**:  
   Our team will consult with experts from Leroy Merlin to develop a product that meets their needs.


## **Defining the Vision for Your Project**

- Overview: Our project is a software that uses AI to generate backgrounds for images to be used in the Leroy Merlin store. It solves the problem of innefficient creation of product display images by offering a quick and cost-effective way to generate said images.

- > Schematic Drawings:  
  Отсюда мб https://wiki.yandex.ru/xakaton/tz/

- Tech Stack:
  - Backend: Docker, Python, FastAPI, Uvicorn
  - Frontend: React, Vite, TypeScript
  - Database: MongoDB
  - ML: Python, PyTorch, probably MLFlow/AirFlow
  - HuggingFace libraries: Diffusers, Transformers

>*Feel free to add more sections as needed. You are the owners of your project!*  
> можно добавить что-то про будущее проекта либо как мерлен тут задействован, а можно и забить
