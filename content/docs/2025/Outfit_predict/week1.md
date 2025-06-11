**1\. Team Formation**:

TEAM Name: Outfit\_predict

Communication Channels: Telegram

| Team Member | Telegram ID | Email address | Track | Responsibilities |
| :---- | :---- | :---- | :---- | :---- |
| Dinar Yakupov | @Dinar5150 | d.yakupov@innopolis.university | Frontend | Designing UX/UI of project application  Developing Frontend for project application. Contribute to writing reports and making presentation. Commit link: [https://github.com/IU-Capstone-Project-2025/Outfit\_predict/commit/bdd27021c52d4a241164836bdff18f99c1888af5](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/bdd27021c52d4a241164836bdff18f99c1888af5) |
| Artyom Grishin | @Irecool | ar.grishin@innopolis.university | Backend | Designing backend architecture for project application. Developing backend application for project. Contribute to writing reports and possibly to ML part. Wrote dataset comparison: [https://github.com/IU-Capstone-Project-2025/Outfit\_predict/commit/288e915f65b0768f59c5683abf76805aa5c592fe](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/288e915f65b0768f59c5683abf76805aa5c592fe)  |
| Bulat Sharipov | @bulattt11 | b.sharipov@innopolis.university | ML | Designing ML part of the application Researching current approaches in project objective. Contribute to writing reports and possibly to backend part. Commit link: [https://github.com/IU-Capstone-Project-2025/Outfit\_predict/commit/5a0347da914714069cbd99a0dba23539f12eefa6](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/5a0347da914714069cbd99a0dba23539f12eefa6) |
| Victor Mazanov | @Victor131116 | v.mazanov@innopolis.university | Team Lead | Writing reports. Making presentation. Contribute to ML, Backend, DevOps part. Commit link: [https://github.com/IU-Capstone-Project-2025/Outfit\_predict/commit/6859e4b35de8deea63cfc06d1125cd71c29beb08](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/6859e4b35de8deea63cfc06d1125cd71c29beb08) |
| Danil Fathutdinov | @Danman\_575 | d.fathutdinov@innopolis.university | ML | Designing ML part of the application. Researching current approaches in project objective. Contribute to writing reports and possibly to backend part. Commit link: [https://github.com/IU-Capstone-Project-2025/Outfit\_predict/commit/ac05bd84f76e8c0a0469e95fc4f4f57ed363c5cd](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/ac05bd84f76e8c0a0469e95fc4f4f57ed363c5cd)  |
| Remal Gareev | @resent99 | r.gareev@innopolis.university | DevOps | Designing architecture for project deployment Deploying the project on local servers. Possibly contribute to backend and ML parts. Wrote a part of backend, but send it in Telegram as a file: [https://github.com/IU-Capstone-Project-2025/Outfit\_predict/commit/b8583666c90718293134bfbb75c808baf4c2ed5a](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/b8583666c90718293134bfbb75c808baf4c2ed5a) |

**2\. Project Brainstorming & Selection:**

Project Ideas:

1. Web-platform that helps users to decide which outfit to wear based on a person's wardrobe and clothing of characters from movies, fashions collections, fashion markets.  
2. Framework with fit\_predict like interface but for weld defect detection. The framework will have implemented segmentation/detection models with appropriate modifications (i.e. backbone pre-trained on x-ray images). Moreover, this framework could be extended for medical purposes.  
3. Web-platform that will automatically analyze product cards on marketplaces and derive several properties. 

Brief market research:

1. For the first project we have several existing products. Lamoda provides possibilities to try on clothes, but this functionality is limited and does not provide an opportunity to try the whole outfit and collect it. Several other applications work with 3D modelling, which is not applicable in day-to-day cases.  
2. There exist torchxrayvision framework but its functionality is limited. There are pre-trained backbones and segmentation/detection models, but users need to build / modify models for specific tasks. Moreover, it does not provide any interface to train and predict the model. 

Problem Statement (for chosen idea): During routine life we face a problem of what clothes to wear. We have a wardrobe, but scanning through it and combining outfits may be very time-consuming and would not lead to optimum outfit. Therefore, we try to provide a web-platform that will generate and suggest outfits based on persons wardrobes.

**3\. Basic Requirements Gathering:**

Target users: Persons who care about their look.

Target users and their primary needs: Primary need is to fastly design an attractive outfit using an existing wardrobe.

User stories:

1). “As an ordinary user , I want to get a full look for a day so that I won’t spend much time for choosing clothes and will look good”

2). “As a stylist, I want to create a basic look for my client so that I could do my work more efficient”

3\) “As a clothes seller, I want to advertise my products via showing representative looks  so that I will have more clients”

4). “As a customer, I want to complete my look with missing cloth so that I could have full new look.”

Initial Scope (What in MVP, what is not):  
In MVP:

1). Upload images with clothes in the context of session, limit in some images per session

2). User- friendly and simple design of web application 

3). Getting best looks from our dataset in terms similarity between user clothes and look’s clothes.

Not in MVP:

1). Possibility to choose specific clothes from wardrobe and search for looks that complete missing look

2). A user authorization with saving wardrobe

3). Possibility to choose the desired style of the look from represented ones

**4\. Tech Stack (With Justification)**

Frontend: React is a library that updates only the changed parts of the page so that the interface works quickly and smoothly. TypeScript is basically a JavaScript with static typing, which helps to find errors before running the code. Tailwind CSS provides a set of classes for quick and convenient styling without manually writing CSS.

Backend: FastAPI for serving API, PostgreSQL as a database for storing different metadata for pictures and user data. Minio as S3 object storage to store clothes images. Psycopg has an async connection to the database. And Celery (if needed) to make task queues for future GPU utilization efficiency.

ML: PyTorch for designing, training model and for inference purposes. Possibly albumentations for augmenting dataset. Ultralytics for providing already implemented models and simple interfaces. Other frameworks could be added as needed.

