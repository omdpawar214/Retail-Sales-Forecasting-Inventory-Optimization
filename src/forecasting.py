from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def train_model(df):

    # Reduce dataset size
    df = df.sample(n=20000, random_state=42)

    df = df.dropna()

    X = df.drop(['Weekly_Sales', 'Date'], axis=1)
    y = df['Weekly_Sales']

    # Encode categorical
    X = pd.get_dummies(X)

    X = X.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    print("Training model...")

    model = RandomForestRegressor(
        n_estimators=10,
        max_depth=5,
        n_jobs=-1,
        random_state=42
    )

    model.fit(X_train, y_train)

    print("Training completed!")

    predictions = model.predict(X_test)

    result = pd.DataFrame({
        'Actual': y_test.values,
        'Predicted': predictions
    })

    return model, result