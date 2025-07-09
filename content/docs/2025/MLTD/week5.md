# **Week #5**

## Feedback

### Sessions

User 1: Network Administrator at a small business

  - Feedback:

    Wanted real-time alerting instead of batch processing.

    Liked the file upload simplicity.

    Mentioned that interpreting the probability score was unclear — suggested using labels like "Low", "Medium", "High Threat".

User 2: Cybersecurity Analyst (Freelancer)

  - Feedback:

    Liked the simplicity of the web interface.

    Wanted support for Mac syslogs or Apache logs (not just HDFS/BGL).

    Mentioned the need for visual analytics.

User 3: IT Support Technician (Kazan Federal University)
 
  - Feedback:
  
    Wanted command-line automation examples in the documentation.
  
    The colors were not quite well chosen, which makes the text difficult to see at times.

### Analyze

* The highest priority issue was support for Mac os system log files.
* The medium priority issues are visual analytics and inappropriate colors.
* The lowest priority issues are interpretation of the probability estimate, command-line automation examples in the documentation, and real-time alerting support
## Iteration & Refinement

### Implemented features based on feedback

* Added support for Mac os system log files
* Changed user colors and user interface

### Performance & Stability

| Metric                     | Description                                                | Current Status                                            |
| -------------------------- | ---------------------------------------------------------- | --------------------------------------------------------- |
| **Inference Time**       | Time from file upload to prediction                        | \~2s for avg log file (\~300 lines)                     |
| **Accuracy - F1 Score**  | ML model performance (on HDFS and BGL logs)                | Accuracy (HDFS: 98%, BGL: >99%), Precision (HDFS: 88%, BGL: >99%), Recall (HDFS: 36%, BGL: >99%), F1 Score (HDFS: 51%, BGL: >99%)                        |                                 |

### Documentation

 * [README.md](https://github.com/IU-Capstone-Project-2025/MLTD/blob/main/README.md) file	explains the idea of the application and the problem it solves, project setup, dependencies, and usage.


### ML Model Refinement

- This week was implemented model for Mac OS system log files. Until Friday we preprocessed data and  created parser for raw log files. Then we trained unsupervised Isolation Forest model and got distribution of anomaly degrees of each log line in training data. Based on it was chosen threshold = 0 for classifying anomaly. Next weeks we'll add 1 or 2 models for other log file types (Windows/Hadoop) and improve HDFS model performance (need at least 70 for accuracy, precision, recall and f1-scroe).

# Weekly commitments

## Individual contribution of each participant

Paramon:
- Added [options to select log formats](https://github.com/IU-Capstone-Project-2025/MLTD/commit/36d164a7f22a03f9859b6e25a64e71200658e195) in the web interface and API.
- Updated [setup documentation](https://github.com/IU-Capstone-Project-2025/MLTD/commit/d9c54090c72908ad81a26f3d6883bcccbe0cea1a) for running the application.
- Wrote the weekly commitments and plans for next week in the [report](https://github.com/PYP2205/MLTD/commit/b7d1ce8bc34ad04fc05d20050266fdbf72df6a6f).

Bulat:
- Created parser and ML model for the [MAC log format](https://github.com/IU-Capstone-Project-2025/MLTD/commit/6dca6e3085bf5513f79de822270ba2a457275ec1).
- Wrote most of the [report](https://github.com/PYP2205/MLTD/pull/6).

## Plan for Next Week
Next week we have plans to:
- Make a new model and parser for Windows logs.
- Test the system for any potential bugs.
- Improve the web user inferface.
- Improve HDFS model performance.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
