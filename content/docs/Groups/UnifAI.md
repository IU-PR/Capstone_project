---
weight: 1
bookFlatSection: true
title: "UnifAI"
---
<style> .markdown a{text-decoration: underline !important;}</style>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)

# **Introduction**

**UnifAI** is a platform that cracks language barrier with Artificial Intelligence. 
We aim to create perfect speech-to-speech pipeline to recognize, translate and simulate 
speaker's voice in real-time. 

<p align="center">
    <img src="https://svgshare.com/i/uHd.svg"  width="50%">
</p>

We provide [application](TODO_INSERT_LINK_WHEN_DONE) that could recognize users 
speech (voice-to-text), transmit it to server that translates it (text-to-text), and 
parse messages from other people and generating their voices in your own language 
(text-to-speech). If you want to know more about program workflow, you can check 
_Schematic Drawings_ in [Vision for our project](UnifAI#defining-the-vision-for-your-project).

If you want to collaborate with us, or just interested in project, message 
Polina Zelenskaya at [Telegram](t.me/cutefluffyfox) or 
[Email](mailto:p.zelenskaya@innopolis.university)!

# **Week #1**

## **Team Members**


| Team Member              | Telegram ID                          | Email Address                       |
|--------------------------|--------------------------------------|-------------------------------------|
| Polina Zelenskaya (Lead) | [@cutefluffyfox](t.me/cutefluffyfox) | p.zelenskaya@innopolis.university   |
| Ekaterina Maksimova      | [@n0m1nd](t.me/n0m1nd)               | e.maximova@innopolis.university     |
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
We aim to utilize a combination of several Machine Learning tools to recognize and 
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
They aimed to be used in offline dialogues as a more convenient way to interact with your interlocutor. 
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
to recognize and translate speech in (near) real time. Those tools may include: 
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


**Anticipating Future Problems**: 
Resources required to maintain 3 ML models might not be enough for an average user 
(a decent GPU is needed to smoothly run the app). Also, STT model has delay (depending on 
a scale of chosen model of whisper AI), and if model with the lower size is chosen then 
accuracy will be also lower on average.

**Elaborate Explanations**: 
* Independent microservices are used in our project for STT, TTS models and translation. 
* STT model that we will use (whisper AI), is a multitasking model that performs multilingual speech recognition and language identification. We will choose one of the 5 available models of whisper (that differ in size, required vram and accuracy appropriately) on client-side based on the PC characteristics of the end user.
* Our solution differentiates from others by providing a real-time translator for all connected users with proper models’ computing resources delegation and accuracy. 


# **Week2**

During week 2 we conducted several meetings and discussed crucial aspects of out project: process workflow, technologies we are going to use, research that is required for successful result, roles in team and responsibilities of each member.


## **Tech Stack and Team Allocation**

**Polina Zelenskaya** - team leader that manages all communication within the team. 
Also, one of machine learning engineers and responsible for research behind voice 
generation, workflow of text-to-speech models, and communication with the server on 
the client side. Tech stack consists of python, fairseq models (text-to-speech that can 
simulate provided voice), requests library for server communication, and os package as 
tool for analyzing pc.  

**Ekaterina Urmanova** - ml engineer that can work with different models and will try 
to optimize UnifAI for each user based on their computer. Also, responsible for 
translation from one language to another. Tech stack: python, Opus (collection of 
pre-trained models that contains more than a thousand text-to-text translators) and 
Whisper (library of speech recognition models).

**Ekaterina Maksimova** - server developer that controls sessions, user texts, 
users data such as authorization info, and responsible for deployment of server and 
translation model. Tech stack consists of: python, gRPC, Redis, websocket, Opus, Docker.

**Evsey Antonovich** - Frontend Python developer, responsible for the user-facing part 
of the Python application, GUI, working with Daniyar to connect the frontend part of 
the client with the backend part of the client. Tech stack: python, Dear PyGui, 
fastapi, websocket, multithreading

**Daniyar Cherekbashev** - backend python developer, responsible for client-server websocket 
connection, whisper model suggestion (based on client GPU and CPU), processing audio 
input with speech recognition model on client side with pause/end of sentence detection. 
Tech stack: python, python libraries: fastapi, uvicorn, starlette, websocket, 
faster_whisper, speech_recognition


## **Architecture Design**

**Component Breakdown**: 
Our principal architecture consists of three parts: Voice Recognition, 
Text Translation and Voice Synthesis. We are currently considering an architecture 
where voice recognition and synthesis is done on the client machines or servers 
hosted by client companies. 

Connection between client and server side will be maintained via websocket 
(persistent TCP connection). Each time a user says anything, the data will be 
immediately sent to the server and translated here. Once the user finishes their 
sentence, the flag will be sent along with json to the server, so that the server 
can send back the full translation.

When the full translation is received by appropriate users, the text will be 
synthesized with the voice of the speaker with the help of voice cloning AI. 
Some sample data for voice cloning AI might be sent before creating a connection 
for more accurate results.

**Data Management**: 
We only plan to use databases for short-term storage and caching. 
Voice data will not be saved on the server, and we will only send short 
voice clips chosen by users for use in voice synthesis.

**UI/UX Design**: 
As the main part of our project is automatic voice recognition, translation 
and synthesis, the user will not have to manually interact with the application much. 
Most of the process will be fully automatic, and as such, our user interface will be 
as simple as possible - at most, there will be a login menu, a settings window and a 
chat log. This simplicity will allow for users to quickly integrate our application 
into their workflow without any hurdles, not having to spend much time learning on how 
to use our app.

**Integration and APIs**: 
Currently, we are not planning to use any external APIs as we are going to run 
all models locally on the server- and client-side.

**Scalability and Performance**: 
Scalability is only limited by the computing power needed to run translation models 
on the server. Additional instances for translation servers may be spun up on-demand 
with little issue.

**Security and Privacy**: 
We intend to store minimal user data, limited to basic authentication for making calls. 
Voice processing is done entirely on the client.

**Error Handling and Resilience**: 
We will be consistently polling all connected (via websocket) clients and reconnect 
if a failure occurs. All critical errors will be logged on the server for manual 
inspection. In our app, failure of any microservice will make it impossible 
for an app to continue working as intended, so it is important to gracefully 
recover after every error.

**Deployment and DevOps**: 
Our project is mostly client based, so the server part will not be very difficult. 
We will use Docker and GitHub for deployment. 

## **Week 2 discussions**

**Tech Stack Book Resources**:
As we have already done prerequisite research on our tech stack, 
we feel like we have enough knowledge to not refer to any books on our tech stack. 
Additionally, there are already plenty of good sources on our tech stack that are not books.

**Mentorship Support**:
Our team is composed of developers who all possess a diverse background and 
experience with various technologies and tech stacks, leading to a well-rounded 
team with sufficient summary experience and knowledge to not require a mentor to lead us.

**Exploring Alternative Resources**:
To aid us in our research for potential ways to structure and develop our 
project, we utilize various techniques of information searching, looking 
through sources such as [Hugging Face](https://huggingface.co/), 
[Kaggle](https://www.kaggle.com/), [Stackoverflow](https://stackoverflow.com/), 
looking for [GitHub](https://github.com/) repositories of projects of similar scope to ours, 
reading articles on [Habr](https://habr.com/ru/all/) and using [Google](https://www.google.com/) 
to search for any other potential sources where we could gain insight on 
effectively utilizing various technologies in our project.

**Identifying Knowledge Gaps**:
Right now we are developing product that is not implemented by anyone yet. 
This field of speech-to-speech translation requires research that could dramatically 
improve performance of models, resulting in a various of questions that we should 
investigate:
* How TTS models perform when 'clone' and 'output' audio languages differs?
* Are there any 'perfect sentences' that would simulate majority of sounds that humans use for communication?
* Is there any 'paths' to increase quality of translation, or directly translating from input language, to target one, performs the best?
* Will idea of separating all parts (speech recondition, translation, and voice cloning) create a bottleneck situation?
* Is real-time translations much more valuable, than delayed with better performance? 
* Due to different language structures it may be impossible not to delay tts output, what could be done about it?
* And many more! Q~Q

We are not yet sure about the exact knowledge gaps that will appear in the 
process of the application (backend) development of our application, but if we do 
find out that we have some, we will have no trouble in dealing with them through 
the use of brainstorming solutions as a team and effective information searching online.

**Engaging with the Tech Community**:
As we’ve already mentioned, we have a diverse team of developers with knowledge in 
various tech stacks. Due to this, we feel confident enough in being able to develop 
our project without particularly active engagement with the broader tech community 
or other experts for additional information. Of course, if we do feel like our 
knowledge is limited in certain fields, then we will try to reach out to other 
experts in these fields (e.g. community in IU, friends) for potential guidance and assistance, 
utilizing our professional networks that we gained through our development backgrounds.

**Week Learning Objectives**:
During this week our main goal was to test pipeline by hands: record audio, extract text 
from it, translate, and do voice cloning for different language. We succeeded in it and 
now have a complete idea how to automate this process.

In addition, we needed to discuss team roles, decide on logo and processes in team, 
complete report, and just set up schedule for meetings. We managed to achieve all this.

**Sharing Knowledge with Peers**:
To share knowledge and expertise with our teammates, we organize weekly sessions 
where we meet up and discuss the ways we could use our technologies from the tech 
stack in the development of our project, alongside sharing our personal insight on 
how the expertise from each of us could be used to further aid in effective 
application of technologies in our software.

**Leveraging AI**:
If we find out that we are lacking in expertise in a certain field that would 
be necessary for the completion of our project, then it is possible that we could 
use LLMs such as  to ask some questions related to that field in order to gain more knowledge 
about it and figure out the best way of applying technologies from that field in our project.


