# **Week #6**

## Links
- **API Docs**: https://github.com/IU-Capstone-Project-2025/MLTD/blob/main/README.md
- **Demo**: https://drive.google.com/file/d/1_nqGQkMYLtU_vDzGvbLanDaIURegFIEg/view?usp=drive_link

## Final deliverables

### Project overview

MLTD is a threat detection API used for detecting any cyber threats in log files. It uses machine learning to find any threats from user-provided log files. Users can upload their log files using a frontend web interface, the command line, or scripts. It supports HDFS, BGL, MAC, and SSH log files by now.

### Features

- Treat detection model for HDFS log file.
- Treat detection model for BGL log file.
- Treat detection model for MAC system log file.
- Treat detection model for SSH log file.
- Uploading log files using a frontend web interface or the command line.
- Analysis output: the number of abnormal lines, the total number of lines in the file, the percentage of abnormal lines, and a label indicating whether the file is abnormal.

### Tech stack

* Frontend: NextJS, ShadCN, React.js

* Backend: Python (FastAPI), Node.js (Express)

* ML/DL: PyTorch + Transformers (BERT)
  
* EDA and data preprocessing: numpy, pandas, matplotlib

* Utilities: tqdm, pickle, re
  
* Infrastructure: Docker

* Tools: GitHub Actions (CI/CD), Sentry (логирование ошибок)

### Setup instructions

#### Requirements
To run MLTD with Docker:
- Docker
- Docker Compose

To run MLTD natively:
- Nodejs 24
- Python 3.13

Clone the repository:
```
git clone https://github.com/IU-Capstone-Project-2025/MLTD
cd MLTD
```

Download the BGL Model:

The model was too big to be stored on GitHub, so you will need to download the model [here](https://drive.google.com/file/d/1miVZN5arMReuDLH0e9Pjmd7SIeJEXdaM/view?usp=sharing). After it has finished downloading, extract the ZIP archive and move/copy the "saved_model" folder to "MLTD/backend/ML/BGL".

#### Run MLTD in production mode with Docker Compose:
```
docker compose up -d
```

#### Run MLTD natively:

##### Frontend:
Install dependencies:
```
cd frontend
npm install .
```

Run development build:
```
npm run dev
```

Run production build:
```
npm run build
npm start
```

##### Backend:
Install dependencies:
```
cd backend
pip install -r ./requirements.txt
```

Run development build:
```
fastapi dev ./main.py
```

Run production build:
```
fastapu run ./main.py
```

### Interacting with the API using the web interface
Open any web browser that you use (ex. Google Chrome, Microsoft Edge, Mozilla Firefox, etc.) and enter "http://localhost:3000/" if you are running MLTD localy on your machine. If you are running MLTD on a different machine then enter "http://[Hostname/IP Address]:3000/". Next you click on the box that saya "No file selected." and select a .txt, .log, or .csv file that contains system or network activity. Once you have selected a file, you click on "Upload" and the file will be uploaded to tbe backend API. Then you click on "Log format" to select the type of logging format that is contained in the file (BGL, HDFS, MAC, SSH). Finally after you have selected the appropriate log format, you can click on "Analyze" and wait for the results. After file analyzation has finished, you should see results containing the numbers of lines contained in the analyzed file, the number of anomalies found, and the probability that threats are present.

### Interacting with the API using a terminal/command line interface
Open any terminal (ex. Windows Terminal, PowerShell, Command Prompt, etc.) and do the following:
```
curl -X POST -F "file=@path/to/log/file" http://[Backend API IP Address]:8000/upload
curl http://[Backend API IP Address]:8000/analyze/[File name you uploaded]?format=[format of the log]
```

## Presentation draft

[link to the presentation](https://docs.google.com/presentation/d/1Wpvt7F_ewtAw89_3wM9kyxg3gsAN_Xc0H7WS-LHt1Q8/edit?usp=sharing)

# Weekly commitments

## Individual contribution of each participant

Bulat:
- Created [parser and ML model](https://github.com/IU-Capstone-Project-2025/MLTD/commit/686ed0db84e0430a69bf5dda3cb56b6e6df29803) for the SSH log format.
- Wrote the [report](https://github.com/PYP2205/MLTD/pull/7/files).

Paramon
- Added [progress indicators](https://github.com/IU-Capstone-Project-2025/MLTD/commit/30125fe57d00ad534affce202d9759f6e91595df) to the frontend (as suggested by our TA).
- Added a component for displaying [results](https://github.com/IU-Capstone-Project-2025/MLTD/commit/30125fe57d00ad534affce202d9759f6e91595df) to the frontend after the file has been analyzed.
- Made the [backend API support](https://github.com/IU-Capstone-Project-2025/MLTD/commit/d8b0a8600bbf82f71000caa6a04f021d50a268d5) the SSH ML model.
- [Made every model return]((https://github.com/IU-Capstone-Project-2025/MLTD/commit/686ed0db84e0430a69bf5dda3cb56b6e6df29803)) the amount of lines and anomalies along with the probability of a threat for the results of file analyzation.
- [Updated the README](https://github.com/IU-Capstone-Project-2025/MLTD/commit/bae5460d12af5e0c467118c503dbd769c43d9999) to organize setup and usage instructions. And added instructions on how to use the API from a command line interface.

## Plan for Next Week

Next week we have plans to:
- Test the system for any potential bugs and fix them.
- Create a presentation of our product and prepare for defense.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
