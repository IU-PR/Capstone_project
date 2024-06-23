---
title: "Week #3"
---

# **Week #3**

## **Developing the First Prototype and Creating the Priority List**

### **Technical Infrastructure**

For the initial launch of our models, we utilized a laptops with NVIDIA RTX 3060 and NVIDIA GTX 1650M GPUs.
When they were launched successfully, for the next processing we transitioned to using server with
an NVIDIA TESLA P40 GPU. This powerful infrastructure allowed us to handle the computational demands of our deep
learning tasks efficiently.

While these laptops' GPUs provided adequate performance for development, we recommend using higher-performance GPUs for
faster processing and improved efficiency in future iterations.

### **Backend Development**

- **Blur Detection Model**:

For the **Blur Detection model**, we adopted
the [D-DFFNet](https://paperswithcode.com/paper/depth-and-dof-cues-make-a-better-defocus-blur),
which was trained on a specialized [dataset](https://drive.google.com/file/d/1pkgfGSKx80Eq1_kq6-PwYl6zSYXwkqS8/view).
Our model showed promising results during testing on our internal dataset, as detailed in
our [GitHub issue](https://github.com/IU-Capstone-Project-2024/A-Shot/issues/12).
This model leverages depth and depth-of-field cues to enhance blur detection accuracy significantly.

Here you can see video of model work:


- **Image Grouping Model**:

For the **Image Grouping model**, we
utilized [CVNet](https://github.com/shihaoshao-gh/superglobal?tab=readme-ov-file),
informed by the research in this [paper](https://arxiv.org/abs/2308.06954) and further supported by a
second [study](https://strathprints.strath.ac.uk/55814/1/Connor_etal_VISAPP_2015_identification_of_mir_flickr_near_duplicate_images.pdf).
The model was trained on
the [California-ND dataset](https://www.researchgate.net/publication/256986331_California-ND_An_annotated_dataset_for_near-duplicate_detection_in_personal_photo_collections),
which is specifically annotated for near-duplicate detection in personal photo collections. This approach has
significantly improved the accuracy and reliability of our image grouping functionality.

### **Frontend Development**

Our application was developed using *Kotlin Multiplatform Compose*, leveraging the IntelliJ IDEA environment for an
efficient development workflow. Kotlin Multiplatform allows us to share code across multiple platforms, ensuring a
seamless and consistent user experience.

### **Data Management**

For the Minimum Viable Product (MVP), we prioritized model development and application functionality over data
management. As such, we did not initially implement a database. However, in the next phase, we plan to integrate a
robust database solution using **SQLite** and the **Room** library. This will enhance our data storage and management
capabilities, providing a solid foundation for future application scalability.

### **Prototype Testing**

We conducted extensive testing of our prototype to ensure reliability and performance.
The testing phase involved evaluating the models' accuracy, the application's responsiveness, and overall system
stability.
Also, we created CI/CD pipelines based on **Gradle** and **CMake** building for different operating systems to improve testing
In plans, CI/CD pipelines for deployment using GitHub Releases

## **Weekly Progress Report**

In the backend development phase, we successfully implemented two models: Blur Detection and Image Grouping. Here are
the key accomplishments:

1. **Integration with Java using JNI**:

- We utilized the Java Native Interface (JNI) to enable calling C++ code from Java, facilitating seamless integration
  between the models and the Java-based application.

2. **Model Execution with ONNX Runtime**:

- Incorporated the ONNX Runtime library into our C++ code, allowing our models to run on multiple operating systems and
  devices, including Windows, Mac, Linux, Android, and iOS.
- Exported the trained models in the .onnx format for compatibility and deployment efficiency.

### **For Blur Detection Model**

1. **Image Upload with Magick++**:

- Integrated the Magick++ library (a C++ API for ImageMagick) to support a wide range of image formats.
- Developed code to handle image uploading and preprocessing.

2. **Model Execution**:

- Implemented the code to execute the blur detection model on the uploaded images.
- Connected the C++ backend logic with the Java application, ensuring smooth functionality.

[Here you can see the video of blur-detection model work](https://drive.google.com/drive/u/0/folders/18jDpyZYHyM5TImLloxhwcTvzpyfWj6Ws)

Here you can see screenshots of image-groiping model work:

![First image](/2024/A-Shot/week03/image-grouping/1sta-shot.png)
![Second image](/2024/A-Shot/week03/image-grouping/2nda-shot.png)
![Third image](/2024/A-Shot/week03/image-grouping/3rda-shot.png)

### **Frontend Development**

- Integrated most of the UI components into the existing UX skeleton created in the previous week.

[Here you can see the video of working prototype](https://drive.google.com/file/d/1KzaFrnpbjQm7oWYZ74eE02lWsVIItn-N/view?usp=sharing)

### **Testing and CI/CD**

- Conducted thorough testing of the application and models to ensure reliability and performance.
- Implemented a CI/CD pipeline to automate building processes, enhancing development efficiency
  and consistency.

### **Challenges & Solutions**
- **1st Problem** Trained models must be run from the application. We could have called code from Java and Python using libraries, or run a separate subprocess and use stdout/in for communication, but this did not suit us.
  
- **1st Solution** We decided to use onnxruntime, a tool that allows you to run neural networks on any device.  To do this, we exported the models to the .onnx format. We wrote a C++ library that uses ImageMagick to upload images and Onnxruntime to launch neurons. Next, the application accesses this library using JNI (Java Native Interface).


- **2nd Problem** onnxruntime and imagemagick are required to run our library

- **2nd Solution** We have compiled these libraries from the source with the necessary configurations for us and included them in our library

### **Conclusions & Next Steps**

Despite significant progress, several tasks remain:

1. **Model Performance Improvement**:

- While the current model accuracy is satisfactory, we aim to further enhance performance through additional
  training and fine-tuning. Also, it will be nice to optimize blur detection model to reduce the complexity and weight
  of the model
- Also we need to integrate Image-Grouping model into our application

2. **Frontend Completion**:

- At testing phase we understand, that UI 'eats' a lot of extra space, it seems informate, so we will brainstorm 
about new ways to update UI features and finalize the remaining parts of the frontend to ensure complete 
functionality and a polished user experience.

3. **Database Integration**:

- Integrate SQLite and Room for database management to improve application performance and user experience.
- This will eliminate the need for importing libraries every time, streamlining data handling processes.

3. **Multiplatforming**:

- While our library has been compiled and tested on Linux, next week we will build it for Windows and macOS
