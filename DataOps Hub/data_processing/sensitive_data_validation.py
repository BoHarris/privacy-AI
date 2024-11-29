import pandas as pd
import re

# Regex patterns for identifying PII fields
PII_Patterns = {
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",  # Pattern for SSN,
    "email": r"^[a-zA=Z0-9._%+-]+@[A-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "telephone": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",    
    "ip_address": r"(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)",
    "mac_address": r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})",
    "birth_date": r"\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b",  # Date formats
    "address": r"\d{1,5}\s(?:[A-Za-z]\.)?\s(?:\b[A-Za-z]+\b\s?){1,3}(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Way|Court|Ct|Circle|Cir|Place|Pl)\b(?:\s(?:Apt|Suite|Unit|#)?\s?\d{1,5})?",
    "geographical": r"-?(?:90(?:\.0+)?|[1-8]?\d(?:\.\d+)?),\s*-?(?:180(?:\.0+)?|(?:1[0-7]\d|[1-9]?\d)(?:\.\d+)?)",
    "us_zipcode": r"\b\d{5}(?:-\d{4})?\b",
    "credit_card_Number": r"\b(?:\d{4}[-.\s]?){3}\d{4}\b"
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
