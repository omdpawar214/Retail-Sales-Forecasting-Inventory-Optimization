import pandas as pd

def load_data():
    train = pd.read_csv("data/raw/train.csv")
    features = pd.read_csv("data/raw/features.csv")
    stores = pd.read_csv("data/raw/stores.csv")
    return train, features, stores


def merge_data(train, features, stores):
    df = pd.merge(train, features, on=['Store', 'Date'], how='left')
    df = pd.merge(df, stores, on='Store', how='left')
    return df


def clean_data(df):
    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'])

    # Separate numeric and categorical columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(exclude=['number']).columns

    # Fill numeric columns with median
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical columns with mode
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df