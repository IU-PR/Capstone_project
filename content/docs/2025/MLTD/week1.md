# Week #1

## Project Description

### Project name: MLTD

**Code repository:** https://github.com/IU-Capstone-Project-2025/MLTD

Threat Detection Tools and APIs can cost money and can be vendor exclusive. MLTD is a threat detection API used for detecting any cyber threats in log files. It allows users to host the API locally on any hardware and detect any kind of threat. MLTD uses machine learning to find any threats from user-provided log files. Users can upload their log files using a frontend web interface, the command line, or scripts. The backend will check for any threats and send any results back to the user.

## Team Members
| Team Member | Telegram Alias | Email Address | Track | Responsiblities |
|-------------|----------------|---------------|-------|-----------------|
| Paramon Yevstigneyev | [ParamonPlay2205](https://t.me/ParamonPlay2205) | p.yevstigneyev@innopolis.university | Backend | Team lead, management, Backend API developer |
| Bulat Fakhrutdinov | [Bbolo4ka](https://t.me/Bbolo4ka)| b.fakhrutdinov@innopolis.university | Frontend/ML | Machine Learning developer, Frontend Developer |

## Brainstorming

### Project ideas:
- Utilize supervised or unsupervised machine learning to detect threats. Supervised machine learning is commonly used for classification, which in this case it will classify whether or not a threat exists in a log file. On the other hand, unsupervised machine learning can be used to detect unknown threats.
- A backend API that would recieve log files from users. Having the threat detection engine integrated with an API would allow threat detection to be automated with scripts.
- Allow the machine learning model to be trained with data that contains existing threats to improve threat detection.

### Market Research
* Palo Alto Wildfire is popular cloud-based malware analysis engine that utilizes machine learning to detect known and unkown malware. However, Palo Alto WildFire can only be used on Palo Alto Firewalls, which are known to be very expensive. And also require sepreate licenses in order to use certain features. Which may not be ideal for small or medium sized businesses who are trying to secure their networks and systems.
* Apache Spot is a platform for analyzing network data and logs using ML to detect anomalies and threats. It is primarily focused on network traffic analysis and only partially supports other types of logs, unlike MLTD, which can handle any logs. MLTD also has a simple interface for uploading logs and viewing results, unlike Apache Spot, which has an interface based on Jupyter Notebook + Kibana, which requires technical skills.

## Basic Requirements

### Target Users and their needs
The target users are System/Network administrators and Cybersecurity Analysts who want to check for any threats with system and network activity.

### User Stories 
1. "As a system administrator, I want to be able to check for any suspicious system activity to prevent a cyber attack."
2. "As a network administrator, I want to discover any threats on the network so that I can prevent unauthorized network access."
3. "As a cyber security analyst, I want to be able to find any cyber threats so that I can help find vulnerabilities, misconfigurations, etc."


### Initial Scope
An API with basic functionallity that would parse log files containing system and network activity. The API shoud be able to recieve log files by using a frontend web interface, scripts, and a command line interface.

## Tech-Stack

**Backend Stack:**
- Python: A popular programming language for data processing and building APIs.
- FastAPI: A popular and easy to learn Python library for creating APIs.
- scikit-learn: Since the backend API will be written in python, we decided to scikit-learn to make integrating machine learning into the API easier.

**Frontend Stack:**
- NextJS: A popular JavaScript framework that uses react to create web interfaces.

## Weekly Commitments
Paramon helped with orgainizing the group, wrote the report, setup the repositories, and creating boilerplate code. While Bulat helped with deciding when to have weekly meetings, helped make role distribution more even to ensure equal contribution, helped with coming up with ideas, and helped decide what machine learning and frontend frameworks to use.
