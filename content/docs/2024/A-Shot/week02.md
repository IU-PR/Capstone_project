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

3. **User Interface (UI) Design**: ...

4. **Integration and APIs**: ...

5. **Scalability and Performance**: ...

6. **Security and Privacy**: ...

7. **Error Handling and Resilience**: ...

8. **Deployment and DevOps**: ...

### **Week 2 questionnaire:**

1) Tech Stack Resources: ...

2) Mentorship Support: ...

3) Exploring Alternative Resources: ...

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