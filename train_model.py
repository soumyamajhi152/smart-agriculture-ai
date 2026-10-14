import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATA_URL = (
    "https://raw.githubusercontent.com/"
    "prasertcbs/basic-dataset/master/Crop_recommendation.csv"
)

FEATURES = [
    "N", "P", "K", "temperature",
    "humidity", "ph", "rainfall"
]


def train_crop_model():
    df = pd.read_csv(DATA_URL)

    X = df[FEATURES]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return model, accuracy
