import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def export_data(dataframe: pd.DataFrame, export_path: str):
    """Export the processed data to a CSV file."""
    try:
        dataframe.to_csv(export_path, index=True)
        logging.info(f"Data exported to {export_path}")
    except Exception as e:
        logging.error(f"Error exporting data: {e}")
