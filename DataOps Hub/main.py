from data_processing.load import load_data
from data_processing.clean import clean_data
from data_processing.sensitive_data_validation import check_sensitive_data
from data_processing.export import export_data
import logging
import os
import pandas as pd

logging.basicConfig(level=logging.INFO)


def complete_pipeline(
    filepath: str,
    export_directory: str,
    filename: str = "processed_sensitive_data.csv",
    clean: bool = True,
    check_sensitivity: bool = True,
) -> pd.DataFrame:
    logging.info("Starting pipeline")

    # Load data
    try:
        df = load_data(filepath)
        if df is None or df.empty:
            logging.error("Dataframe is None or empty after loading")
            return None
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None
    # Clean data
    if clean:
        try:
            df = clean_data(df)
            if df is None or df.empty:
                logging.error("Dataframe is None or empty after cleaning")
                return None
            logging.info("Data cleaned successfully")
        except Exception as e:
            logging.error(f"Error cleaning data: {e}")
            return None

    # Sensitive Data Check
    if check_sensitivity:
        try:
            check_sensitive_data(df)
            logging.info("Sensitive data check completed")
        except Exception as e:
            logging.error(f"Errpr during sensitive data check: {e}")

    # Ensure the export directory exists
    os.makedirs(export_directory, exist_ok=True)
    processed_path = os.path.join(export_directory, filename)
    logging.info(f"Processed file path: {processed_path}")

    # Export the processed data
    try:
        export_data(df, processed_path)
        logging.info(f"Data exported successfully to {processed_path}")
    except Exception as e:
        logging.error(f"Error Exporting Data: {e}")
        return None
    logging.info("Pipeline completed and export")
    return df


# Useage
filepath = "c:/Users/Bokha/OneDrive/Desktop/privacy-AI/DataOps Hub/resources/raw/dataset_sensitive_info.csv"
export_directory = (
    "c:/Users/Bokha/OneDrive/Desktop/privacy-AI/DataOps Hub/resources/processed"
)
filename = "processed_sensitive_data.csv"
processed_data = complete_pipeline(filepath, export_directory, filename)
