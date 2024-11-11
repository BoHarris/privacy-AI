# Privacy-AI Compliance Classifier 🚀

## Overview
**Privacy-AI Compliance Classifier** is a machine learning model designed to determine if incoming file requests contain **Personally Identifiable Information (PII)**. It uses a **Random Forest Classifier** for classification and provides a **Flask API** for easy integration.

### Features
- 🌲 **Random Forest Model**: Predicts compliance with PII standards.
- 🌐 **Flask API**: Interface for making predictions.
- 📊 **Evaluation Metrics**: Reports accuracy, precision, recall, and F1 score, with a **Confusion Matrix** visualization.

## Problem Statement:
As a privacy compliance tech auditor, I have observed that not all professionals in the technology field can accurately identify Personally Identifiable Information (PII). This gap can lead to unintended exposure of sensitive data, increasing risks for both individuals and organizations.

## Proposed Solution:
One solution is to develop a machine learning (ML) or artificial intelligence (AI) system that can accurately identify PII within datasets and assess the associated risk levels of exposure. Such a system could provide consistent and accurate PII identification, supporting compliance efforts and enhancing data protection.

## Research Background:
The National Institute of Standards and Technology (NIST) defines PII as information maintained by an agency that can distinguish or trace an individual's identity. Examples of PII include a person’s name, Social Security number, and birthplace. According to NIST 800-122, PII also includes any data that can identify an individual when combined with other available information [1, p.2-2].
In contrast, data that pertains to an individual but does not directly identify them—such as aggregated demographics, general geographical data (e.g., city or region), credit scores, device type, and session information—generally falls outside of PII’s scope. As outlined in NIST's publication, data is classified as "traceable" or "linkable" if it contains enough identifiable information to distinguish an individual through their online activities (NIST, 2009, p. 4). Traceable data directly identifies an individual, while linkable information refers to data that, when logically combined, could reveal an individual’s identity [1, p.2-3].

## Outline of PII Data guideline: 

1. Name
   1. Full name
   2. Maiden name
   3. Mother’s maiden name
   4. Alias
2. Personal Identification numbers
   1. Social Security number
   2. Passport number
   3. Driver’s license
   4. Tax Payer
3. Address information
   1. Street Address
   2. Email Address
4. Asset information
   1. IP address
   2. MAC address
   3. Host specific persistent identifiers that links to a particular person or a small well defined group of people
5. Telephone numbers
   1. Mobile
   2. Business
   3. Personal
6. Personal characteristics
   1. Photographic images containing
      1. Face
      2. Distinguishing marks
        1. Scars
        2. Tattoos
    3. X-rays
       1. Dental
       2. Bone structure
     4. Biometrics
          1. Retina scan
          2. Voice signature
          3. Facial geometry
 5. Fingerprint
 6. Information identifying owned property
       1.   Vehicle registration number
       2.   VIN
       3.   License plate
       4.   Title record
       5.   House deed
       6.   Mortgage and Loan Information
  7. Serial Number for personal assets
      1. Electronics
      2. Bikes
      3. Jewelry
  9. Information about an individual
      1. Birth information
           1. Date
           2. Location
           3. Race
       2. Religion
       3. Weight
       4. Activities
       5. Geographical indicators
       6. Employment information
            1. Employee ID
            2. Job title
            3. Work contact information
            4. Payroll information
            5. Performance
            6. Certifications and Professional Licenses
            7. Emergency Contact information
            8. Tax Documentation
          
Additional PII not outlined in NIST's guidelines

  10. User Generated Content (UGC)               
  11. User Generated Content Personal Information in the following
  12. Photos and videos
       1. Faces
       2. Background details with traceable details
       3. Street signs
       4. Businesses
  13. Voice Recording
  14. Posts containing
  15. PII see above
  16. Tags and mentions
  17. User name
  18. Timestamped content

## Automated PII Detection Using Machine Learning
This project documents a machine learning approach designed to automatically identify Personally Identifiable Information (PII) within structured datasets. The goal is to provide organizations with a streamlined, automated tool to help improve data governance, privacy  data protection efforts by flagging potentially sensitive data.

### This model achieves PII detection by focusing on these key components:

#### Structured Data Analysis for PII Detection:
The model assesses structured data features, such as demographic and financial attributes, to detect indicators of PII. By analyzing patterns in these attributes, it can classify data as sensitive or non-sensitive. Unlike more advanced systems that use Natural Language Processing (NLP) to analyze unstructured data, this model is optimized for structured data formats, providing a practical solution for databases and tabular data[2].

#### Supervised Learning for Binary Classification:
This model uses a supervised machine learning approach[3], specifically a Random Forest Classifier, to determine the sensitivity of data. The model was trained on labeled datasets with examples of sensitive and non-sensitive records, enabling it to learn distinguishing patterns. The output is a binary classification indicating whether the dataset likely contains PII (1) or does not (0), allowing for straightforward interpretation.

#### Feature Selection and Encoding:
Key features were selected and encoded to improve the model's accuracy in identifying sensitive data. By preprocessing categorical data (e.g., gender, age ranges, or income categories) and normalizing numerical features, the model can focus on patterns relevant to sensitivity. This setup allows it to detect fields that, individually or in combination, could identify individuals.

#### Sensitivity Classification Output:
Rather than assigning detailed risk scores, the model provides a simplified binary output—either sensitive or non-sensitive. This basic classification approach supports organizations in quickly filtering datasets for further review and implementing privacy safeguards for high-risk data.
Scalability for Retraining and Enhancement:
While this model does not include continuous monitoring or adaptive learning, it can be periodically retrained with new data or updated regulations to maintain relevance and accuracy over time. Future iterations could incorporate additional features for real-time risk assessment or nuanced sensitivity scoring, as needed.
By leveraging machine learning for automated PII detection, this project offers a practical solution for identifying sensitive data within structured datasets, helping organizations prioritize data protection efforts and meet privacy compliance standards more effectively.


#### References: 
[1] National Institute of Standards and Technology, "Guide to Protecting the Confidentiality of Personally Identifiable Information (PII)," Special Publication 800-122, Apr. 2010. [Online]. Available: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-122.pdf
[2] IBM, “Structured vs unstructured data” 29 June 2021 [Online] Available: https://www.ibm.com/think/topics/structured-vs-un 
[3] Isha Salian Salian, Isha, Nvidia.Com, “SuperVize Me: What’s the Difference Between Supervised, Unsupervised, Semi-Supervised and Reinforcement Learning?’, 2, August 2021



## Project Structure

```plaintext
privacy-ai/
├── app.py                    # Flask API for deploying the model
├── ml/
│   ├── train_model.py        # Model training and saving
│   ├── evaluate_model.py     # Model evaluation functions
│   ├── features.py           # Feature engineering and preprocessing
├── resources/
│   └── processed/            # Processed training data
└── model.pkl                 # Trained model file
Usage
Train the Model

shell
Copy code
python ml/train_model.py
This script trains and saves the model as model.pkl.

Start the API

shell
Copy code
python app.py
Launches the Flask API on http://127.0.0.1:5001.

Make a Prediction

shell
Copy code
curl -X POST http://127.0.0.1:5001/predict -H "Content-Type: application/json" -d '{"Pclass": 3, "Sex": 1, "SibSp": 0, "Parch": 0, "Fare": 35.0, "Normalized_Age": 0.5}'
Response: { "prediction": 0 } where:

0 = Non-Compliant
1 = Compliant
Evaluation Results 📈
Metric	Score
Accuracy	95%
Precision	94%
Recall	90%
F1 Score	92%
Confusion Matrix
![image](https://github.com/user-attachments/assets/000c0dba-cdf9-4de9-8688-a0cde00a4841)


Dependencies
Make sure to install the necessary Python packages:
Flash
Pandas
Seaborn
numpy
scikit-learn
joblib
matplotlib
Requests Testing (Optional):
requests

License 📜
This project is open-source under the MIT License.

Future Work 🔮
Hyperparameter Tuning: Explore additional tuning methods for better accuracy.
Additional Model Testing: Experiment with other classification models for performance comparison.
Expand Features: Add more features for even better prediction accuracy.
