import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


def normalize_feature(dataframe: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Normalize a numerical column to the range [0,1]"""
    scaler = MinMaxScaler()
    dataframe[f"Normalize_{column_name}"] = scaler.fit_transform(
        dataframe[[column_name]]
    )
    return dataframe


def encode_feature(dataframe: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Encode a categorical column using Label Encoding"""
    encoder = LabelEncoder()
    dataframe[f"{column_name}_encoded"] = encoder.fit_transform(dataframe[column_name])
    return dataframe


def prepare_features(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Prepare all necessary feature for the ML model"""
    # Normalize numerical features
    if "Age" in dataframe.columns:
        dataframe = normalize_feature(dataframe, "Age")

        # Encode categorizal feature
        dataframe = encode_feature(dataframe, "Category")

        # Add any additional feature engineering steps

        return dataframe
