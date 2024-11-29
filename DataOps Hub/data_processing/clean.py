import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Preprocessing column names: stripping, lowercasing, and replacing spaces with underscores.")
def preprocess_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe.columns = dataframe.columns.str.strip().str.lower().str.replace(' ', '_')
    return dataframe

def clean_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Clean the data by handling missing values, removing duplicates, and parsing data"""
    if dataframe is None or dataframe.empty:
        logging.error("Input Dataframe is None or empty in clean_data")
        return None

    # Log the initial shape of the DataFrame
    logging.info(f"Initial DataFrame shape: {dataframe.shape}")

    # Drop duplicates
    dataframe.drop_duplicates(inplace=True)

    # log the final shape after cleaning
    logging.info(f"Final DataFrame shape after cleaning: {dataframe.shape}")

    # Additional check to ensure dataframe is not empty after cleaning
    if dataframe.empty:
        logging.error("DataFrame is empty after cleaning")
        return None

    return dataframe
