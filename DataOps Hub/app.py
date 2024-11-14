# Flask API for model deployment
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Set the model path to root directory
model_path = os.path.join(os.getcwd(), "models/model.pkl")

# Check if the model file exists and load it
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}")
else:
    print("model.pkl not found at the specified path.")
    exit(1)  # Exit if model file is not found


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from the POST request and convert it to a DataFrame
        data = request.get_json()
        df = pd.DataFrame([data])

        # Define the expected columns in the order required by the model
        expected_columns = [
            "SSN",
            "Passport Number",
            "Drivers License",
            "Tax ID",
            "Email",
            "IP Address",
            "MAC Address",
            "Phone Number",
            "Birth Date",
            "Address",
            "City",
            "Latitude",
            "Longitude",
        ]

        # Drop any extra columns that are not in expected_columns
        df = df[[col for col in df.columns if col in expected_columns]]

        # Add missing columns with default values if they are not in the POST request
        for col in expected_columns:
            if col not in df.columns:
                df[col] = 0  # or another default appropriate value

        # Reorder the DataFrame columns to match the expected order
        df = df[expected_columns]

        # Convert all non-numeric columns to numeric values, setting them to a default if needed
        for col in df.columns:
            if df[col].dtype == "object":  # Checks if the column is non-numeric
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        # Debug: Print the DataFrame to ensure it’s correctly formatted before prediction
        print("DataFrame before prediction:")
        print(df)

        # Generate prediction using the loaded model
        prediction = model.predict(df)

        # Return the prediction as JSON
        return jsonify({"prediction": int(prediction[0])})

    except Exception as e:
        print(f"Error: {e}")  # Logs the error to the console
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
