## **Week №6 Report**

## **Links**

Specify here all the necessary links to your website, application installer, final demo, etc.

* Deployment: [https://outfitpredict.ru/](https://outfitpredict.ru/)  
* API Docs: [https://outfitpredict.ru/api/docs\#/](https://outfitpredict.ru/api/docs#/)  
* Design: [\[CAPST\] Outfit Predict: Design Screenshots](https://drive.google.com/drive/folders/1RgxqnDQA1F4scbUIOTpxkfgz6KNdx-LE?usp=sharing)  
* Demo: [demo\_outfit\_predict\_16\_07\_2025](https://drive.google.com/file/d/1BBsZ2nXdcEKEWO2KuaXyvkaVg9NgMkNV/view?usp=sharing)

## **Final deliverables**

## **Project overview**

**Problem**: Imagine you have a lot of clothes, but cannot compose a suitable outfit from these.

**Solution**: We created a website, where you can upload your clothes, and it will create an outfit from your clothes for you.

**Target Audience:** Anyone who care about their look

### **Features**

1. Landing Page: Here you can observe a short explanations of our project, some examples, and about page  
1. Signup & Login: Here you can register, and log in into your profile  
2. Upload images: You can upload images of your clothes from your wardrobe into your profile. Here they will be visible  
3. Generate outfits: You can generate suitable outfits from your clothes.

### **Tech stack**

1. Frontend: React, Tailwind CSS  
2. Backend: FastAPI, MinIO, PostgreSQL, Qdrant, Alembic  
3. DevOps: Docker, Nginx, Docker-compose  
4. ML: Ultralytics, Transformers, fine-tuned YOLOv11, DINO v2, SAM, FashionCLIP

### **Setup instructions**

Look from *Repository Setup* section to *Running the Application* section:

[https://github.com/IU-Capstone-Project-2025/Outfit\_predict/blob/main/README.md](https://github.com/IU-Capstone-Project-2025/Outfit_predict/blob/main/README.md)

## **Presentation draft**

*[outfit\_predict\_presentation.pdf](https://drive.google.com/file/d/10qfMN1IJh5XMFEp-9bmuJ7ugt7rDW8Vw/view?usp=sharing)*

# **Weekly commitments**

## **Individual contribution of each participant**

Victor Mazanov: Conducted Customer Development interview ([link](https://www.notion.so/CustDev-for-Week-6-21d5a218c5d5807da8a2d1e3306cf45c)) and add functionality of searching similar cloth on the internet by the description of the thing from outfit ([link](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/2c0b18b213936c5ce5e2776bb0105c4f92725c40))  
Bulat Sharipov: Managed team work, distributed tasks, backend development, wrote report, created presentation  
Danil Fathutdinov: Created ML class for determining the outfit class  
Dinar Yakupov: Updated frontend pages, fixed bugs and introduced optimizations  
Remal Gareev: Improved CI & CD. Fixed bugs and introduced optimizations in the backend.  
Artyom Grishin: Performed backend development and product design ([link](https://www.notion.so/Product-Design-for-week-6-232a795c445f8015af78dc284ffcc368?source=copy_link))

## **Plan for Next Week**

- Implement last features, such as choosing only subset of clothes to perform outfits  
- Introduce style filtration to resulting outfits  
- Introduce randomization to outfit search, or daily outfits  
- Final polishing and presentation repetition

**Confirmation of the code's operability**

We confirm that the code in the main branch:

- In working condition.  
- Run via docker-compose (or another alternative described in the README.md).

