import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# load prepared feature and labels
from .features import prepare_features
from .labels import create_compliance_labels

# load data
df = pd.read_csv("resources/processed/processed_train.csv")

# Prepare features and labels
df = prepare_features(df)
df = create_compliance_labels(df)

# Split features and labels
X = df.drop(columns=["compliance_label"])
y = df["compliance_label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize model (Starting RandomForest)
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy:2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall: .2f}")
