from evaluate_model import evaluate_model, plot_confusion_matrix
from features import prepare_features
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import sys
import os

# Load data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
df = pd.read_csv("resources/processed/processed_sensitive_data.csv")
X, y, selected_columns = prepare_features(df)

# Check if features and target variable are valid
if X is None or y is None:
    print("Error: Features or target variable is None. Please check data processing.")
    sys.exit(1)

# Split features and labels
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Verify the splits are not empty
if X_train.empty or X_test.empty or y_train.empty or y_test.empty:
    print("Error: Training or testing set is empty after split.")
    sys.exit(1)

# Initialize the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Hyperparameter tuning
param_dist = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 10, 20, 30],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "max_features": ["sqrt", "log2"],  # Adjusted to avoid deprecated "auto" setting
}

# Set up RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=10,
    cv=2,
    scoring="accuracy",
    random_state=42,
    n_jobs=-1,
)

random_search.fit(X_train, y_train)
best_model = random_search.best_estimator_

# Evaluate the tuned model
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Best Parameters:", random_search.best_params_)
print(f"Model Accuracy after Tuning: {accuracy:.2f}")

# Evaluate and plot confusion matrix
evaluate_model(y_test, y_pred)
plot_confusion_matrix(y_test, y_pred)

# Save the model to a models directory
output_dir = "models"
os.makedirs(output_dir, exist_ok=True)
model_path = os.path.join(output_dir, "model.pkl")
joblib.dump(best_model, model_path)
print(f"Model saved as {model_path}")
