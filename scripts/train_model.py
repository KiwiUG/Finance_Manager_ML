import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

DATA_DIR = "data/processed/"
MODEL_PATH = "model/general_model.pkl"
ACCURACY_PATH = "model/general_accuracy.txt"

def load_all_user_data():
    all_data = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith("_processed.csv"):
            df = pd.read_csv(os.path.join(DATA_DIR, filename))
            all_data.append(df)
    return pd.concat(all_data, ignore_index=True) if all_data else None

def train_general_model():
    df = load_all_user_data()
    if df is None or df.empty:
        print("❌ No processed data available for general model training.")
        return

    # Split features and target
    X = df.drop(columns=["category"])
    y = df["category"]

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Evaluate
    y_pred = model.predict(X)
    acc = accuracy_score(y, y_pred)

    # Save model and accuracy
    joblib.dump(model, MODEL_PATH)
    with open(ACCURACY_PATH, "w") as f:
        f.write(str(acc))

    print(f"✅ General model trained with accuracy: {acc:.2f}")

if __name__ == "__main__":
    train_general_model()
