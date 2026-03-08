# **Week #3**

## Implemented MVP features

1. **Log Upload Functionality**.

   Description: Users can upload .log files (only for HDFS) containing raw system logs.

   Purpose: This is the entry point of the user journey.

   Implementation: Frontend + backend endpoint for file upload.

   PR: Add log upload endpoint

   Issue: Users need to upload logs for analysis
  
2. **Preprocessing Pipeline**.
   
   Description: Uploaded logs are automatically parsed into a structured csv format.

   Limitation: Works with HDFS (Hadoop Distributed File System) log files.

   Aggregate or convert logs into a model-friendly format.
   
   PR: Implement log preprocessing pipeline
  
   Issue: Parse and normalize log files

3. **Model Inference**
   
   Description: Use a trained Decision Tree to predict whether the block is normal or anomalous.

   Limitation: Works with HDFS (Hadoop Distributed File System) log files.
   
   Output: Probability prediction ∈ [0, 1] (the rate of anomalous blocks in log file)

   PR: Model inference pipeline

   Issue: Integrate ML model for prediction

**Functional User Journey**

* User uploads a log file.

* System parses logs, encodes features, and performs inference.

* Anomaly detection model analyzes data.

* User receives report with predictions.. 


## Demonstration of the working MVP
![](img/MVP_Demo_Screenshot_1.jpg)
![](img/MVP_Demo_Screenshot_2.jpg)
![](img/MVP_Demo_Screenshot_3.jpg)
![](img/MVP_Demo_Screenshot_4.jpg)
![](img/MVP_Demo_Screenshot_5.jpg)

## ML


**Link to the training code**: *link*

The goal of the model is to detect anomalies in system log data (for HDFS) using classification techniques. An anomaly may indicate a system error, potential cyberattack, or unexpected behavior.

* Model Selection
    - Model: DecisionTreeClassifier from scikit-learn

    - Reason for choice: This model was chosed due to interpretability, fast to train, handles sparse categorical input (like event type counts). Also this model showed slightly better results than Logistic Regression, Rando Forest, AdaBoost

* Training dataset
    - For training dataset preparation we firstly used structured dataset Event_occurence_matrix.csv from [loghub repo](https://github.com/logpai/loghub/tree/master)

    - Original logs parsed and converted into a structured format:
            
       - BlockId or log ID as the unit of grouping  
       - EventId (e.g., E1–E29) as features
       - Label (0: Normal, 1: Anomaly)
    - This dataset was converted to more diverse dataset to solve the problem of the imbalance in the distribution of features between learning and inference. Each row represents either:
  
        - A full block (multiple events grouped by BlockId)
        - Or a medium chunk of logs (for medium-data simulation)
        - Or a small “chunk” of logs (for low-data simulation)
   - Example of feature row, where numbers are counts (or presence/absence) of each EventId (E1–E29) for each block:
            E1=0, E2=0, E3=2, E4=0, E5=1, ..., E29=0, Label=1
    - Results was saved to hybrid_training_dataset.csv. The model was trained on this data.

## Internal demo

Ml model:
 * The model tends to over-predict anomalies on short or “thin” log blocks
 * There were many false positives outputs that why recall and f1 were not high
 * Necessary to add support for different log types
UI :
 * We need to choose more readable colors.
# Weekly commitments

## Individual contribution of each participant

Bulat:
  - [Data preparation and Feature extrraction](https://github.com/IU-Capstone-Project-2025/MLTD/commit/3a99c214b700918b99db984884c12c55ae3c5247#diff-bdd58e541d0df8e2df97349e2097a44062e17f9fc97f96c876f66e205d5616e0)
  - [Raw input log Parser](https://github.com/IU-Capstone-Project-2025/MLTD/commit/bf851ec0659d53106a6f13a134cc55fb114d70b8#diff-905db344f9a9a03e36d0361f83d77d2bdb63d76e04c09b88b0b7c54514ff53fb)
  - [Model training](https://github.com/IU-Capstone-Project-2025/MLTD/commit/3a99c214b700918b99db984884c12c55ae3c5247#diff-5ee14f62bd52e0d068d070f38b5a90ade10a9d416f55cb196a5aa4d4ee5e104f)
  - [Model testing and inference](https://github.com/IU-Capstone-Project-2025/MLTD/commit/bf851ec0659d53106a6f13a134cc55fb114d70b8#diff-6b663448c0dfe959e3bd260768c35e14c02bf40921f4ecfb87245d9e45229ca3)

Paramon:
  - [Frontend](https://github.com/IU-Capstone-Project-2025/MLTD/commit/ac59b033fdc3b87d884db3b39d5a78ef396c4a91),
  - [API usage information](https://github.com/IU-Capstone-Project-2025/MLTD/commit/51d8a5bead856869994259365978b79853cf595b)
  - Report
    

## Plan for Next Week
 - Improve performance of current model (especially recall / F1)
 - Add support for other log types (e.g., BGP, Linux system logs, macOS)
 - Add parsers for other log types
 - Make the user interface more intuitive, responsive, and informative — especially for uploading logs, viewing results, and understanding model predictions.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
