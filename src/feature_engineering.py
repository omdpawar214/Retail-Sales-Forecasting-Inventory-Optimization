def create_features(df):
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day
    df['day_of_week'] = df['Date'].dt.dayofweek

    # Lag feature
    df['lag_1'] = df['Weekly_Sales'].shift(1)

    # Rolling mean
    df['rolling_mean_7'] = df['Weekly_Sales'].rolling(window=7).mean()

    df.fillna(0, inplace=True)

    return df

def add_seasonality(df):
    # Simulate festival boost (Nov-Dec high sales)
    df['festival'] = df['month'].apply(lambda x: 1 if x in [11, 12] else 0)

    # Increase sales artificially during festival
    df['Weekly_Sales'] = df.apply(
        lambda row: row['Weekly_Sales'] * 1.2 if row['festival'] == 1 else row['Weekly_Sales'],
        axis=1
    )

    return df

import numpy as np

def add_demand_variation(df):
    noise = np.random.normal(0, 0.05, len(df))  # 5% variation
    df['Weekly_Sales'] = df['Weekly_Sales'] * (1 + noise)
    return df