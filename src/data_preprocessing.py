import pandas as pd

def load_data(file_path):
    """
    Load a dataset from a CSV file.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded dataset.
    """
    return pd.read_csv(file_path)

def detect_missing_values(data):
    """
    Detect missing values in a dataset.

    Args:
    data (pd.DataFrame): The input dataset.

    Returns:
    pd.Series: A series containing the number of missing values in each column.
    """
    return data.isnull().sum()

def save_data(data, file_path):
    """
    Save a dataset to a CSV file.

    Args:
    data (pd.DataFrame): The dataset to save.
    file_path (str): The path to the output CSV file.
    """
    data.to_csv(file_path, index=False)