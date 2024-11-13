import pandas as pd
import re

# Regex patterns for identifying PII fields
PII_Patterns = {
    "full_name": r"(?i)name",
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",  # Pattern for SSN
    "passport_number": r"passport",
    "drivers_license": r"license",
    "tax_id": r"tax|ssn",
    "email": r"^[\w\.-]+@[\w\.-]+\.\w+$",
    "ip_address": r"(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)",
    "mac_address": r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})",
    "telephone": r"\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b",
    "birth_date": r"\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b",  # Date formats
    "address": r"address|street|city|zip|postal",
    "geographical": r"(latitude|longitude|geo|coordinates)",
}


def check_sensitive_data(dataframe: pd.DataFrame):
    """Check for PII-Sensitive data aross columns"""
    print("Running Sensitive Data Checks")

    for col in dataframe.columns:
        for pii_type, pattern in PII_Patterns.items():
            if re.search(pattern, col, re.IGNORECASE):
                print(
                    f"Column '{col}' might contain sensitive PII data of type '{pii_type}'."
                )
    print("Sensitive Data Checks Completed")
