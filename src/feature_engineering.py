import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def create_aggregate_features(df):
    df['total_transaction_amount'] = df.groupby('AccountId')['Amount'].transform('sum')
    df['average_transaction_amount'] = df.groupby('AccountId')['Amount'].transform('mean')
    df['transaction_count'] = df.groupby('AccountId')['Amount'].transform('count')
    df['std_transaction_amount'] = df.groupby('AccountId')['Amount'].transform('std').fillna(0)
    return df

def extract_time_based_features(df):
    df['transaction_hour'] = pd.to_datetime(df['TransactionStartTime']).dt.hour
    df['transaction_day'] = pd.to_datetime(df['TransactionStartTime']).dt.day
    df['transaction_month'] = pd.to_datetime(df['TransactionStartTime']).dt.month
    df['transaction_year'] = pd.to_datetime(df['TransactionStartTime']).dt.year
    return df


def encode_categorical_variables(df):
    label_encoder = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = label_encoder.fit_transform(df[col].astype(str))
    return df

def normalize_features(df, columns):
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def standardize_features(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def handle_missing_values(df):
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in ['float64', 'int64']:
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna('Unknown')
    return df
