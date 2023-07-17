---
weight: 1
bookFlatSection: true
title: "UnifAI"
---

<style> .markdown a{text-decoration: underline !important;} </style>
<style> .markdown h2{font-weight: bold;} </style>

![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper-74aa9c?style=for-the-badge&logo=openai&logoColor=white)


# **Presentation**

{{< embed-pdf url="/UnifAI/UnifAI.pdf" >}}


# **About us**

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

And if you want to collaborate, or just interested in our team, message 
Polina Zelenskaya at [Telegram](https://t.me/cutefluffyfox) or 
[Email](mailto:p.zelenskaya@innopolis.university)!

# **Week #1**

## Team Members


| Team Member              | Telegram ID                                   | Email Address                       |
|--------------------------|-----------------------------------------------|-------------------------------------|
| Polina Zelenskaya (Lead) | [@cutefluffyfox](https://t.me/cutefluffyfox)  | p.zelenskaya@innopolis.university   |
| Ekaterina Maksimova      | [@n0m1nd](https://t.me/n0m1nd)                | e.maximova@innopolis.university     |
| Ekaterina Urmanova       | [@aleremus](https://t.me/aleremus)            | e.urmanova@innopolis.university     |
| Evsey Antonovich         | [@aiden1983](https://t.me/aiden1983)          | e.antonovich@innopolis.university   |
| Daniyar Cherekbashev     | [@wrekin](https://t.me/wrekin)                | d.cherekbashev@innopolis.university |


## Value Proposition

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


## Lean Startup Questionnaire

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


## Leveraging AI, Open-Source, and Experts

**How we plan to leverage AI & Open-source in our project**:
We will use an Open-Source ML model to convert people’s speech to text (whisper AI), 
text translator to target language (Opus), and text voice over (Piper + FreeVC24). 
Some code (or answers to questions) might also be generated from natural language processing models.

## Inviting Other Students

At this moment in time we have already assembled a team and assigned roles, and we do not plan to 
invite anymore. However, if we will find ourselves stuck on some task, we are open to ask experts, or 
even expand our team with new specialists.

## Defining the Vision for Your Project

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


# **Week #2**

During week 2 we conducted several meetings and discussed crucial aspects of out project: 
process workflow, technologies we are going to use, research that is required for successful 
result, roles in team and responsibilities of each member.


## Tech Stack and Team Allocation

**Polina Zelenskaya** - team leader that manages all communication within the team. 
Also, one of machine learning engineers and responsible for research behind voice 
generation, workflow of text-to-speech models, and communication with the server on 
the client side. Tech stack consists of python, [gTTS/Piper/FreeVC24](UnifAI#voice-cloning-tts--sts) models (text-to-speech that can 
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


## Architecture Design

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

## Week 2 discussions

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



# **Week #3**

This week we conducted several meetings and built standalone reproducible components of our app: 
microphone input stream with Whisper model voice recognition (speech-to-text), text translator (text-to-text) with Opus model, 
backend server with user authentication, login page, and TTS (Text-to-speech) via gTTS, 
STS (speech-to-speech) based on [coqui's](https://github.com/coqui-ai/TTS) vctk/freevc24 model. In addition, we conducted research to find new way to synthesise speech.


## Finalized application flow

We finalized the complete flow of our application, which is stated and developed as follows: 
1. User authorize to our application
2. After authorization, user is able to join a voice channel, where his voice will be recognized by an STT model running on a client-side
3. Then transcribed text will be sent to the server where translation part happens (to all other languages sitting in the same channel)
4. Then every other person except speaker receives translated text 
5. This text will be used by voice cloning models on client-side.
   1. Firstly text-to-speech model will generate text in any arbitrary voice
   2. Secondly, speech-to-speech model will replace synthesised voice to real one of our client

We named this full pipeline 'STT-TTTT-TTS-STS'. Please be sure to remember it, as we will refer to it only that way.


## SpeechToText (STT)
We implemented the usage of the Faster Whisper STT model in a class with configurable model parameters 
(model size, type of computation, device (CPU/GPU)) and transcription parameters (there are quite a lot of 
configurable parameters, such as language, beam size, penalty, temperature, etc).

We also tested tiny and medium versions of Whisper and analyzed performance metrics that are crucial for us:

|                     | Whisper-tiny                                               | Whisper-medium                                               | Whisper-large-v2                                               |
|---------------------|------------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------|
| Licence             | MIT                                                        | MIT                                                          | MIT                                                            |
| Pre-trained         | Yes                                                        | Yes                                                          | Yes                                                            |
| Parameters          | ~39M                                                       | ~244M                                                        | ~1550M                                                         |
| Languages supported | 99                                                         | 99                                                           | 99                                                             |
| Link                | [Hugging Face](https://huggingface.co/openai/whisper-tiny) | [Hugging Face](https://huggingface.co/openai/whisper-medium) | [Hugging Face](https://huggingface.co/openai/whisper-large-v2) |
| Examples            | [Hugging Face](https://huggingface.co/openai/whisper-tiny) | [Hugging Face](https://huggingface.co/openai/whisper-medium) | [Hugging Face](https://huggingface.co/openai/whisper-large-v2) |
| Error rate*         | Check description                                          | Check description                                            | Check description                                              |
| Real-time*          | Yes                                                        | Yes, on GPU                                                  | Yes, on GPU                                                    |

\* Whisper models show competitive advantage over already commercial-used speech recognition models. 
It is hard to formulate Word-error-rate as a number, as it is highly dependent on dataset and languages used.
In addition, real-time factor depends on system, hardware, language, and batch size. So if you are interested in precise
information, please refer to [OpenAI research paper](https://cdn.openai.com/papers/whisper.pdf).\
\*\* MIT Licence supports commercial use, meaning we can use these models in our project. 

Some demo of what we have done:

{{< youtube Cye_leJ29UQ >}}


## Translation model (TTTT)
TextToTextTranslator - technology that translates text from one language to text in another language. 
We decided to use Opus-MT models, because they are lightweight, accurate, and can translate to more than 
a hundred languages.

Here are some parameters that we based our search on:

|                     | Opus-MT                                                           | 
|---------------------|-------------------------------------------------------------------|
| Licence             | CC-BY 4.0 license                                                 |
| Pre-trained         | Yes                                                               |
| Parameters          | ~39M                                                              |
| Languages supported | 231                                                               |
| Link                | [Opus website](https://opus.nlpl.eu/Opus-MT/)                     |
| Examples            | [Hugging face](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en) |
| Word error rate*    | Check description                                                 |
| Real-time*          | Yes, on GPU                                                       |


\* Word error rate, and real-time-factors are both language-specific. For precise information please check Opus website.\
\*\* CC-BY 4.0 license supports commercial use, meaning we can use these models in our project. 


We have figured out how to use Opus-Mt models. For an example, we have made a simple translator that can translate 
text between russian and english:

![Example of translation mode](https://i.imgur.com/xgzsyyt.png)


## Voice cloning (TTS + STS)
Brief introduction to what happened. We faced a lot of challenges with voice cloning (speech synthesis) 
models (Please refer to [challenges](UnifAI#challenges-and-solutions) for more information). Due to that we needed to develop new technology. As our solution, we decided to decompose voice cloning models (that take as input text 
and voice to clone), to two different models: text-to-speech, and speech-to-speech: 

**TextToSpeech (TTS)**\
Text to speech is technology to synthesize human-understandable audio files. This technology has 
developed rapidly as its interest is raised. Nowadays, there exist thousands of real-time TTS models, 
with different speakers and quality. This is one of the reasons why we switched models.

For the TTS part we found several potential libraries and technologies that could help us make the 
project come true: [gTTS](https://pypi.org/project/gTTS/), [Piper](https://github.com/rhasspy/piper). We have already implemented and tested gTTS, however in the near future we would like to switch to Piper as it seems to provide better audio synthesis.


|                     | gTTS                                          | Piper                                                  |
|---------------------|-----------------------------------------------|--------------------------------------------------------|
| Licence             | MIT                                           | MIT                                                    |
| Pre-trained         | No (deterministic)                            | Yes                                                    |
| Parameters          | None                                          | ~7.3M                                                  |
| Languages supported | 16                                            | 22                                                     |
| Link                | [Pypi](https://pypi.org/project/gTTS/)        | [Github](https://github.com/rhasspy/piper/tree/master) |
| Examples            | [Youtube](https://youtu.be/BuMonMxrb4Q?t=161) | [Github](https://rhasspy.github.io/piper-samples/)     | 
| Stability           | Stable                                        | May ignore / mispronounce words                        |
| Real-time*          | Yes                                           | Yes                                                    |


**SpeechToSpeech (STS)**\
Speech to speech is an idea to generate an audio file, based on original audio with text that we want 
to pronounce with voice from the second file. In a nutshell, we want to change the speaker's voice in the 
original audio. Luckily for us, we realized that these types of models perform pretty good as they are filtering 
audio with a new ‘voice filter’. Which is good for us, as we can now use non-human sounding TTS with good pronunciation, 
and replace voice to customer-one.

One of STS models we decided to use is FreeVC24:

|                     | FreeVC24                                                    | 
|---------------------|-------------------------------------------------------------|
| Licence             | MIT                                                         |
| Pre-trained         | Yes                                                         |
| Parameters          | ~13M                                                        |
| Languages supported | All (Non-language-specific)                                 |
| Link                | [Github](https://github.com/OlaWod/FreeVC )                 |
| Examples            | [Github](https://olawod.github.io/FreeVC-demo/)             |
| Word error rate     | ~4.23% ( [research](https://arxiv.org/pdf/2210.15418.pdf) ) |
| Real-time           | Yes                                                         |



**Voice cloning progress**\
During this week we implemented gTTS TTS model, as well as integrated FreeVC24 within the pipeline. So now we can
clone anyone's voice (but for now, far from ideal) and pronounce sentences with it on several languages. You can see our current results below:

Text to pronounce:

```
早上好中国. 现在我有冰激淋 我很喜欢冰激淋. 但是《速度与激情9》比冰激淋'
Доброе утро китай. Теперь у меня есть мороженое, я люблю мороженое. Но «Форсаж 9» лучше мороженого
Guten Morgen, China. Jetzt habe ich Eis, ich liebe Eis. Aber „Fast and Furious 9“ ist besser als Eis
Good morning china. Now I have ice cream, I love ice cream. But 'Fast and Furious 9' is better than ice cream
```


Original audio:

{{< audio src="/UnifAI/voice-sample-w3.mp3" capstone="Voice sample" >}}

Our generated results (with current models):

{{< audio src="/UnifAI/tts-sts-ch-w3.mp3" >}}
{{< audio src="/UnifAI/tts-sts-de-w3.mp3" >}}
{{< audio src="/UnifAI/tts-sts-ru-w3.mp3" >}}
{{< audio src="/UnifAI/tts-sts-en-w3.mp3" >}}

Samples of already-existing models with direct voice-cloning (approach we abounded due to licence problems, stability issues, and limitations on real-time factors and languages support):

{{< audio src="/UnifAI/vc-ch-w3.mp3" >}}
{{< audio src="/UnifAI/vc-de-w3.mp3" >}}
{{< audio src="/UnifAI/vc-ru-w3.mp3" >}}
{{< audio src="/UnifAI/vc-en-w3.mp3" >}}


## Backend development & Data management
For the sake of preserving the sanity of our backend developer we have made the decision to switch 
to golang(& gin) for our backend.

We have also made some decisions regarding security and data management: for authentication we 
are going to utilize JWT(JSON Web Token) with HMAC algorithm and the principle of access & refresh 
tokens. User passwords will be hashed with the bcrypt algorithm and stored in a postgresql table.

![Server deployment](https://i.imgur.com/XHTsbsv.png)


## Frontend (UI/UX of application)
During this week, we have done research on the potential ways to implement the user-facing part of our 
application, and after investigating several potential solutions, decided on a language and 
framework to use.

We decided to use Python, and mainly one library: Dear PyGui. We made this decision for several reasons:
* First of all, both Python and Dear PyGui are easy to use. At the current stage of development, it is important for us to be able to quickly iterate upon our previous changes. The ease of use of Python and Dear PyGui, therefore, makes them good choices.
* Secondly, Dear PyGui uses GPU rendering and is built using C++, which gives it great performance. Great performance is important for our application to be able to meet the real-time usage demands, and will also let our application be snappy and responsive in usage.
* Lastly, Dear PyGui has a permissive MIT license, which means that as we scale up our project for commercial use, the license will not be a hindrance.

After coming to a conclusion on which framework to use, we quickly developed a login page for our application using Dear PyGui. The ease of use of both Python and Dear PyGui let us develop this page without much difficulty, featuring the logo of our project, text boxes to input the server address and username, and a button to log in. Of course, this is only the initial iteration of the login screen, and we will potentially refine it further as the development progresses. 

![Application UI example](https://i.imgur.com/SyxmPdV.png)


## Challenges and Solutions

**Challenge with microphone input:**\
We should decide when we have to handle microphone input data to be processed while also not 
interrupting the process of speaking. Also, if we listen for too much without transcribing, 
there will be a significant delay. The best solution found is to use VAD (Voice Activity Detector), 
that will detect speech in the microphone stream and, after a certain configurable threshold, 
this speech will be passed to the whisper model for transcription.

**Lack of research:**\
We are dealing with the problem that not so much research was done in real-time voice translation 
models. We need: real-time, multi-language, multi-speaker, voice cloning models. Preferably with 
good quality. Due to the fact that we are working in a developing field, we spend hours and hours 
just to find what solutions already exist and how they work. As a result of a week-long search, we 
found no solutions that satisfy our requirements, which led us to our last hope - develop new 
technology by ourselves. (P.S. we succeeded, new stt-tttt-tts-sts pipeline was developed, and you 
can check our voice-cloning (tts-sts) results [here](UnifAI#voice-cloning-tts--sts))

**Quality of models that we can use on client side:**\
Speaking about models, we firstly decided that speech-recognition and voice cloning will be both 
on client side. This is beneficial as we can protect users data, reduce server load, and make 
models adjustable for each person individually. However, good speech-recognition models are far 
away from real-time when they are deployed on slow CPUs (which could be the case with our clients). 
So now we have a dilemma, about streaming audio and recognizing it on the server, or let the situation 
stay the same. We decided that for MVP we will not change our design, and as a future improvement 
add subscription to a server-based-models for better and faster performance. This will both be the 
way to make the project commercial, and provide users with not so good CPU (and no GPU) to use our 
product.

**Slow start of translation model:**\
First translation takes additional time to load the model. Just loading a model on CPU/GPU is 
not enough to fully initialize it. This will affect our goal of achieving the Real Time solution. 
To deal with this problem we decided to make the first translation (initialization) on the server 
before a client connects to it. This will increase time needed to start the Server but will 
decrease time delay between clients.

**Translation model unexpected behaviour:**\
When we pass a line with no words or symbols into the translator, the model tries to generate 
output, but gives random text and takes more than 5 seconds to generate it. To overcome 
this problem we found a solution to add a barrier that filters out lines that can disrupt 
translator’s work.

## Plans for upcoming weeks
1. Implement proper audio stream queueing and multithreading on client-side for improved performance
2. Complete the backend implementation: authorization, authentication, data storage, passing messages between clients, Docker
3. Improve TTS model from gTTS to Piper ( [learn more](UnifAI#voice-cloning-tts--sts) )
4. Improve handling of TTTT's unexpected behaviour. Collect statistics when problems occur. One of the metrics we will use is time spent translating a single message; if it exceeds average by some factor, a diagnostic message will be logged.
5. Implement several more windows: voice recording screen upon first registration of the user in the application, the main window of the application where a chat log of what the other users are saying will be shown, a settings window for settings such as: choosing a voice recognition model, pipeline settings, volume, etc.; and possibly even a password recovery screen.


# **Week #4**

During this week we conducted meeting with potential clients (to demonstrate them our product and collect
feedback), developed new pages for UI, and made our solution downloadable within one line of code!


## External Feedback
To find out what our customers are looking for, we decided to collect some external feedback. 
However, as our project contain different parts that user communicate with, we determined that it would
better and more informative for us to collect feedback with different ways:
* Conducted meetings with potential clients (our friends) and showed them current technologies we implemented (we used this technique for SST, TTS-STS models, UI/UX)
* Tested STT models on our own by translating different audio samples and comparing them with the original text
* Found expertise feedback with much bigger representative group (used this for TTTT)

With this approach we got broader understanding of quality of our models, and things that our customers 
want from this product.


**Speech recognition (SST):**\
After running model on GPU, we decided to suggest Whisper-large as the main model, as we found it to 
be real-time with delay less than 1 second! We supposed that only whisper-base would fit under 
these criteria as we never tested with GPU properly. For comparison, on CPU for base model it 
takes around 1-1.5 seconds for processing, while large model on GPU takes around 0.4-0.6 seconds, 
which is 2-3 times faster, and, which is the most important, **FAR** more accurate: we asked our
friends to tell us some story, and for 3-4 minute speech on Russian, on average model recognized all but 2 
words correctly, and for English speech results were the same.

Also, this demo showed that inputs with low language probability are highly likely to be incorrect 
and thus might be ignored for further processing. For that, we are going to find some threshold 
that will omit messages that do not satisfy it. In addition, we might ask what languages a person 
might speak, so we can completely drop all messages with misinterpreted detected language.


**Text translation (TTTT):**\
For TTTT we decided to analyze metrics more 'strictly'. As we have small representative group, it would be
better for us to find some research/analysis with deeper research. Luckily for us, these models 
were previously tested, and they showed excellent results for most common languages such 
as English, Russian, Spanish, Chinese, German etc. There was used two following metrics:
* [BLEU (bilingual evaluation understudy)](https://en.wikipedia.org/wiki/BLEU):\
An algorithm for evaluating the quality of text which has been machine-translated from one natural 
language to another. Quality is considered to be the correspondence between a machine's output and 
that of a human.
* [Chr-f (Character F-score)](https://machinetranslate.org/chrF):\
A metric for machine translation evaluation that calculates the similarity between a machine 
translation output and a reference.

Both of these metrics show how machine translated text is similar to human translation, 
the more the score model gets, the more human-like text will be. 

For example the most recent version of [Opus-mt-RU-EN](https://github.com/Helsinki-NLP/OPUS-MT-train/tree/master/models/ru-en)
(from russian to english translation) has 0.611 BLEU score and 0.736 Chr-F score. As [Google Team 
says](https://cloud.google.com/translate/automl/docs/evaluate) BLEU score more than 0.6 means that model
is often better than a human, so this model will be perfect for our task.

For more models evaluation you can visit official [Opus website](https://opus.nlpl.eu/Opus-MT/).


**TTS-STS:**\
For this part, we asked our friend to record 15-30 second audio and asked them to choose any sentence to 
generate. After that, we translated given sentence to several languages (such as German, Russian, English, Chinese)
and generated audio samples of them saying that sentence in different languages. We did this with 3 models:
our previous [gTTS solution](UnifAI#voice-cloning-tts--sts), current [Piper model](:TODO:), and facebook model
[Fairseq](https://github.com/facebookresearch/fairseq/tree/main/examples/mms). Then we asked responders to sort
by quality, and all 6 people selected our Piper-based solution as the best.

We were glad to hear such positive feedback, however our representative group noticed that quality of speech
cloning is not the best, as it could be easily distinguished between real person. We explained to them the problem
we face with tradeoff between fast-light generation (not so good, but model weight only 50MB), and deep-learning
copy of voice with 3GB model. We mentioned our solution as to train models on server and translate 
high-quality cloning, so that no user would need to download several gigabytes for each person in a call.
But to make that option as a subscription, so we can support GPUs on the server. Most of the client said
that it is a good idea, and they were ready to pay for it.


**Frontend:**\
To gain feedback on the responsiveness and the general user experience of our UI, we showed 
our application (or at least, the frontend part of it) to some other students of the university 
that we knew and were friends with. We asked them to just naturally use our application and 
observed how they interacted with it, and afterwards we asked them some questions about their 
experience: which parts did they feel were unintuitive, what was confusing, what they liked 
the most about the UI, and how they would rate the experience overall. From these surveys, 
we found that while some parts of the UI were slightly confusing at first, our application 
generally felt easy to use and that the application user interface flow was natural.


## Testing

**Server**:\
We have conducted testing of the backend. We used a REST client (httpie, tests are partially 
automated, partially manual). The authorization subsystem seems to work well: the flows of “register -> 
refresh (obtain new token pair)” and “login -> access endpoint with required login” all function correctly.
Meaning user authorization and data exchange functions properly. In addition, that results that database is 
configured correctly, and store all required information in a correct form.

**Frontend:**\
To test the frontend part, we have employed manual testing, by naturally using the 
app and seeing that the UI changes work correctly. Alongside that, we asked other 
members of the team to try and use the UI, also asking them to try doing something that would 
break it. After that - we asked some people unrelated to the team to try and use the UI, to 
see how a person outside the development team would use the application and see any potential 
issues we might have missed.


## Iteration progress

**Backend progress:**\
This week we implemented database services, namely an API for interacting with 
postgres:
* designed schemas for users
* implemented basic requests

Also, during this week we implemented registration and authorization services, as well as
token creation and validation, and password hashing and salting. During this week we continued 
working on chat rooms functionality.


**STT progress:**\
In this week, we implemented a test version of fully asynchronous websocket connection on client 
side to receive and send messages independently in a non-blocking manner. Also, we made a port of 
microphone input from pyaudio to sounddevice to solve compatibility issues among different 
operating systems, so it now works on both Windows (tested), Linux (tested), and should be on 
other systems as well (not tested macOS). In addition, we ran these models on GPU and analyzed
their performance.

**TTTT progress:**\
We added more filters to handle inappropriate input mentioned in [Week 3 Report](UnifAI#plans-for-upcoming-weeks), 
these filters can handle strings made only from special characters, such as spaces, commas, 
slashes etc. In addition, we Added possibility to run several translations in parallel. 
And during this week we collaborated with backend developer and discussed API to make it easier to
connecting translator to the server.

**TTS-STS progress:** \
During this week we finally moved to [Piper](https://github.com/rhasspy/piper/tree/master) models. 
As this technology is only several weeks old, we were surprised that all their models are now 
available on [hugging face](https://huggingface.co/rhasspy/piper-voices), which made it much easier 
to develop us a downloader for them. So, during this week we not only switched to better TTS, 
but we also made all models (Piper and FreeVC24) downloadable and configurable with 1 line of code.

Here are some examples of new 'voices', you can compare them with previous [mentioned here](UnifAI#voice-cloning-tts--sts):

{{< audio src="/UnifAI/tts-sts-ch-w4.mp3" >}}
{{< audio src="/UnifAI/tts-sts-de-w4.mp3" >}}
{{< audio src="/UnifAI/tts-sts-ru-w4.mp3" >}}
{{< audio src="/UnifAI/tts-sts-en-w4.mp3" >}}

**Settings window:**
While using our application, different users will have different needs. As such, we have 
implemented a settings screen into our app, so that users can adjust the application to their 
needs. Currently, we have four settings that can be changed: volume, speech playback speed, the 
input device to use and the model size to use during speech recognition. Our work on this 
focused on implementing the UI itself and also the process of saving and loading the settings 
from a configuration file.

![Settings window](https://i.imgur.com/LfRcwMl.png)

**Language Settings window:**
Our application is aimed to bridge the language gap between users of different nationalities, 
and so, each user may need to specify a different language that the application will need to 
translate the words of other users to, alongside choosing a specific TTS model.

![Language settings window](https://i.imgur.com/hX3p33h.png)


# **Week #5**

During this week we collected even more feedback, provided a list of upgrades to backend part, 
analyzed server requirements, filtered TTS-STS models by license, and contacted main Piper 
developer for help. We are on a productivity streak!

{{< hint danger >}}
Alright, amazing reports, as usual. Kudos for being active! 
{{< /hint >}}

## External feedback v2

**STT:**\
To collect even more feedback on speech recognition, we conducted another meeting with new representative
group in which we let people test two Whisper models: whisper-large-v2 and whisper-base. As we 
expected, people were completely unsatisfied with the transcriptions of the whisper-base model, 
because even in complete silence and with clearly pronounced words, they were 
often misinterpreted by this model. Opposed to the base model, the large model showed incredible 
results even with noises around, and only suffered sometimes when multiple people were talking 
at the same time. 

To overcome this problem, we updated language probability threshold and asked our group to speak
for a little more. After that our group was fully satisfied and impressed with our results. We asked 
group to provide a numeric score (from 0 to 5) for both models, and that what results we get:

|             | whisper-base | whisper-large-v2 | whisper-large-v2 (fine-tuned) |
|-------------|--------------|------------------|-------------------------------|
| Candidate 1 | 1            | 5                | 5                             |
| Candidate 2 | 2            | 4                | 5                             |
| Candidate 3 | 3            | 4                | 5                             |
| _Average_   | _~2_         | _~4.33_          | _~5_                          |


**TTS-STS**:\
This one was tricky to test, as there are few other solutions that correlates with us. So we decided 
to collect feedback via Google forms of two types: with and without deep voice cloning models. We made
this separation as we think that heavy models should be considered, however they are not the solution 
we are going for. With this is mind, we provided audio samples of already-existing [lightweight solutions](UnifAI#voice-cloning-tts--sts),
our first [gTTS approach](UnifAI#voice-cloning-tts--sts), [Piper-designed](UnifAI#iteration-progress) model examples, and samples of [deep-learning clones](https://www.youtube.com/watch?v=Bj8jsz4pwho). 

The mean results of both group and total mean could be found in a table below:

|                       | Light abandoned | gTTS-based | Piper-based | Deep clone |
|-----------------------|-----------------|------------|-------------|------------|
| Without deep-learning | 1.75            | 2.05       | 3.95        |            |
| With deep-learning    | 1.27            | 1.4        | 2.73        | 4.65       |
| _Average_             | _~1.54_         | _~1.77_    | _~3.42_     | _~4.65_    |

**User Interface:**\
In order to collect feedback on the application UI, we contacted potential clients 
conducted a meeting, and showed the user interface of our application, try it out, and rate it on four 
metrics, alongside providing comments on each part and where they felt the UI was the weakest:
* <ins>Responsiveness</ins>\
Responsiveness was defined as how quickly the UI responded to the user’s inputs, and in general 
how much it felt like the actions of the user had a meaningful impact on the application. In general, 
users of the application said that the UI felt mostly pretty responsive, with the only delays in the 
updates of the UI being the time it takes for the application to send a request to the server and 
receive in response, and apart from that, the application felt generally responsive and quick.
* <ins>Design</ins>\
The design rating of the UI was defined as how nice the application felt to look at. As the UI of 
our application is built upon the Dear PyGui framework, which uses ImGui, it provides by default 
a sleek, clean, dark design with blue colors, a design that the vast majority of the users found 
pleasing to the eyes and refreshingly minimalistic, alongside invoking a sense of nostalgia for 
those people that have worked with this GUI framework before.
* <ins>Natural flow</ins>\
The “natural flow” of the UI was defined as how intuitive it felt to use - how the actual flow of 
the interface correlates with the flow that the users expect. As our application is still in 
active development, we have not yet ironed out all the parts of the UI, meaning that the users 
did not find it completely intuitive - in general, there was a number of problems in the flow 
of the UI that our users found, but despite that, they found it still adequately usable.
* <ins>Functionality</ins>\
The functionality of the UI was defined as how much of the UI actually had meaningful functions 
at the current stage of development. As we have mentioned previously, we are still at an active 
stage of development of the application, and as such, we have not yet fully connected the frontend 
of the application with the backend. Because of this, the users were somewhat disappointed that a 
moderate chunk of the UI were still placeholders or did not hold meaningful functionality.

The results of these meeting are summarized in a table below:

|             | Responsiveness | Design  | Natural flow | Functionality |
|-------------|----------------|---------|--------------|---------------|
| Candidate 1 | 3              | 5       | 4            | 2             |
| Candidate 2 | 5              | 4       | 4            | 2             |
| Candidate 3 | 5              | 5       | 3            | 3             |
| _Average_   | _~4.33_        | _~4.66_ | _~3.66_      | _~2.33_       |


## Collaboration with other students

Just for a small promotion we posted a message in a telegram chat about our project, and asked people to
check it out. We weren't expecting such a flow of ideas from people who were interested to help us. 
Some people messages us directly about their suggestions and concerns. One of a feedback 
we received is how models perform on a sentences with several-meanings. Let's take a look on a simple example:
> "I didn't say YOU stole my money" - someone else stole them\
> "I DIDN'T SAY you stole my money" - I said something else

And this could be even applied to a word-only mistake (russian example):
> "Рабочие устали, им нужно передохнУть" - seems right\
> "Рабочие устали, им нужно передОхнуть" - yea... that's bad


Also, some people asked us whether models have language bias. What they meant by that is if took 
non-gendered sentence in one language, that will be gendered after translation, how would model perform?
If an english-speaking user would say "Sam bought some food", and one of an end-gate users will
receive text on russian, is sentence going to be gendered as "Sam купил" (masculine) or "Sam купила" (feminine)?

We need a lot of time to test all this, but we are gratefull to hear such an interesting and important 
ideas from other students on this course. In addition, we would like to thank [Karim Galliamov](https://github.com/KGallyamov),
an amazing ML engineer from "Try this" team, for raising some of these question to our attention.


## Technical improvements

**Backend:**\
This week was spent completing and polishing our core systems:
* Major refactoring of the project structure to be more adaptable and reliable
* Completed users room functionality
* Implemented gRPC client for contact with translation server
* Adapted the code to facilitate OpenApi 2 schema generation from code (for use with swagger and postman)
* Integrated server tests via postman, to check correctness and stability of out system

Right now we are working on updating a several core functionalities:
* Room tests (now with swagger!)
* Redesign database interaction code (to allow flawless concurrency and decrease stress on a database)

In addition, we are planing to make sure Docker image works as expected, and finally we plan to
combine Opus models with a server within the next week.

**TTS licence issues:**\
Last week [we mentioned](https://huggingface.co/rhasspy/piper-voices) that Piper is now available 
on Hugging face, which demonstrated us one of the most important parts. Models licence depends on 
a dataset they were created. And we didn't know that before, so during this week we clicked through
all 100+ voices Piper offers now, through all 22 languages, all different qualities, to separate
non-commercial-use and commercial-use models. Also, it seemed we were the first one to do this, as
we found some issues with either dataset locations or licences mentioned, so we [opened an issue](https://github.com/rhasspy/piper/issues/123) on 
official Piper's repository, and even [contacted creator](https://community.mycroft.ai/t/can-i-use-alan-piper-model-for-commercial-purposes/13744) 
of Piper to help us during this process. 

After filtering all models, we are left with 21 languages (all Swahili models were under their own 
Lanfrica's licence that only permits "non-profit, educational, and public benefit purposes"). And we
already modified our code so that our solution will install only permitted models.

**Connected SST & TTS-STS:**\
This week we combined two major parts of our project - all client-side models. So now we can locally run
speech recognition and speech syntheses withing one laptop. However, we faced some problems during this
part as libraries-dependencies seems to differ, resulting in several conflicts, but with several days of
googling and redesigning - it all works together.

**TTTT language map:**\
We downloaded all existing models for 20 languages that were available in Piper model. Then we 
created a map that describes possible translations between languages in Opus-MT models. Here is a 
map of all language model connections that we wanted to use.

![Opus language map v1](https://i.imgur.com/otFAP3T.png)

How to read: name of a row indicates origin language, name of column says in what language we 
want to receive output.

After close analysis we found out that some of the 20 languages were not provided, for example 
we can see that no model translates to Kazakh, Georgian and Nepalese languages. Because there were 
no ability to make translation to those languages, we decided to exclude them from our project, 
and we got following map:

![Opus language map](https://i.imgur.com/0DLLzUg.png)

We have implemented an algorithm that can make translations between languages that previously 
were not possible. To make this happen, the program finds language that can make connections 
between two languages that haven’t had connection before. For example:
* We can not translate from English to Norwegian, but we can translate from English to Spanish and 
from Spanish to Norwegian. Using this type of logic we can make translations from almost any 
language to any other.

**Application UI:**\
While working on the UI of our project this week, we focused on several tasks related to it:
* Implementing changes from previously received feedback:\
Previously received feedback let us understand the weakest parts of the user experience while 
using our application. Because of this, a sizable amount of time was dedicated to making sure that 
all the feedback was taken in account and the changes were implemented with said feedback in 
mind - some general changes to improve the user experience of the interface.
* Implementing user authentication into the interface:\
Another important part was implementing the user authentication process into the UI. To accomplish 
this, we added registration functionality on the frontend, that lets a user register an account 
with the application, alongside the functionality of logging in with an existing account.
![New UI](https://i.imgur.com/UJelNr4.png)
* Implementing the initial audio sample recording screen, room joining/creating screen and the main “chat” window:\
Lastly, we focused on implementing three more parts of the UI: audio sample recording screen, 
room management and the main application window.\
\
The audio sample recording screen is the screen that appears the first time the user uses 
our application - in this screen, the user records their own voice so that it can be retransmitted 
to other users for the voice cloning process. Additionally, on this screen the user is asked to 
select their language settings, through the previously created language settings screen.\
\
The room management screen is the screen where users are able to choose between creating their 
own “chat” room, or joining an existing one.\
\
And finally, the main application window - in the main application window, a text log of the 
messages in the current chat room is shown to the users. Alongside that, this is the window 
where the users actually hear what other people in the chat room are saying, translated into 
the user’s language and spoken using TTS and voice-cloning.

{{< hint danger >}}
Alright, report is good. Liked the survey data. Noted the absence of the final presentation on the top of the file. Please add that.
Overall, 5 the week! And good luck with the project and the final presentation!

Your team is doing wonders and I am sincerely wishing you success!
If you'll need any support even after project - do not hesitate to contact me.   
Cheers, Rustam
{{< /hint >}}
