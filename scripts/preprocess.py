import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

def preprocess_user_data(user_id):
    input_path = f"data/users/{user_id}.csv"
    output_path = f"data/processed/{user_id}_processed.csv"
    label_path = f"data/processed/{user_id}_label_encoders.pkl"

    if not os.path.exists(input_path):
        print(f"❌ No data found for user '{user_id}'")
        return

    df = pd.read_csv(input_path)

    # Drop rows with missing required values
    df = df.dropna(subset=["amount", "type", "category", "date"])

    # Convert date to datetime and extract useful features
    df["date"] = pd.to_datetime(df["date"])
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["weekday"] = df["date"].dt.weekday
    df = df.drop(columns=["date", "note"], errors="ignore")

    # Encode categorical values
    label_encoders = {}
    for col in ["type", "category"]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Save processed data
    df.to_csv(output_path, index=False)

    # Save encoders
    joblib.dump(label_encoders, label_path)

    print(f"✅ Preprocessed data for user '{user_id}' saved to '{output_path}'")
