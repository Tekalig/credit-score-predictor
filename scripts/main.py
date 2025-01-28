import numpy as np
from src.feature_engineering import create_aggregate_features, extract_time_based_features, encode_categorical_variables, handle_missing_values, normalize_features, standardize_features
from src.data_preprocessing import load_data, save_data

# Load the dataset
data_path = "../data/data.csv"  # Update with the actual path
df = load_data(data_path)

# Step 1: Create Aggregate Features
df = create_aggregate_features(df)

# Step 2: Extract Features
df = extract_time_based_features(df)

# Step 3: Encode Categorical Variables
df = encode_categorical_variables(df)

# Step 4: Handle Missing Values
df = handle_missing_values(df)

# Step 5: Normalize/Standardize Numerical Features
numerical_columns = df.select_dtypes(include=[np.number]).columns
df = normalize_features(df, numerical_columns)  # Normalize
df = standardize_features(df, numerical_columns)  # Standardize

# Save the processed data
processed_data_path = "../data/processed_transactions.csv"
save_data(df, processed_data_path)