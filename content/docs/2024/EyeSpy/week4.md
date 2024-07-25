---
title: "Week #4"
---

# **Week #4**

## **External Feedback**

This week, we received valuable feedback from close friends who tested our app. They pointed out the need to track the presence of the user's face in the frame, as the absence can disrupt landmark drawing. Additionally, they noticed that face tracking can break if the face is partially covered by obstacles like hands. We need to account for these scenarios in future iterations to improve robustness.

## **Testing**

Our testing strategy will include end-to-end (e2e) testing once we implement the backend. We will also conduct performance testing on various M1, M2, and M3-powered Macs to ensure the app runs smoothly on all supported devices. Security testing will be crucial to guarantee that the video stream and cropped images never leave the user's device. This week, we tested the initial version of face tracking and plan to test gaze estimation next week.

## **Iteration**

Based on the external feedback and our testing results, we will iterate on the app to enhance face presence detection and handle obstacles that may interfere with tracking. These improvements will be integrated into the next version to ensure a more reliable and accurate tracking system.

## **Weekly Progress Report**:

Our team successfully converted the PyTorch model to CoreML using coremltools and tracing. This conversion was crucial for leveraging the full capabilities of Apple's hardware.

### **Challenges & Solutions**

The main challenge we faced was handling the model's input, as it expects an image in the form of a multidimensional float array. Initially, we tried to make the model accept grayscale images, but this led nowhere because tracing couldn't convert numpy operations to the corresponding CoreML format. Instead, we spent the week finding an efficient method to grayscale an NSImage and convert it to a float array. We discovered that CIImageFilter is incredibly fast and can grayscale images with almost zero overhead.

### **Conclusions & Next Steps**

We concluded that the converted CoreML model is over 10 times faster than the PyTorch version, thanks to its ability to utilize the M family GPU and Apple Neural Engine (ANE). This significant speed improvement allows us to integrate gaze estimation into our app without any performance drop. Next steps include finding a way to draw the gaze vector for debugging purposes and estimating where the user is looking on the screen, or if they are looking outside of it.
