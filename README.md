# Privacy-AI Compliance Classifier 🚀

![Confusion Matrix](![image](https://github.com/user-attachments/assets/1cb0b01e-014c-41b2-8792-d13b2ccb326a)
)

## Overview
**Privacy-AI Compliance Classifier** is a machine learning model designed to determine if incoming file requests contain **Personally Identifiable Information (PII)**. It uses a **Random Forest Classifier** for classification and provides a **Flask API** for easy integration.

### Features
- 🌲 **Random Forest Model**: Predicts compliance with PII standards.
- 🌐 **Flask API**: Interface for making predictions.
- 📊 **Evaluation Metrics**: Reports accuracy, precision, recall, and F1 score, with a **Confusion Matrix** visualization.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Evaluation Results](#evaluation-results-📈)
- [Dependencies](#dependencies)
- [Future Work](#future-work-🔮)
- [License](#license-📜)

---

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


Dependencies
Make sure to install the necessary Python packages:

shell
Copy code
pip install -r requirements.txt
License 📜
This project is open-source under the MIT License.

Future Work 🔮
Hyperparameter Tuning: Explore additional tuning methods for better accuracy.
Additional Model Testing: Experiment with other classification models for performance comparison.
Expand Features: Add more features for even better prediction accuracy.

