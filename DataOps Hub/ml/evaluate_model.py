import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import seaborn as sns


def evaluate_model(y_true, y_pred):
    """Calculate and print basic evaluation metrics"""
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print(f"Accuracy: {accuracy: .2f}")
    print(f"Precision: {precision: .2f}")
    print(f"Recall: {recall}.2f")
    print(f"F1 Score: {f1: .2f}")

    return accuracy, precision, recall, f1


def plot_confusion_matrix(y_true, y_pred):
    """Plot the confusion matrix"""
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Non-Compliant", "Compliant"],
        yticklabels=["Non-Compliant", "Compliant"],
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()


def cross_validate_model(model, X, y, cv=5):
    """Perform cross-validation and print the average accuracy"""
    scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
    print(f"Cross-Validation Accuracy (average of {cv} fold): {scores.mean(): .2f}")
    return scores
