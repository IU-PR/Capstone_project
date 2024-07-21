---
title: "Week #6"
---

# **Week #6**

## **Presentation**
https://gamma.app/docs/Language-Teacher-q11cywi3f6p7vvt?mode=doc

## **Weekly Progress Report**

**Our team did:**

For this week we have integrated the ML functionalities on the website. We also made some editing on the UX/UI domain. Now the user can navigate through the website more easily.

We have fixed some issues with the audio_score function that compares the phonemes of the model with the true phonemes of text. The function was giving error when inputting multiple words.

## **Challenges & Solutions**

Audio_score function not running on the website, the issue is being solved currently.

The model was not working on multiple words, we fixed the mapping in the dictionary to make it work with multiple words.

The model is trained on the alphabet of English, hence the decoder can give invalid concatenation of the symbols. We have used longest-common-subsequence to get the best possible alignment of the characters. 

The implementation if this was already made previously, but the reason of this was discovered recently after checking the model specification.

## **Conclusions & Next Steps**

By the end of the week, we will need to deploy our website. 

For the design part, we would need to change some colors and beautify the pages of functionality (characters and sentences).

Also, by the end of the week we would show statistics of our model on the common voice dataset and compare it with the  built-in library in python.
