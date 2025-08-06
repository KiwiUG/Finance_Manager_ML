import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_personal_model(user_id):
    input_path = f"data/processed/{user_id}_processed.csv"
    model_path = f"model/users/{user_id}_model.pkl"
    accuracy_path = f"model/users/{user_id}_accuracy.txt"

    if not os.path.exists(input_path):
        print(f"❌ Preprocessed data not found for {user_id}")
        return

    df = pd.read_csv(input_path)

    # Feature & target selection (modify target based on goal)
    X = df.drop(columns=["category"])  # 🧠 Predict category from other fields
    y = df["category"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate and save model
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    os.makedirs("model/users", exist_ok=True)
    joblib.dump(model, model_path)
    with open(accuracy_path, "w") as f:
        f.write(f"{acc:.4f}")

    print(f"✅ Model trained for {user_id} with accuracy: {acc:.4f}")
