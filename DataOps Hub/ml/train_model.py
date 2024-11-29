from evaluate_model import evaluate_model, plot_confusion_matrix
from features import prepare_features
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import logging
import os
import sys

#Configure logging
logging.basicConfig(level=logging.info, format="%(asctime)s - %(levelname)s - %(message)s")

#Paths
DATA_PATH = "resources/processed/processed_sensitive_data.csv"
MODEL_DIR = "models"
MODEL_FILE = "model.pkl"

def load_data(file_path):
    """Load the processed dataset"""
    try:
        logging.info(f"Loading data from {file_path}")
        return pd.read_csv(file_path)
    except FileNotFoundError:
        
