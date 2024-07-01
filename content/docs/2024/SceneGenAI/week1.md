---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member          | Telegram ID   | Email Address                       |
|----------------------|---------------|-------------------------------------|
| Bulat Akhmatov       | @bulatik1337  | b.akhmatov@innopolis.university     |
| Alexandra Vabnits    | @sashhhaka    | a.vabnits@innopolis.university      |
| Amir Nigmatullin     | @cheezy_on_me | am.nigmatullin@innopolis.university |
| Mintimer Karimov     | @JIeru0H      | m.karimov@innopolis.university      |
| Nurislam Zinnatullin | @zaurall      | n.zinnatullin@innopolis.university  |
| Bahdan Shah          | @bodashkaxd   | b.shakh@innopolis.university        |
| Daniil Tiuftin       | @daniil_ktr   | d.tiuftin@innopolis.university      |

### **Value Proposition**

- **Identify the Problem**:
  For users of furniture marketplaces like the [Leroy Merlin website](https://leroymerlin.ru/), it is important to
  visualize products against
  relevant backgrounds to represent the scale of the products and how they look in a real environment.
  Current solution: for example, Leroy Merlin, as an expert in the field, solves this problem by filming in a photo
  studio. For
  example, a vase is photographed against the background of the interior, a drill on a table in the workshop, and garden
  furniture against the background of a garden plot. Such filming is labor-intensive; it is necessary to organize the
  logistics of goods to the photo studio, and in the case of garden furniture, it is difficult to organize a place for
  filming in general. Sometimes, Leroy Merlin uses 3D rendering instead of a photo shoot, but this is also
  labor-intensive
  and expensive.
  Proposed solution: Generative neural networks can help solve this problem by generating backgrounds that match the
  product, enhancing the experience for clients of furniture marketplaces in general. With Leroy Merlin representative
  as our advisor for the project, we have an opportunity to consult with an expert in the field and receive valuable
  feedback.

- **Solution Description**:  
  Using AI to create a service tool that integrates backgrounds into product images on the online shop. This tool will
  help clients to visualize product sizes in the environment they want, eliminating the need for extensive photoshoots
  or 3D rendering.

- **Benefits to Users**:   
  Users will benefit from a more immersive shopping experience and clear understanding of how products fit into their
  desired spaces. This also leads to better purchasing decisions and customer satisfaction.

- **Differentiation**:  
  Existing software for background image generation, such as Photoroom, 24 AI, and PicWish, generate acceptable results
  on general requests. However, this background is usually not related to the product or topic, which is integral to our
  needs. Additionally, each of these products works well only in English, which presents its own problems. On the
  positive side, we discovered some convenient features such as the ability to easily redact the original image, which
  we will consider implementing in the tool.

- **User Impact**:  
  Beyond improving user engagement, our software project extends to driving sales through enhanced visualization and
  potentially optimizing the e-commerce industry's approach to product representation by reducing resource-intensive
  photoshoots.

- **User Testimonials or Use Cases**:  
  Leroy Merlin reported that feedback from their clients revealed how the tool enabled them to accurately visualize
  furniture in their living spaces, leading to confident and satisfying purchases. This is supported by [research from
  the Journal of Business Research](https://www.sciencedirect.com/science/article/abs/pii/S0148296314001039), which
  found that product presentations with relevant consumption backgrounds are
  more effective in evoking mental imagery than solid white backgrounds, increasing consumers' behavioral intentions
  through a positive emotional response. Showcasing these success stories adds credibility and reinforces our
  value proposition.

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address?

   Our project addresses the need for users of furniture marketplaces, such as the Leroy Merlin website, to visualize
   products in realistic environments for scale and appearance.

2. Who are your target users or customers?

   Our customers are furniture marketplaces, who may benefit from finding an efficient way to display their products,
   and their clients, who will receive a smoother customer experience.

3. How will you validate and test your assumptions about the project?

   Representatives from Leroy Merlin will provide feedback about our idea and express their wishes.
   We will test the solution on different pictures and evaluate the results. If possible, we will also collect feedback
   from client users of the marketplace.

4. What metrics will you use to measure the success of your project?

   Leroy Merlin representatives will evaluate the success of the project based on their satisfaction with the results
   and factors such as image realism, processing speed, and user interface usability. We will also consider the
   feedback from the end-users of the marketplace.

5. How do you plan to iterate and pivot if necessary based on user feedback?

   We will identify areas that need improvement and prioritize them for future updates. We are willing to adjust our
   approach based on the feedback from case holder and end-users, ensuring the system aligns with their needs and
   preferences.

## **Leveraging AI, Open-Source, and Experts**

- **AI**:  
  We will use AI for the major part of our project for recognizing fitting backgrounds, generating them and applying
  them to the product image.

- **Open-Source**:  
  Our plans involve using open-source libraries and tools, such as translation APIs, to save time in development of our
  project. Specifically, we plan to utilize the following models:

    - transparent-background: A tool for removing the background from images. More details can be
      found [here](https://pypi.org/project/transparent-background/).
    - photo-background-generation: A model for generating photo backgrounds. More details can be
      found [here](https://huggingface.co/yahoo-inc/photo-background-generation).
    - BLIP image captioning large: A model for generating image captions. More details can be
      found [here](https://huggingface.co/Salesforce/blip-image-captioning-large).

  We also assume that this list may change in the final product.

- **Experts**:  
  Our team will consult with experts from Leroy Merlin to develop a product that meets their needs.

## **Defining the Vision for Your Project**

- Overview: Our project is a software that uses AI to generate backgrounds for images to be used in the Leroy Merlin
  store. It solves the problem of innefficient creation of product display images by offering a quick and cost-effective
  way to generate said images.

- > Schematic Drawings:  
  ![image](/2024/SceneGenAI/TechnicalDiagram.jpg)


- Tech Stack:
    - Backend: Docker, Python, FastAPI, Uvicorn
    - Frontend: React, Vite, TypeScript
    - Database: MongoDB
    - ML: Python, PyTorch, probably MLFlow/AirFlow
    - HuggingFace libraries: Diffusers, Transformers

- Project Origin:
  Our expert is Leroy Merlin, the case holder in the hackathon organized by Yandex Cloud, which takes place from 1st
  June until 15th June. We regularly have calls with them and receive feedback on what kind of product they want to see.
  Yandex Cloud provides us with access to their services to facilitate development. We plan to develop a prototype by
  the deadline of the hackathon, continue to improve the product further by getting feedback from an expert.
