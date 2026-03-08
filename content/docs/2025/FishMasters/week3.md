---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

- User login and registration, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/43)
- Name of the profile, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/62)
- Picture in the profile, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/62)

- Possibility to rotate the map, (was implemented on previous week)
- Possibility to open labels with fish pictures on the map, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/56)
- Adding fishing places, [PR back](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/41)
- Possibility to start the event of fishing, [PR Front](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/66), [PR Back](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/41)
- User interface to add pictures of fishes, [PR Front](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/51), [PR Back](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/52)

- Test model for ML, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/60)

## Demonstration of the working MVP

Link to the video: [Google drive](https://drive.google.com/file/d/1TnywiUV9pFK4W7nPgpUDDVc1hI2_WKPa/view)

## ML

*Remove this section if not applicable*

**Link to dataset**: [Link](https://disk.yandex.ru/d/1UGiENnMIG0OSg)

We build UML diagram for the ML part and started implementing some parts of it: 
- Vector DB: Based on Quadrant cloud solution, to store ready embeddings
- Fish Speices class: to store all information about row in one place
- Data preparation: to prepare data for tokenization in our embedder


**Links to the initial model artifacts**: [Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)

## Internal demo

All needed comments were provided on the video.

# Weekly commitments

## Individual contribution of each participant

Stepan Vagin:
- Created UML of the architecture, [Link](https://mermaid.live/edit#pako:eNqtWW1P4zgQ_itRpJVaXVkBhS5EupN42zsE9Niyux9OSCc3mbY-Eidnu7DdFfz2m9hOsB23RatDojTJvHlm_Mzj8CNOywziJE5zIsQ5JXNOinsW4Y-6E30RwC-ZBD4jKUQ_9KP65xcBhKeLT0vgqyQSklM2t55mVFQ5WU1ALHMpelz_TaJrKuTLRyoWdxWkFMRL31JaEJbloF1WS9mzn4lF-VTrnYMkNBc9ofWTyDJm5J_vmb0EFeItL1MQouTOGtIcCNO-_rUX0g-sqOJQaSM9Cd_kJtEcioJI-h1_S7ZVmkNRPsKdLKunkmfbrT-SnGZEglpXJ-5pWdaLCmbiophClqHcDRY9dzJR1HeS6NMTMC0F3Ho6BwYcXbYG_CC_QipLW2NKZLpwxZvqa6WXvrnUqi92-kqSqQidBqBsBhxYCpt8ewu-usFUiO5qH5KIMhn9Gh3u7u46_bAU2OtNpGf60o5tRmUPmmUJdwl9t1symlqyTZwYsDHr5FdOIIdHwqR5KIKa66JCzXyJ9emhzAzTJ8PZGI83pGLPTgQDOl9MSx7asW_MxiDKyRTybXt-Rlk2brytX_SaADaleZPe2xKmTZ0TSaZEuOg3Q7sX1spvSPWCeRxE3XY2SHWDwIXblliya4ITaAC6SxpERWvCBj1VwA4wa2C46BpBnLlSKltStKwyZ8fTTGkNom6ubdzHNg5ohZHZ8hxMcloyhh4QRJOoEThr77n75yTPjaneloWhsLl7urpEvKVZ06MY6MubstJ42jCElDTJso2i4dKdrsakgB7DDwvm1kS1PqVOKk0d7C1umben0VIIStg4_DQDkXJa6ZJ0ni7IlEoiA08E_R4yl5Z5yQP3Z2WZ3XIwgC-CQ3MejgGr-3GZ5-evgfZCQ1SW5zVu9PVu1I8HUTn9B3srnNm6AcMsosaCujVPbi91eU_1he2O4xzKiaxX-7n97gCZsjwhT7Wfnt7lquR4q7a5rTEbD7Cl4ayrwIDH2CjDVKgg-irW9lqADLAQP1wH5zfTEc-4k1NZPzsPm-1GgVXeLitByO1SS2SfNbNSqbP5ioPoOQ4-Xvs148Pb9F-MEZ-eBTJ-t2JyAZKmxmmLXo5bL3O3euzhsu-AP1KPmYND8xKP9tmzv2jpUWJzJVuEsea5YQ929vV8PE28SRkY0D5N3VQCxR1vLcVOLRoDHSu2mcVqyml2Z03DN_rHnfSw_eAyiN5o06sd8gBOU3GhGYh_ICF5uqx3MS4_pQILfCKvelVbbhPIIJrzcsmyvyVfykVz76EZ6xajca1OAL_m_6vJm8nkbcY2GRmfn_3-01ZaLmfOMDfXqk-R6bQb_rP5hiiDBkzq0ZGpcrhOJaNYHixtaI-lOU0fJui1G49AHK8BaakAgnUFMk5nEs-xas8gs7EvnWPQvD19E5UXt4sHkQoCGoqxloVkyrZy02PwZGFgc3DxcNoBKNOvE6hKrgemfcPGvRy4_JOdsLJAVK6RbE1esTgK-oF3IV-j0Poj1jqc0srj8U8dR4LgtlhVwCvCkQhhAT4v60nVaTH1XNP_fnvbbhNeCvHVjMqOth6b3hgMdLggj6APxF3_9cboTpfXI7Qj4YUY4I6GujiFIRW9gtBLnhrrv0yuwyys5dgTRdV6LmPre-wmqOu967nMGjQyWh3m3HCfIDIHXNX9fU0LKv9Qb554p2XfvYvwYK72sVjQyiCF-1JsZ-c37x1TEiGLWCvbGd5JVKOykdef3jurWu3Cm-oCWCYiwxsh09PItuG97altuGO6ThCeNMXric6JoUsyQmG8rjQsb23XNwibbbhd0l-JoQmbVAKnzSTiNZjBIyYh081mZ8B-fRRySlKVe6PTvl7ZLqo_vdcLXoxtdZpTv1YKnZk7mgVhZO46c48vjcZpc2yZAXKuOguto66CB1TYthxwA4lNDtqQmkZ1gnJmQadbFKaLdZJtq2wU68T82lgdWZ-Z2cJGxedua_ZzQ0m8xfqEYo12oQXFJrVwrFE8iOdIeuMEKRMM4gJ4QerLWOH5fYxHjQLu4wS_ZjAjSH7u43v2jGoVYX-VZdFoIvGaL-JkRnKBV_qth_n3QCuCAAT8DBmajJNDZSFOfsTf4uR49H7_YPd49GG4d7A33BsO4lWc7AwP3h-Njj6MjofDo_3do_3D50H8Xbnce793dDA62N0_Ohoe7h-PRsPn_wAwMBsj)
- Created classes FishSpeices, VectorDatabase, to connect to vector DB, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/65)
- Created first ML endpoint, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/60)
- Updated backlog, [Link](https://github.com/orgs/IU-Capstone-Project-2025/projects/19)

Kostya Zimin:
- fix db migrations and add liquibase, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/57)
- refactor all controllers for useful explanation in swagger and create API contract, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/55)
- fix all methods in service part and add more exceptions, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/58) 
- fix sql codes, db relationships and docker-compose file for back part

Ivan Vasiliev:
- defined the architecture of search system with Stepan Vagin(discussed which models, dataset to use, workflow)
- developed preprocess of the data, added embeddings of the data [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/67)
retrieved datasets from the data_prep.py, [Link](https://disk.yandex.ru/d/1UGiENnMIG0OSg)
- worked on localization of the dataset, compared different models(Helsinki-NLP/opus-mt-en-ru, facebook/nllb-200-distilled-600M, mistral-7b-instruct-v0.1.Q4_K_M.gguf) mess work can be found here, [Link](https://colab.research.google.com/drive/1ppwNaTgdo2aXw3f1GOrXNHJugJ6pC3_9?usp=sharing)

Kirill Greshnov:

- Connect login and registration with backend, add page for fishing event with statistics, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/43)
- Add local image upload for fishing event, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/51)
- Add feature to choose fishing location, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/56)
- Add functionality to profile page to show actual user data, minor design changes, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/62)


Egor Belozerov:
- containerize the ML part + add it to deployment, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/commit/c51f571771ddcc5a9daf666ae269159896ae0211)
- additional build and linting flutter app, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/45)
- fix 301 status code for https endpoint, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/46)
- deploy the backend, [PR](https://capstone.aquaf1na.fun/swagger-ui/index.html#/)
- fix the issues with runner and sops (recreate the encryption keys)


Damir Sadykov:
- Started working on final app design (some screens are done, some sketches for other were made, color palette with fonts has been selected) in Figma: [Link](https://www.figma.com/design/DBMIs26GU4KfwtITxK8BPT/FishMasters?node-id=0-1&t=251Gacni5ihDyEa8-1)
- Research in automated tools for design travel from Figma to Flutter (plugins: "Figma to Flutter", "Figma2Flutter", "Supernova", tools: "FlutterFlow"). Result: no plugins are good enough for this purpose (lot's of bugs) and tool FlutterFlow is good for transfer design to flutter code.
- FlutterFlow design for first screen are made, [FlutterFLow](https://app.flutterflow.io/project/fishing-so9fix) (subscription required, so screenshots are made (in same Figma file: [Figma](https://www.figma.com/design/DBMIs26GU4KfwtITxK8BPT/FishMasters?node-id=0-1&t=251Gacni5ihDyEa8-1 ))
- Fishing event related requests handle are made: fishing event is now ready, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/66)
- Pictures of catches upload request handled too, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/66)

Adel Gaznanov:
- Сreate endpoint to add new water places on the map, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/42)
- Сreate endpoints to start and end fishing on the specific water place, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/41)
- Сreate an opportunity to save caught fish during fishing, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/52)

## Plan for Next Week

- Start to implement features, meant for final project
- Continue building ML architecture
- Fixing bugs

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).