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

2) Mentorship Support:
   We are supported by Vladimir Bazelevich,
   a master's student skilled in mathematics and machine learning (ML),
   who will help us navigate potential ML challenges.

3) **Exploring Alternative Resources:**
   In addition to documentation, we use websites like [StackOverflow](https://stackoverflow.com/) and
   LLMs ([ChatGPT](https://chat.openai.com/), [Chat Mistral](https://chat.mistral.ai/)).
   For ML solutions,
   we refer to [Papers With Code](https://paperswithcode.com/), [Google Scholar](https://scholar.google.com/),
   and search engines.

4) **Identifying Knowledge Gaps:**
   Given the evolving nature of ML, we acknowledge the existence of knowledge gaps,
   especially when dealing with problems that traditional algorithms cannot solve.
   For instance, we plan to use siamese networks for image grouping,
   a method that has yielded satisfactory results in similar tasks.
   However, we are open to exploring new techniques or insights to enhance performance.
   An example of this is providing a model with depth insight to detect defocus blur,
   which resulted in improved performance.
   To assess our ideas and gain valuable insights, we will consult our mentor.

5) **Engaging with the Tech Community:**
   We actively follow GitHub, Papers with Code, and Google Scholar to keep up with the latest ML developments.

6) **Learning Objectives:**
   Our goals include:
	- Gaining hands-on experience in machine learning, particularly within the context of image processing and analysis.
	- Experimenting with novel methods for blur detection and similar shot grouping.
	- Enhancing our team collaboration skills through the joint implementation and publication of a user-friendly ool.

7) **Sharing Knowledge with Peers:**
   We regularly discuss relevant topics, share solutions, and brainstorm ideas in our Telegram group and calls.

8) **Leveraging AI:**
   We employ AI tools like [ChatGPT](https://chat.openai.com/) and [Chat Mistral](https://chat.mistral.ai/)
   to gain clarity on technical aspects.

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

1. **Completed the desktop app UI design:**
   After completing the user flow and UI sketch, Matthew created Lo-Fi and Hi-Fi UI designs in Figma.
   The designs were evaluated by other team members, all required improvements were done.
   His work will be used in the following weeks to implement the desktop application.

2. **Implemented UI drafts in demo desktop app:**
   Nikita used UI sketches to create a demo application.
   The application contains all required screens and transitions between them.
   Moreover, application successfully runs both on Windows and Linux.

3. **Identified existing solutions for blur detection and image grouping:**
	- Arthur and Timofey looked for existing image similarity ranking methods.
	  They have found several solutions and identified the most promising works:
      - https://arxiv.org/pdf/1906.07589
      - https://arxiv.org/pdf/1610.07940
    - Michael and Artemii checked papers on blur detection, highlighting the following ones:
      - https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.13567?saml_referrer
      - https://paperswithcode.com/paper/depth-and-dof-cues-make-a-better-defocus-blur

4. **Identified required tools and libraries.**
	- Egor helped to find the library for image manipulations. 

### **Challenges & Solutions**

...

### **Conclusions & Next Steps**

...