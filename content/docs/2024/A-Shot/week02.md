---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

- **Desktop App:**
  We will use [Compose Multiplatform](https://www.jetbrains.com/lp/compose-multiplatform/) for A-Shot,
  as it is an easy-to-use and efficient tool for creating multiplatform applications.

- **Neural Networks:**
  [PyTorch](https://pytorch.org/) will be our choice for training and operating neural networks due to its extensive
  toolset.

- **Image Handling:**
  For loading images, we will opt for [ImageMagick](https://imagemagick.org/), as it supports over 100 image formats,
  including those preferred by photographers but not supported by common libraries like [OpenCV](https://opencv.org/).

### **Architecture Design**

1. **Component Breakdown**:
   A-Shot is composed of several key elements:

	- **Multiplatform Desktop Application:**
	  This is the user-friendly interface that photographers interact with.

	- **Machine Learning Modules:**
		- **Blur Detection:**
		  This module identifies and flags blurry images.

		- **Similar Shot Grouping:**
		  This module groups similar shots together.

2. **Data Management**:
   A-Shot is optimized for handling large image volumes efficiently, maximizing performance and resource utilization.

	- **In-Place Sorting:**
	  Images are organized within their original directories,
	  offering disk space conservation and maintaining a streamlined,
	  user-friendly file structure.

	- **Thumbnail Generation:**
	  For fast operation and low memory usage,
	  A-Shot displays thumbnails of high-resolution images within the user interface.

3. **User Interface (UI) Design**:
   The UI design is ready and available on Figma: ...
   The application consists of several screens, here are some of them:

	- **Import Screen:**
	  The initial screen for selecting the image source.
	- **Overview Screen:**
	  Enables navigation between sorted shots.
	- **Cull screen:**
	  The core application interface for viewing grouped images and selecting the best ones.

4. **Integration and APIs**:
   A-Shot currently operates as a standalone application, performing model inference locally.
   Additional features may include integration with popular tools such as Adobe Lightroom and Adobe Photoshop,
   once the core functionality has been fully developed and optimized.

5. **Scalability and Performance**:
   A-Shot's standalone nature and Jetpack Multiplatform development ensure
   effortless scalability across nearly all PC/laptop platforms.
   However, machine learning models should be optimized for efficient execution on lower-spec devices.

6. **Security and Privacy**:
   A-Shot ensures user privacy, as it operates offline without storing sensitive data.

7. **Error Handling and Resilience**:
   A-Shot prioritizes user data safety by avoiding sensitive operations like modification or deletion,
   ensuring that application errors do not affect user images.
   Furthermore, A-Shot will undergo testing under various conditions to guarantee reliability and resilience.

8. **Deployment and DevOps**:
   A-Shot's CI/CD pipeline, using GitHub Actions, will ensure regular updates with automated testing, version control,
   and build processes.
   Deployments will be managed through GitHub Releases for seamless distribution.

### **Week 2 questionnaire:**

1) **Tech Stack Resources:**
   Our team utilizes the following tool documentations:
	- [Compose Multiplatform](https://www.jetbrains.com/help/kotlin-multiplatform-dev/get-started.html)
	- [PyTorch](https://pytorch.org/docs/stable/index.html)
	- [Image Magick](https://imagemagick.org/script/develop.php)
	- [Material Design 3](https://m3.material.io/)

2) Mentorship Support: ...

3) **Exploring Alternative Resources:**
   In addition to documentation, we use websites like [StackOverflow](https://stackoverflow.com/) and
   LLMs ([ChatGPT](https://chat.openai.com/), [Chat Mistral](https://chat.mistral.ai/)).
   For ML solutions,
   we refer to [Papers With Code](https://paperswithcode.com/), [Google Scholar](https://scholar.google.com/),
   and search engines.

4) Identifying Knowledge Gaps: ...

5) Engaging with the Tech Community: ...

6) Learning Objectives: ...

7) Sharing Knowledge with Peers: ...

8) Leveraging AI: ...

### **Tech Stack and Team Allocation**

| Team Member              | Track                | Responsibilities               |
|--------------------------|----------------------|--------------------------------|
| Artemii Miasoedov (Lead) | ML                   | Product and Project management |
| Timofey Brayko           | ML                   | Image grouping                 |
| Artur Rakhmetov          | ML                   | Image grouping                 |
| Nikita Kurkulskiu        | ML                   | Desktop app                    |
| Egor Valikov             | Cybersecurity        | Desktop app                    |
| Matthew Rusakov          | Software Development | UX/UI design, Desktop app      |
| Mikhail Romanov          | ML                   | Blur detection                 |

### **Weekly Progress Report**

During this week our team:

1. Identified required tools and libraries
2. Created desktop app UI design
2. Identified existing solutions for blur detection and image grouping
3. Implemented UI drafts in demo desktop app

### **Challenges & Solutions**

...

### **Conclusions & Next Steps**

...