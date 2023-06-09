---
weight: 1
bookFlatSection: true
title: "UnifAI"
---

# **Week #1**

# **Introduction**

## **Team Members**


| Team Member              | Telegram ID                          | Email Address                       |
|--------------------------|--------------------------------------|-------------------------------------|
| Polina Zelenskaya (Lead) | [@cutefluffyfox](t.me/cutefluffyfox) | p.zelenskaya@innopolis.university   |
| Ekaterina Maximova       | [@N0m1nd](t.me/N0m1nd)               | e.maximova@innopolis.university     |
| Ekaterina Urmanova       | [@aleremus](t.me/aleremus)           | e.urmanova@innopolis.university     |
| Evsey Antonovich         | [@aiden1983](t.me/aiden1983)         | e.antonovich@innopolis.university   |
| Daniyar Cherekbashev     | [@wrekin](t.me/wrekin)               | d.cherekbashev@innopolis.university |


## **Value Proposition**

**Problem statement**: 
The language barrier is becoming more and more noticeable. 
Digitization of the world brings people from different cultures and countries closer together. 
Because of all this, knowledge of foreign languages has become a necessary skill for modern 
society. Unfortunately, not all people have the resources to learn a new languages, 
adapt to unique accents and be able to understand language specific grammar.

**Solution description**:
We aim to utilize a combination of several Machine Learning tools to recognise and 
translate speech in (near) real time. Those tools may include: a voice recognition 
model (i.e Whisper), a translation model (i.e Opus) and a TTS model (to be determined). 
Ideally, voice processing would be done client-side, providing independence and privacy to our users. 

**Benefits to Users**:
Our project offers an array of benefits to users looking to utilize it. By using our 
software, users will not have to worry about any language barriers, as the app will 
seamlessly translate anything they speak in real-time and let others hear it in their 
language of choosing. Less time will have to be spent on choosing what language to speak to 
accommodate everyone, and fewer problems will arise from the no longer existing problem of 
not understanding someone’s accent. Additionally, no money will need to be spent on hiring 
professional translators to translate speeches during public events - saving money for 
everyone. Lastly, hearing everything in one’s native language will greatly increase 
productivity, as people generally comprehend speech faster in the language they are the 
most proficient at.

**Differentiation from existing solutions**:
There exists several solutions to this problem.
Google-based speech-to-speech models. Their downfall is use-case. 
They aimed to be used in offline dialogs as a more convenient way to interact with your interlocutor. 
We want to make translation as parallel as possible, and not require any 
additional action from the user. We aim to make this app integrable into other apps 
such as online games and video streaming services.

**User Impact**:
With our app, users can engage in conversations and use apps that were previously 
inaccessible due to language limitations. They can communicate without having to worry 
about manually translating each sentence. Additionally, the scope of use of this project 
is incredibly large: people will find this solution useful for gaming, for regular 
conversations, and maybe even for industries by allowing businesses to expand their 
worldwide reach and client base.

**User Testimonials / Use Cases**:
We imagine many possible use cases for our product, for example:
* Improving meetings in nationally diverse workplaces, especially those where many people work remote. Frequently, language barrier is one of the biggest challenges in workplaces that employ workers of different nationalities, and we feel as if our project could eliminate that issue completely, letting people communicate easier than ever in such scenarios.
* Allowing gamers of different nationalities to communicate in games easier. Very frequently people that speak different languages may get matched up in games where teamwork is important, and in such cases it may be quite frustrating to play! Our software would solve this issue, and allow gamers from all over the world to enjoy playing together and forming great teams.


## **Lean Startup Questionnaire**

**What problem or need does your software project address?**\
The main problem we address is Language barrier on the Internet in ‘voice’ communication: 
video meetings, video replay, streaming content, video games etc. 

**Who are your target users or customers?**\
Our project aims to provide seamless communication for people who speak 
online with foreigners, and/or listen to any audio content on the Internet (e.g. Podcasts, YouTube videos).

**How will you validate and test your assumptions about the project?**\
We will conduct online meetings with foreigners and ask them to speak their native languages. 
If we could understand and communicate with them, we will consider our assumptions proven.

**What metrics will you use to measure the success of your project?**
* Correctness of extracted words from streaming audio per language / dialect (e.g. accuracy)
* Correctness of translation (Word Error Rate) per language / dialect (e.g. cosine distance of 'sentence' vectors)

**How do you plan to iterate and pivot if necessary based on user feedback?**\
If some language will have recognition or translation problems, we will try different models 
or add models for special cases. Maybe we will try to return parameters 


## **Leveraging AI, Open-Source, and Experts**

**How we plan to leverage AI & Open-source in our project**:
We will use an Open-Source ML model to convert people’s speech to text (whisper AI), 
text translator to target language (model TBD), and text voice over (model also TBD). 
Some code (or answers to questions) might also be generated from natural language processing models.

## **Inviting Other Students**

At this moment in time we have already assembled a team and assigned roles, and we do not plan to 
invite anymore. However, if we will find ourselves stuck on some task, we are open to ask experts, or 
even expand our team with new specialists.

## **Defining the Vision for Your Project**

**Overview**: 
Our project utilizes a combination of several Machine Learning tools 
to recognise and translate speech in (near) real time. Those tools may include: 
a voice recognition model (i.e Whisper), a translation model (i.e Opus) and a TTS model 
(to be determined). Ideally, voice processing would be done client-side, providing independence 
and privacy to our users. 

**Schematic Drawings**:

{{<mermaid>}}
flowchart TD
    A(Hans) -->|Speaks German| B[UnifAI]

    B --> |Convert voice to text| C[Server]
    C -->|Tatar text| D[UnifAI]
    D --> |Synthesize Tatar Speech| G(Alsu)
    C -->|Russian Text| E[UnifAI]
    E --> |Synthesize Russian Speech| J(Ivan)
    C -->|English text| F[UnifAI]
    F --> |Synthesize English Speech| k(John)
{{</mermaid>}}

One user(Hans) speaks his native language. UnifAI Captures his voice and turns it into text.
Text is sent to Server that translates the text into requested languages, 
for example, user Alsu has set the language that she wants to receive to tatar, and server 
generates tatar text. When text is delivered to another user, let’s consider Alsu again, 
UnifAI synthesizes voice from text.

**Tech Stack**:
* Python 3.10
* PostgreSQL 14
* Django 4.2.2

**Anticipating Future Problems**: 
Resources required to maintain 3 ML models might not be enough for an average user 
(a decent GPU is needed to smoothly run the app). Also, STT model has delay (depending on 
a scale of chosen model of whisper AI), and if model with the lower size is chosen then 
accuracy will be also lower on average.

**Elaborate Explanations**: 
* Independent microservices are used in our project for STT, TTS models and translation. 
* STT model that we will use (whisper AI), is a multitasking model that performs multilingual speech recognition and language identification. We will choose one of the 5 available models of whisper (that differ in size, required vram and accuracy appropriately) on client-side based on the PC characteristics of the end user.
* Our solution differentiates from others by providing a real-time translator for all connected users with proper models’ computing resources delegation and accuracy. 
