import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.feature_selection import SelectKBest, mutual_info_classif


def encode_data_type(dataframe: pd.DataFrame, column_name: str) -> pd.DataFrame:
    label_encoder = LabelEncoder()
    dataframe[f"{column_name}_encoded"] = label_encoder.fit_transform(
        dataframe[column_name]
    )
    return dataframe


def normalize_feature(dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:
    scaler = MinMaxScaler()
    dataframe[columns] = scaler.fit_transform(dataframe[columns])
    return dataframe


def select_feature(dataframe: pd.DataFrame, target_column: str, k: int = 3):
    """Select top K features based on mutual information with the target column."""
    if target_column not in dataframe.columns:
        print(f"Warning: '{target_column}' column not found for feature selection")
        return dataframe, None, dataframe.columns.tolist()

    X = dataframe.drop(columns=[target_column])
    y = dataframe[target_column]

    # Ensure k does not exceed available features
    k = min(k, X.shape[1])
    selector = SelectKBest(mutual_info_classif, k=k)
    X_new = selector.fit_transform(X, y)
    selected_columns = X.columns[selector.get_support()]
    print("Selected features:\n", selected_columns)
    return pd.DataFrame(X_new, columns=selected_columns), y, selected_columns


def prepare_features(dataframe):
    """Prepare features by encoding, normalizing, and handling target variable."""
    if dataframe is None or dataframe.empty:
        print("Error: DataFrame is empty or None")
        return None, None, None

    # Drop non-predictive columns like 'Full Name'
    if "Full Name" in dataframe.columns:
        dataframe.drop("Full Name", axis=1, inplace=True)

    categorical_columns = [
        col
        for col in dataframe.columns
        if dataframe[col].dtype == "object" and col != "Compliance_Label"
    ]
    for col in categorical_columns:
        dataframe[col] = LabelEncoder().fit_transform(dataframe[col])

    # Normalize numeric columns
    numerical_columns = ["Latitude", "Longitude"]
    dataframe = normalize_feature(dataframe, numerical_columns)

    # Create Compliance_Label if it doesn’t exist
    if "Compliance_Label" not in dataframe.columns:
        print(
            "Warning: 'Compliance_Label' column not found. Creating with example criteria."
        )
        dataframe["Compliance_Label"] = dataframe.apply(
            lambda row: (
                1 if pd.notnull(row["SSN"]) and pd.notnull(row["Tax ID"]) else 0
            ),
            axis=1,
        )

    # Encode categorical columns
    categorical_columns = [
        "SSN",
        "Passport Number",
        "Drivers License",
        "Tax ID",
        "City",
    ]
    for col in categorical_columns:
        if col in dataframe.columns:
            dataframe[col] = LabelEncoder().fit_transform(dataframe[col])

    # Define features (X) and target (y)
    X = dataframe.drop(columns=["Compliance_Label"], errors="ignore")
    y = dataframe["Compliance_Label"]

    # Perform feature selection if y is defined
    X, y, selected_columns = select_feature(dataframe, "Compliance_Label")

    return X, y, selected_columns
